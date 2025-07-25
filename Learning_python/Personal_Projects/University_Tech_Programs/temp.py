import csv
import os

FILENAME = "University_Tech_Programs.txt"
FIELDNAMES = ["University_Name", "Location", "Degree_Level", "Major"]

def search_by_field(field_name):
    search_term = input(f"Enter {field_name.replace('_', ' ')} to search:\n").strip().lower()
    found = False

    try:
        with open(FILENAME, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if search_term in row[field_name].lower():
                    print(f"{row['University_Name']} | {row['Location']} | {row['Degree_Level']} | {row['Major']}")
                    found = True
        if not found:
            print(f"No results found for '{search_term}'.")
    except FileNotFoundError:
        print(f"File '{FILENAME}' not found.")

def list_all_programs():
    try:
        with open(FILENAME, "r") as file:
            reader = csv.DictReader(file)
            print("\nAll University Programs:")
            count = 0
            for row in reader:
                print(f"{row['University_Name']} | {row['Location']} | {row['Degree_Level']} | {row['Major']}")
                count += 1
            if count == 0:
                print("No entries found.")
    except FileNotFoundError:
        print(f"File '{FILENAME}' not found.")

def list_majors():
    majors = set()
    try:
        with open(FILENAME, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                major = row["Major"].strip()
                if major:
                    majors.add(major)
        if majors:
            print("\nList of Majors:")
            for m in sorted(majors):
                print("-", m)
        else:
            print("No majors found.")
    except FileNotFoundError:
        print(f"File '{FILENAME}' not found.")

def add_university():
    university = input("Enter University Name:\n").strip()
    location = input("Enter Location:\n").strip()
    degree = input("Enter Degree Level (Bachelors or Masters):\n").strip()
    major = input("Enter Major:\n").strip()

    new_entry = {
        "University_Name": university,
        "Location": location,
        "Degree_Level": degree,
        "Major": major
    }

    try:
        if os.path.isfile(FILENAME):
            with open(FILENAME, "r", newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if all(row[k].strip().lower() == new_entry[k].lower() for k in FIELDNAMES):
                        print("This entry already exists. Not adding duplicate.")
                        return

        file_exists = os.path.isfile(FILENAME)
        with open(FILENAME, "a", newline='') as file:
            writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
            if not file_exists:
                writer.writeheader()
            writer.writerow(new_entry)
        print("University added successfully.")

    except Exception as e:
        print("Error writing to file:", e)

def main():
    while True:
        print("\n--- University Program Search ---")
        print("1: Search by University Name")
        print("2: Search by Location")
        print("3: Search by Major")
        print("4: List All University Programs")
        print("5: List All Majors")
        print("6: Add a University Program")
        print("7: Quit")

        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            search_by_field("University_Name")
        elif choice == "2":
            search_by_field("Location")
        elif choice == "3":
            search_by_field("Major")
        elif choice == "4":
            list_all_programs()
        elif choice == "5":
            list_majors()
        elif choice == "6":
            add_university()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 7.")

if __name__ == "__main__":
    main()
