#Given a Spanish ID number, return the correct letter
def get_letter(ID):
    remainder = ID%23
    letters = ['T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X', 'B', 'N', 'J', 'Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K', 'E']
    return letters[remainder]

ID_number = int(input("Enter an ID number:"))
print("The letter corresponding to the ID number", ID_number, "is", get_letter(ID_number))

#Check if a Spanish ID number+letter has the correct format
def is_correct(ID_with_letter):
    number = int(ID_with_letter[0:8])
    letter = str(ID_with_letter[8])
    remainder = number%23
    letters = ['T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X', 'B', 'N', 'J', 'Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K', 'E']
    return letters[remainder] == letter
