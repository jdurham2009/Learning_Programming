#Create a mad lib and add it to a file
""" Mad Lib
Thousands of 
 
    1 PLURAL NOUN ago, there were calendars that enabled the ancient 
 
    2 PLURAL NOUN to divide a year into twelve 
 
    3 PLURAL NOUN, each month into 
 
    1 NUMBER weeks, and each week into seven 
 
    4 PLURAL NOUN. At first, people told time by a sun clock, sometimes known as the 
 
    1 NOUN dial. Ultimately, they invented the great timekeeping devices of today, such as the grandfather 
 
    2 NOUN, the pocket 
 
    3 NOUN, the alarm 
 
    4 NOUN, and, of course, the 
 
    1 PART OF BODY watch. Children learn about clocks and time almost before they learn their AB 
 
    LETTER OF THE ALPHABETs. They are taught that a day consists of 24 
 
    5 PLURAL NOUN, an hour has 60 
 
    6 PLURAL NOUN, and a minute has 60 
 
    7 PLURAL NOUN. By the time they are in kindergarten, they know if the big 
 
    2 PART OF THE BODY is at twelve and the little 
 
    3 PART OF THE BODY is at three, that it is 
 
    2 NUMBER oclock. I wish we could continue this 
 
    ADJECTIVE lesson, but weve run out of 
 
NOUN.
"""
def fill_blanks():
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
    if number2 == number1:
        input("You arlready chose this, pick another number\n")
    adjective = input("Give me an adjective\n")
    noun_5 = input("Last one, give me a noun\n")

    madlib_text = (
        f"Thousands of {pluralnoun_1} ago, there were calendars that enabled the ancient {pluralnoun_2}\n"
        f"to divide a year into twelve {pluralnoun_3}, each month into {number1} weeks,\n"
        f"and each week into seven {pluralnoun_4}. At first, people told time by a sun clock,\n"
        f"sometimes known as the {noun_1}. Ultimately, they invented the great timekeeping devices of today,\n"
        f"such as the grandfather {noun_2}, the pocket {noun_3}, the alarm {noun_4}, and, of course, the,\n"
        f"{bodypart_1} watch. Children learn about clocks and time almost before they learn their AB{letter}.\n"
        f"They are taught that a day consists of 24 {pluralnoun_5}, an hour has 60 {pluralnoun_6},\n"
        f"and a minute has 60 {pluralnoun_7}. By the time they are in kindergarten, they know if the big\n"
        f"{bodypart_2} is at twelve and the little {bodypart_3} is at three, that it is {number2}.\n"
        f"I wish we could continue this {adjective} lesson, but we’ve run out of {noun_5}.\n"
    )


    file_path = r"C:\Users\jdurh\OneDrive\Desktop\IT\Learning_Programming\Learning_python\Personal_Projects\Madlibs\madlib.txt"
    with open(file_path, "a") as file:
        file.write(madlib_text)

    print(f"✅ Madlib saved successfully to:\n{file_path}")

        
def main():
    choice = input("Do you want to do a Madlib Yes(Y) or NO(N)?\n")
    if choice == "Y":
        fill_blanks()
    elif choice == "N":
        print("Ok, Bye")
    else:
        print("Invalid input. Please type 'Y' or 'N'.")

main()





    





 