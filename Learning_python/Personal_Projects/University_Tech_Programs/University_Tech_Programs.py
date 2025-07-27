import csv

filename = "University_Tech_Programs.csv"

def load_data():
    data = []
    with open(filename, "r", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data  

def search_data(data, field_name, search_term):
    results = []
    search_term = search_term.lower()
    for row in data:
        if search_term in row[field_name].lower():
            results.append(row)
    return results

def display_results(results):
    if not results:
        print("No matching records found.")
        return
    for row in results:
        print(row)

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
    results = search_data(data, "Degree", choice)
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
    fieldname = input("What do you want to search for? (University, Major, Degree Level, Location)\n").strip()

    if fieldname == "University":
        find_university(data)
    elif fieldname == "Major":
        find_major(data)
    elif fieldname == "Degree Level":
        find_degree_level(data)
    elif fieldname == "Location":
        find_location(data)
    else:
        print("Input Invalid")

main()
