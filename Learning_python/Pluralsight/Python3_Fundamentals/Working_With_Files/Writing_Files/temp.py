# Ask what acronym to add
# Ask user for Definition
#Open file
#Write to file

acronym = input("What acronym do you want to add?\n")
definition = input("What definition do you want to add?\n")
with open(""acronym.txt", "a") as file:
          file.write(acronym + " - " + definition + "\n")