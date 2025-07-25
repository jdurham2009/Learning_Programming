#Temporary file
acronym = input("What acronym do you want to add?\n")
definition = input("What definition do you want to add?\n")
with open("acronyms.txt", "a") as file:
    file.write(acronym + " - " + definition + "\n")