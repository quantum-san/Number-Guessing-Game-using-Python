print("\"Welcome to the number guessing game \"")
print("You will have to guess a number from the riddle which will be mentioned later on in the game")
permission = str(input("Would you like to play the game ? (Yes or No):"))

if permission == "Yes":
    print("Let's start the game")
    print("Riddle:")
    print('''I am a prime number hiding between 35 and 40.
 When my digits are multiplied, the result is 21.
 When they are added, the result is 10.''')
    number = int(input("Who am I ? : "))

    while number != 37:
        number = int(input('''Sorry It's not the number.
        Try Again.
        Enter The number: '''))

    if number == 37:
        print("Bravo !! You guessed the number")

elif permission == "No":
    print("Thank you for taking interest")
else:
    print("Invalid response")

# number = 37


