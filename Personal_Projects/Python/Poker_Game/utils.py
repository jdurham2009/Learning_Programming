import random
import itertools
import math

# ---------- Card / Deck ----------
SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
RANK_VALUE = {r: i+2 for i, r in enumerate(RANKS)}  # 2 -> 2, ..., Ace -> 14

def create_deck():
    deck = [(rank, suit) for suit in SUITS for rank in RANKS]
    random.shuffle(deck)
    return deck

def card_to_str(card):
    rank, suit = card
    return f"{rank} of {suit}"

def hand_list_to_str(hand):
    return ", ".join(card_to_str(c) for c in hand)

# ---------- Player ----------
class Player:
    def __init__(self, name, chips=1000):
        self.name = name
        self.chips = chips
        self.hand = []             # hole cards (2)
        self.active = True         # still in hand (not folded)
        self.current_bet = 0       # bet in current betting round
        self.in_round = True       # has chips > 0, used for round elimination

    def reset_for_round(self):
        self.hand = []
        self.active = True
        self.current_bet = 0

    def __str__(self):
        return f"{self.name} (Chips: {self.chips})"

# ---------- Hand Evaluation ----------
# Returns tuple: (category, tiebreaker list) where higher tuple is better.
# Categories: 8 Straight Flush, 7 Four of a Kind, 6 Full House, 5 Flush, 4 Straight,
# 3 Three of a Kind, 2 Two Pair, 1 One Pair, 0 High Card

def evaluate_7card_hand(cards):
    """
    cards: list of (rank, suit) tuples, up to 7 cards
    returns: (category, tiebreakers_list)
    """
    # Convert ranks to numeric values and group by rank and suit
    values = sorted([RANK_VALUE[r] for r, s in cards], reverse=True)
    suits = {}
    ranks = {}
    for r, s in cards:
        v = RANK_VALUE[r]
        suits.setdefault(s, []).append(v)
        ranks.setdefault(v, 0)
        ranks[v] += 1

    # ----- Flush check -----
    flush_suit = None
    flush_values = []
    for s, vals in suits.items():
        if len(vals) >= 5:
            flush_suit = s
            flush_values = sorted(vals, reverse=True)
            break

    # ----- Straight check helper -----
    def get_straight_high(vals):
        """Given a set/list of values, return high card of straight or None. Handles wheel A-2-3-4-5."""
        vv = sorted(set(vals))
        # Wheel check: Ace treated as 1 for A-2-3-4-5
        if 14 in vv:
            vv = vv + [1]  # Ace low possibility
        max_run = None
        run = []
        prev = None
        for x in vv:
            if prev is None or x == prev + 1:
                run.append(x)
            else:
                run = [x]
            prev = x
            if len(run) >= 5:
                max_run = run[:]  # keep latest run of length>=5
        if max_run:
            return max_run[-1] if max_run[-1] != 1 else 5  # if Ace-low, high is 5
        return None

    # Straight across all cards
    straight_high = get_straight_high(values)

    # Straight flush
    straight_flush_high = None
    if flush_suit:
        straight_flush_high = get_straight_high(suits[flush_suit])

    # ----- Group counts -----
    # Build lists of ranks by count
    counts = {}
    for v, cnt in ranks.items():
        counts.setdefault(cnt, []).append(v)
    # For determinism sort descending
    for k in counts:
        counts[k].sort(reverse=True)

    # Determine category with tiebreakers
    # Straight Flush
    if straight_flush_high:
        return (8, [straight_flush_high])

    # Four of a Kind
    if 4 in counts:
        four_val = counts[4][0]
        kickers = sorted([v for v in values if v != four_val], reverse=True)
        return (7, [four_val] + kickers[:1])

    # Full House (three + pair). If two trips, top trip acts as three, second trip acts as pair.
    if 3 in counts and (2 in counts or len(counts[3]) >= 2):
        three_val = counts[3][0]
        # pair candidate is highest of pairs or other triples
        pair_val = None
        if 2 in counts:
            pair_val = counts[2][0]
        if len(counts[3]) >= 2:
            pair_val = counts[3][1] if pair_val is None else max(pair_val, counts[3][1])
        return (6, [three_val, pair_val])

    # Flush
    if flush_suit:
        top5 = flush_values[:5]
        return (5, top5)

    # Straight
    if straight_high:
        return (4, [straight_high])

    # Three of a Kind
    if 3 in counts:
        three_val = counts[3][0]
        kickers = sorted([v for v in values if v != three_val], reverse=True)
        return (3, [three_val] + kickers[:2])

    # Two Pair
    if 2 in counts and len(counts[2]) >= 2:
        pair1, pair2 = counts[2][0], counts[2][1]
        kickers = sorted([v for v in values if v != pair1 and v != pair2], reverse=True)
        return (2, [pair1, pair2] + kickers[:1])

    # One Pair
    if 2 in counts and len(counts[2]) == 1:
        pair_val = counts[2][0]
        kickers = sorted([v for v in values if v != pair_val], reverse=True)
        return (1, [pair_val] + kickers[:3])

    # High Card
    return (0, values[:5])

