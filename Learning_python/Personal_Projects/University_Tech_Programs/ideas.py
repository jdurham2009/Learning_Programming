import csv

class Program:
    def __init__(self, University_Name, Location, Degree_Level, Major):
        self.University_Name = University_Name
        self.Location = Location
        self.Degree_Level = Degree_Level
        self.Major = Major

    def __str__(self):
        return f"{self.University_Name} | {self.Location} | {self.Degree_Level} | {self.Major}"


def load_data():
    program = []
    with open("University_Tech_Programs.csv", "r", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            p = Program(
                row["University_Name"],
                row["Location"],
                row["Degree_Level"],
                row["Major"]
            )
            program.append(program)

    return program

def search_data(data, field_name, search_term):
    results = []
    search_term = search_term.strip().lower()
    for program in data:
        value = getattr(program, field_name)
        if search_term in value.lower():
            results.append(program)
    return results

def display_results(results):
    if not results:
        print("No matching records found.")
        return
    else:
        print("\nMatching Programs:\n")
        for result in results:
            print(results)


def find_university(data):
    choice = input("What University do you want to search?\n")
    results = search_data(data, "University_Name", choice)
    try:
        display_results(results)
    except:
        print("University not found")

def find_major(data):
    choice = input("What Major do you want to search?\n")
    results = search_data(data, "Major", choice)
    try:
        display_results(results)
    except:
        print("Major not found")

def find_degree_level(data):
    choice = input("What Degree Level do you want to search? Bachelors or Masters?\n").strip().lower()
    results = search_data(data, "Degree_Level", choice)
    try:
        display_results(results)
    except:
        print("Degree Level not found")

def find_location(data):
    choice = input("What Location do you want to search?\n")
    results = search_data(data, "Location", choice)
    try:
        display_results(results)
    except:
        print("Location not found")

def main():
    data = load_data()
    fieldname = input("What do you want to search for?(Program, University, Major, Degree Level, Location)\n").strip()

    if fieldname == "Program":
        search_data()
    elif fieldname == "University":
        find_university()
    elif fieldname == "Major":
        find_major()
    elif fieldname == "Degree Level":
        find_degree_level()
    elif fieldname == "Location":
        find_location()
    else:
        print("Input Invalid")

main()