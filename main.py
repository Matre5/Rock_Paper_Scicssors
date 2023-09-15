import random
import time

print("Lets play Rock-paper-scissors,you'll be playing against the computer in this game")
print("R for Rock \nP for Paper \nS for Scissors\n")
print('The rules are:')
print("Rock beats scissors\nPaper beats rock \nScissors beat paper ")
user_choice = "Play or quit: "
options = ['R', 'P', 'S']
computer_choice = random.choice(options)

name = input("What is your name: ").title()
question = input("Do you want to give your computer a name? Y or N: ").upper()

comp_score = 0
user_score = 0

comp_name = ""
if question == 'Y' or question == "Yes":
    comp_name = input(">>> ")
else:
    comp_name = "Computer"

print('Loading game')
for i in range(20):
    print('.', end=' ')
    time.sleep(.5)


while True:
    user_response = input(user_choice).lower().title()
    match user_response:
        case 'Play':
            play = input('Enter a choice, R, P or S: ').upper()
            if (play == 'R' and computer_choice == 'R'):
                print("A tie")
                print(f'{name} chose {play}  {comp_name} chose {computer_choice}')
                print(f'{name} score = {user_score}  {comp_name} score = {comp_score}')
            elif (play == 'R' and computer_choice == 'P'):
                print(f"{comp_score} wins this round")
                print(f'{name} chose {play}  {comp_name} chose {computer_choice}')
                comp_score += 1
                print(f'{name} score = {user_score}  {comp_name} score = {comp_score}')
            elif (play == 'R' and computer_choice == 'S'):
                print(f'{name} wins this round')
                print(f'{name} chose {play}  {comp_name} chose {computer_choice}')
                user_score += 1
                print(f'{name} score = {user_score}  {comp_name} score = {comp_score}')
            elif play == 'P' and computer_choice == 'S':
                print(f"{comp_name} wins this round")
                print(f'{name} chose {play}  {comp_name} chose {computer_choice}')
                comp_score += 1
                print(f'{name} score = {user_score}  {comp_name} score = {comp_score}')
            elif play == 'P' and computer_choice == 'R':
                print(f'{name} wins this round')
                print(f'{name} chose {play}  {comp_name} chose {computer_choice}')
                user_score += 1
                print(f'{name} score = {user_score}  {comp_name} score = {comp_score}')
            elif play == 'P' and computer_choice == 'P':
                print("A tie")
                print(f'{name} chose {play}  {comp_name} chose {computer_choice}')
                print(f'{name} score = {user_score}  {comp_name} score = {comp_score}')
            elif play == 'S' and computer_choice == 'S':
                print("A tie")
                print(f'{name} chose {play}  {comp_name} chose {computer_choice}')
                print(f'{name} score = {user_score}  {comp_name} score = {comp_score}')
            elif play == 'S' and computer_choice == 'R':
                print(f"{comp_name} wins this round")
                print(f'{name} chose {play}  {comp_name} chose {computer_choice}')
                comp_score += 1
                print(f'{name} score = {user_score}  {comp_name} score = {comp_score}')
            elif play == 'S' and computer_choice == 'P':
                print(f'{name} wins this round')
                print(f'{name} chose {play}  {comp_name} chose {computer_choice}')
                user_score += 1
                print(f'{name} score = {user_score}  {comp_name} score = {comp_score}')
            else:
                print("Invalid inputs...try again")

        case "Quit":
            print(f'{name} score = {user_score}  {comp_name} score = {comp_score}')
            if user_score > comp_score:
                print(f'\n{name} wins the game')
            elif user_score < comp_score:
                print(f"\n{comp_name} wins the game")
            else:
                print(f'\nIt is a tie between {name} and the {comp_name}')

            break

        case _:
            print(f"Invalid input {name}... play or quit")


