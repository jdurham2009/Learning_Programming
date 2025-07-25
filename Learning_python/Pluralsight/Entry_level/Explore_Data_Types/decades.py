# Calculates the decades and years of a person's age
age = int(input("How old are you?\n"))
decades = age // 10
years = age % 10
print("You are " + str(decades) + " decades and " + str(years) + " years old.")