def compare_hands(h1, h2):
    """Compare two evaluation tuples. Return 1 if h1>h2, -1 if h1<h2, 0 if tie."""
    if h1[0] != h2[0]:
        return 1 if h1[0] > h2[0] else -1
    # same category: compare tiebreakers lexicographically
    for a, b in itertools.zip_longest(h1[1], h2[1], fillvalue=0):
        if a != b:
            return 1 if a > b else -1
    return 0

# ---------- Betting System ----------
def collect_blinds(players, dealer_idx, small_blind=5, big_blind=10):
    num = len(players)
    sb_idx = (dealer_idx + 1) % num
    bb_idx = (dealer_idx + 2) % num
    pot = 0
    # small blind
    sb = players[sb_idx]
    sb_amount = min(sb.chips, small_blind)
    sb.chips -= sb_amount
    sb.current_bet += sb_amount
    pot += sb_amount
    # big blind
    bb = players[bb_idx]
    bb_amount = min(bb.chips, big_blind)
    bb.chips -= bb_amount
    bb.current_bet += bb_amount
    pot += bb_amount
    print(f"{sb.name} posts small blind {sb_amount}. {bb.name} posts big blind {bb_amount}.")
    return pot, sb_idx, bb_idx

def betting_round(players, starting_idx, pot):
    """
    Conducts a betting round. Players is list of Player objects in seating order.
    starting_idx: index of player to act first
    Returns updated pot.
    """
    num = len(players)
    active_players = [p for p in players if p.active and p.chips > 0]
    if len(active_players) <= 1:
        return pot

    highest_bet = max(p.current_bet for p in players)
    i = 0
    # track whether each active player has acted since last raise
    acted = {idx: False for idx in range(num)}
    # only consider players who are active
    while True:
        idx = (starting_idx + i) % num
        player = players[idx]
        i += 1

        # skip players who folded or are out of chips entirely
        if not player.active or player.chips == 0:
            acted[idx] = True
            # if they're all-in with current_bet less than highest_bet, we still treat them as acted
            if all(acted.get(j, True) for j in range(num) if players[j].active and players[j].chips > 0):
                break
            if i > num*3:
                break
            continue

        to_call = highest_bet - player.current_bet
        prompt_parts = ["(check)" if to_call == 0 else f"(call {to_call})", "(raise)", "(fold)", "(all-in)"]
        prompt = f"{player.name} - Chips: {player.chips} - Your bet: {player.current_bet} - Highest bet: {highest_bet}. Choose action {prompt_parts}: "
        action = input(prompt).strip().lower()

        if action in ["check", "c"] and to_call == 0:
            print(f"{player.name} checks.")
            acted[idx] = True

        elif action in ["call", "call " + str(to_call)] or (action == "c" and to_call > 0):
            # call (or partial all-in if not enough chips)
            pay = min(player.chips, to_call)
            player.chips -= pay
            player.current_bet += pay
            pot += pay
            print(f"{player.name} calls {pay}.")
            acted[idx] = True

        elif action.startswith("raise") or action.startswith("r"):
            # Allow "raise 50" or "r"
            parts = action.split()
            if len(parts) == 2 and parts[1].isdigit():
                raise_amt = int(parts[1])
            else:
                raise_amt = None
                try:
                    raise_amt = int(input("Enter raise amount (additional on top of call): "))
                except Exception:
                    print("Invalid raise. Treating as call.")
                    raise_amt = 0
            # total additional to match highest_bet + raise_amt
            pay_to_call = max(0, highest_bet - player.current_bet)
            total_needed = pay_to_call + raise_amt
            if total_needed >= player.chips:
                # all-in raise
                total_needed = player.chips
                print(f"{player.name} goes all-in with {total_needed}.")
            player.chips -= total_needed
            player.current_bet += total_needed
            pot += total_needed
            highest_bet = player.current_bet
            # reset acted flags for others so they have chance to respond to raise
            acted = {k: False for k in acted}
            acted[idx] = True
            print(f"{player.name} raises. New highest bet: {highest_bet}.")

        elif action in ["fold", "f"]:
            player.active = False
            print(f"{player.name} folds.")
            acted[idx] = True

        elif action in ["all-in", "allin", "a"]:
            allin_amt = player.chips
            player.current_bet += allin_amt
            player.chips = 0
            pot += allin_amt
            if player.current_bet > highest_bet:
                highest_bet = player.current_bet
                acted = {k: False for k in acted}
            acted[idx] = True
            print(f"{player.name} goes all-in with total bet {player.current_bet}.")

        else:
            print("Unknown action; please try again.")
            # step back so same player chooses again
            i -= 1
            continue

        # Termination: if all active players have acted and their current_bet equals highest_bet (or they're all-in),
        # then betting round ends.
        def player_needs_action(j):
            pj = players[j]
            if not pj.active:
                return False
            if pj.chips == 0:
                # if they're all-in and their current_bet <= highest_bet, they don't need action
                return False
            return pj.current_bet != highest_bet

        if all(acted.get(j, True) for j in range(num) if players[j].active):
            # Also ensure no one still owes a bet (i.e., current_bet != highest_bet) among players with chips
            if not any(player_needs_action(j) for j in range(num)):
                break

        # safety to avoid infinite loops
        if i > num * 10:
            break

    return pot

