def write_to_file(madlib_text):
    file_path = r"C:\Users\jdurh\OneDrive\Desktop\IT\Learning_Programming\Personal_Projects\Python\Madlibs\madlib.txt"
    with open(file_path, "a", encoding="utf-8") as file:
        file.write(madlib_text)
    print(f"✅ Madlib saved successfully to:\n{file_path}")


def lib_1():
    print("Madlib: It's About Time")
    pluralnoun_1 = input("Give me a plural noun\n")
    pluralnoun_2 = input("Another plural noun\n")
    pluralnoun_3 = input("Another plural noun\n")
    number1 = int(input("Give me a number\n"))
    pluralnoun_4 = input("OMG another plural noun\n")
    noun_1 = input("Give me a noun (singular)\n")
    noun_2 = input("Give me another singular noun\n")
    noun_3 = input("Give me another singular noun\n")
    noun_4 = input("Another singular noun\n")
    bodypart_1 = input("Body Part\n")
    letter = input("Choose a letter of the alphabet\n")
    pluralnoun_5 = input("Back to plural nouns, give another one\n")
    pluralnoun_6 = input("Plural Noun\n")
    pluralnoun_7 = input("Plural Noun\n")
    bodypart_2 = input("Part of the body\n")
    bodypart_3 = input("Another part of the body\n")
    number2 = int(input("Give me a number\n"))
    adjective = input("Give me an adjective\n")
    noun_5 = input("Last one, give me a noun\n")

    return (
        f"\n~~~It's About Time~~~\n"
        f"Thousands of {pluralnoun_1} ago, there were calendars that enabled the ancient {pluralnoun_2}\n"
        f"to divide a year into twelve {pluralnoun_3}, each month into {number1} weeks,\n"
        f"and each week into seven {pluralnoun_4}. At first, people told time by a sun clock,\n"
        f"sometimes known as the {noun_1}. Ultimately, they invented the great timekeeping devices of today,\n"
        f"such as the grandfather {noun_2}, the pocket {noun_3}, the alarm {noun_4}, and, of course, the\n"
        f"{bodypart_1} watch. Children learn about clocks and time almost before they learn their AB{letter}.\n"
        f"They are taught that a day consists of 24 {pluralnoun_5}, an hour has 60 {pluralnoun_6},\n"
        f"and a minute has 60 {pluralnoun_7}. By the time they are in kindergarten, they know if the big\n"
        f"{bodypart_2} is at twelve and the little {bodypart_3} is at three, that it is {number2}.\n"
        f"I wish we could continue this {adjective} lesson, but we’ve run out of {noun_5}.\n"
    )


def lib_2():
    print("Madlib: Office Shenanigans")
    job_title_1 = input("Give me a job title.\n")
    verb_ing = input("Give me a verb ending in -ing.\n")
    noun_1 = input("Give me a noun.\n")
    adjective = input("Give me an adjective.\n")
    room = input("Give me a room in the house.\n")
    drink = input("Give me a type of drink.\n")
    celebrity = input("Name a celebrity.\n")
    bodypart_1 = input("Name a body part.\n")
    noun_2 = input("Give me a noun.\n")
    exclamation = input("Give me an exclamation.\n")
    verb_past = input("Give a past tense verb.\n")
    job_title_2 = input("Give me a job title.\n")
    noise = input("Give me a weird noise.\n")
    emotion = input("Name an emotion.\n")
    bodypart_2 = input("Another part of the body\n")

    return (
        f"\n~~~Office Shenanigans~~~\n"
        f"It was just another day at the office when the {job_title_1} got caught {verb_ing} with a {noun_1} in the break room.\n"
        f"Everyone knew it was going to be a {adjective} kind of day.\n"
        f"I walked into the {room} with my morning {drink} and saw {celebrity} giving a motivational speech\n"
        f"to the interns about the importance of keeping your {bodypart_1} clean and your {noun_2} charged.\n"
        f"Suddenly, someone yelled, \"{exclamation}!\" and the printer {verb_past} into flames.\n"
        f"The {job_title_2} tried to fix it by smacking it and yelling \"{noise}\" but honestly, that just made things worse.\n"
        f"At that point, I was so {emotion} I almost fell off my {bodypart_2}.\n"
    )


def main():
    choice = input("Which MadLib do you want to do?\n"
                   "1. It's About Time!\n"
                   "2. Office Shenanigans\n").strip()
    if choice == "1":
        madlib_text = lib_1()
        write_to_file(madlib_text)
    elif choice == "2":
        madlib_text = lib_2()
        write_to_file(madlib_text)
    else:
        print("Invalid input. Please type 1 or 2.")

main()
