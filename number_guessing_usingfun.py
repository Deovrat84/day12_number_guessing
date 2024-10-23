import art
import random

Hard_Turns = 6
Medium_Turns = 8
Easy_Turns = 10
Out_of_Range = 0
print(art.logo)
#function to check the answer
def check_answer(user_guess, actual_answer, turns):
    if user_guess > actual_answer:
        print("Too High")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too Low")
        return turns - 1
    else:
        print(f"You have got it. The answer was {actual_answer}")

#setting the difficulty
def set_difficulty():
    level = ["Easy", "Medium", "Hard"]
    select_level = input("Please select the level 'Hard', 'Medium', 'Easy'")
    if select_level == level[0]:
        return Easy_Turns
    elif select_level == level[1]:
        return Medium_Turns
    elif select_level == level[2]:
        return Hard_Turns
    else:
        return Out_of_Range


#function to play the guessing number game.
def game():
    
    print("Welcome to the number guessing GAME between 1-100. COMPUTER has choosen a number which you have to GUESS yeaaaahhhh!!")
    answer = random.randint(1,100)
    guess = 0
    difficulty_level = set_difficulty()
    if difficulty_level > 0:
        while guess != answer:
            print (f"You have {difficulty_level} turns to guess the number")
            guess = int(input("Make a guess: "))
            difficulty_level = check_answer(guess, answer, difficulty_level) #no idea why this difficulty_level = difficulty_level
            if difficulty_level == 0:
                print("You've run out of the turns, You lose.")
                return #return inside a function is useful to break the function without returning anything.
    else:
        print("You choose Wrong Level")

#Calling the game function
game()