# ---------- Game Flow ----------
def deal_hole_cards(deck, players):
    for _ in range(2):
        for p in players:
            if p.chips > 0:
                p.hand.append(deck.pop(0))

def reveal_flop(deck):
    deck.pop(0)  # burn
    return [deck.pop(0) for _ in range(3)]

def reveal_turn_or_river(deck):
    deck.pop(0)  # burn
    return deck.pop(0)

def showdown(players, community_cards, pot):
    active = [p for p in players if p.active]
    if len(active) == 1:
        winner = active[0]
        print(f"{winner.name} wins the pot of {pot} by everyone else folding!")
        winner.chips += pot
        return

    evals = []
    print("\n--- Showdown ---")
    for p in active:
        full_cards = p.hand + community_cards
        ev = evaluate_7card_hand(full_cards)
        evals.append((p, ev))
        print(f"{p.name}: {hand_list_to_str(p.hand)}  => {ev}")

    # Find best eval
    best = evals[0]
    winners = [best[0]]
    for p, ev in evals[1:]:
        cmp = compare_hands(ev, best[1])
        if cmp == 1:
            best = (p, ev)
            winners = [p]
        elif cmp == 0:
            # tie -> need to compare both ev tuples
            if compare_hands(ev, best[1]) == 0:
                winners.append(p)

    # If multiple winners: split pot evenly (simple split). Remainder goes to first winner.
    share = pot // len(winners)
    remainder = pot - share * len(winners)
    for i, w in enumerate(winners):
        award = share + (remainder if i == 0 else 0)
        w.chips += award
        print(f"{w.name} wins {award} chips.")
    print("")

# ---------- Main Game Loop ----------
def play_texas_holdem():
    print("=== Text-based Texas Hold'em ===")
    try:
        num_players = int(input("Number of players (2-8): "))
    except Exception:
        print("Invalid number; defaulting to 2.")
        num_players = 2
    num_players = max(2, min(8, num_players))

    players = []
    for i in range(num_players):
        name = input(f"Enter name for player {i+1} (leave blank for 'Player {i+1}'): ").strip()
        if not name:
            name = f"Player {i+1}"
        players.append(Player(name, chips=1000))

    dealer_idx = 0
    small_blind = 5
    big_blind = 10

    round_num = 1
    while True:
        print(f"\n--- Round {round_num} ---")
        # Remove players with zero chips from play
        active_table = [p for p in players if p.chips > 0]
        if len(active_table) <= 1:
            if active_table:
                print(f"{active_table[0].name} is the winner of the game!")
            else:
                print("No players with chips remain. Game over.")
            break

        # Reset players for round and create deck
        for p in players:
            p.reset_for_round()
            if p.chips == 0:
                p.active = False
        deck = create_deck()

        # Rotate dealer
        dealer_idx = dealer_idx % len(players)
        print(f"Dealer: {players[dealer_idx].name}")

        # Collect blinds
        pot, sb_idx, bb_idx = collect_blinds(players, dealer_idx, small_blind, big_blind)

        # Deal hole cards
        deal_hole_cards(deck, players)
        for p in players:
            if p.hand:
                print(f"{p.name} hole cards: {hand_list_to_str(p.hand)}")

        # Pre-flop betting: first action is player after big blind
        first_to_act = (bb_idx + 1) % len(players)
        pot = betting_round(players, first_to_act, pot)

        # If only one active player remains after betting, immediate showdown/award
        if sum(1 for p in players if p.active) <= 1:
            showdown(players, [], pot)
            # move dealer, next round
            dealer_idx += 1
            round_num += 1
            continue

        # Flop
        community = reveal_flop(deck)
        print(f"\nFlop: {hand_list_to_str(community)}")
        # betting starts at player after dealer
        pot = betting_round(players, (dealer_idx + 1) % len(players), pot)
        if sum(1 for p in players if p.active) <= 1:
            showdown(players, community, pot)
            dealer_idx += 1
            round_num += 1
            continue

        # Turn
        community.append(reveal_turn_or_river(deck))
        print(f"\nTurn: {hand_list_to_str(community)}")
        pot = betting_round(players, (dealer_idx + 1) % len(players), pot)
        if sum(1 for p in players if p.active) <= 1:
            showdown(players, community, pot)
            dealer_idx += 1
            round_num += 1
            continue

        # River
        community.append(reveal_turn_or_river(deck))
        print(f"\nRiver: {hand_list_to_str(community)}")
        pot = betting_round(players, (dealer_idx + 1) % len(players), pot)

        # Showdown
        showdown(players, community, pot)

        # Move dealer to next seated player with chips
        dealer_idx += 1
        round_num += 1

        # Check if users want to continue or stop
        cont = input("Continue playing? (y/n) ").strip().lower()
        if cont not in ["", "y", "yes"]:
            print("Ending game. Final chip counts:")
            for p in players:
                print(f"{p.name}: {p.chips}")
            break

if __name__ == "__main__":
    play_texas_holdem()