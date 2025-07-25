#Search for or add University using University Tech File file
def find_university():
    look_up = input("What University would you like to look up?\n")

    found = False
    try:
        with open("University_Tech_Programs.txt", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if look_up in row["University_Name"].lower():
                    print(f"{row['University_Name']} | {row['Location']} | {row['Degree_Level']} | {row['Major']}")
                    found = True
        if not found:
            print("University not found.")
    except FileNotFoundError:
        print("File not found.")

    try:
        with open("University_Tech_Programs.txt", "a", newline='') as file:
            writer = csv.writer(file)
            writer.writerow([university, location, degree, major])
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
main()