import csv
file_path = r"C:\Users\jdurh\OneDrive\Desktop\IT\Learning_Programming\Personal_Projects\Python\University_Tech_Programs\University_Tech_Programs.csv"
filename = "University_Tech_Programs.csv"

def load_data():
    data = []
    with open(file_path, "r") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data  


def search_data(data, field_name, search_term):
    results = []
    search_term = search_term.lower()
    for row in data:
       # print(f"Checking: {row[field_name].lower()}")  # Debug line
        if search_term in row[field_name].lower():
            results.append(row)
    return results

def display_results(results):
    if not results:
        print("No matching records found.")
        return

    lines = []
    for row in results:
        # Format each line with newline at the end
        line = (
            f"University_Name: {row['University_Name']} | "
            f"Location: {row['Location']} | "
            f"Degree_Level: {row['Degree_Level']} | "
            f"Major: {row['Major']}\n"
        )
        print(line, end='')    # Print to console
        lines.append(line)     # Append to list for file writing

    export = input("Do you want to export the results to a file? (yes/no): ").strip().lower()
    if export == "yes":
        filename = input("Enter file name without extension:\n").strip()
        if not filename:
            print("Filename cannot be empty. Aborting export.")
            return
        filepath = filename + ".txt"

        try:
            # Check if file exists
            file_exists = os.path.exists(filepath)

            # Open in append ('a') mode if it exists, else write ('w')
            with open(filepath, "a" if file_exists else "w", encoding="utf-8") as f:
                if file_exists:
                    f.write("\n--- Appended Results ---\n")
                f.writelines(lines)
            print(f"Results {'appended to' if file_exists else 'exported to'} {filepath}")
        except Exception as e:
            print(f"Failed to write file: {e}")
    else:
        print("Okay, not exporting.")


"""    export = input("Do you want to export the results to a file? (yes/no): ").strip().lower()
    if export == "yes":
        filename = input("Enter file name without extension:\n").strip()
        if not filename:
            print("Filename cannot be empty. Aborting export.")
            return
        filepath = filename + ".txt"
        try:
            with open(filepath, "a" if file_exists else "w", encoding="utf-8") as f:
                f.writelines(lines)
            print(f"Results exported to {filepath}")
        except Exception as e:
            print(f"Failed to write file: {e}")
    else:
        print("Okay, not exporting.")"""

def find_university(data):
    choice = input("Which University do you want to search?:\n")
    results = search_data(data, "University_Name", choice)
    if results:
        display_results(results)
    else:
        print("University not found")


def find_major(data):
    choice = input("What Major do you want to search?\n")
    results = search_data(data, "Major", choice)
    if results:
        display_results(results)
    else:
        print("Major not found")


def find_degree_level(data):
    choice = input("What Degree Level do you want to search? Bachelors or Masters?\n").strip().lower()
    results = search_data(data, "Degree_Level", choice)
    if results:
        display_results(results)
    else:
        print("Degree Level not found")

def find_location(data):
    choice = input("What Location do you want to search?\n")
    results = search_data(data, "Location", choice)
    if results:
        display_results(results)
    else:
        print("Location not found")

def main():
    data = load_data()
    
    while True:
        fieldname = input("\nSearch by: University, Major, Degree Level, Location (or type 'exit' to quit)\n").strip().lower()

        if fieldname == "university":
            find_university(data)
        elif fieldname == "major":
            find_major(data)
        elif fieldname == "degree level":
            find_degree_level(data)
        elif fieldname == "location":
            find_location(data)
        elif fieldname == "exit":
            print("Goodbye!")
            break
        else:
            print("Invalid input. Please try again.")


main()
