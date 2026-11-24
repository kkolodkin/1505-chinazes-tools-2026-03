import test
import Game1
import Game2
import Game3
import Game4

def print_menu():
    print(
'''
============================
Menu options

1. Run Test Module
2. Guess the number
3. Cows game
4. Tic Tac Toe
5. 
============================
''')

print("Hello! Welcome to Chinazes Tools!")

while 1:
    print_menu()
    user_choice = input("Select a menu option number: ")
    print()

    if user_choice == '1':
        test.run()
    elif user_choice == '2':
        Game1.run()
    elif user_choice == '3':
        Game2.run()
    elif user_choice == '4':
        Game3.run()
    elif user_choice == '5':
        Game4.run()
    elif user_choice == '6':
        print("Bye!")
        break
    else:
        print("Invalid choice. Try again.")