import random
rock = '''
    ________
    (________)
    (_________)
    (___________)
    (_____________)
    (--------------)
    '''

paper = '''
    _____________
    _____________
    _____________
    _____________
    (************)
    '''

scissors ='''
            _____
        ____________
    ____________________
    _____________________
    (##############)
    '''

Game_images = [rock,paper,scissors]
user_choice = int(input("Enter Your Choice : 0 for rock,1 for paper,2 for scissors :"))

if user_choice >= 3 or user_choice < 0:
    print("You Enterd Invalid Number,You Lose.")

else:
    print(Game_images[user_choice])
    computer_choice = random.randint(0,2)

print("Computer chose:")
print(Game_images[computer_choice])

if computer_choice == user_choice:
    print("It's a draw")

elif computer_choice == 0 and user_choice == 2:
    print("You Loose")

elif user_choice == 0 and computer_choice == 2:
    print("You Win")

elif computer_choice > user_choice:
    print("You Loose")

elif computer_choice < user_choice:
    print("You Win")