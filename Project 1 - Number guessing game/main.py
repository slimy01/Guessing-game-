import random as r

def ask_for_number():
    random = r.randint(1,50)
    attempts = 0
    list_of_num = []
    while True:
        try:
            guess = input("Please enter your guess (1-50)")

            if not guess.isdigit():
                raise ValueError("Guess must be a digit.")
            
            if not guess:
                raise ValueError("Guess cant be left blank.")
            
            guess = int(guess)

            if guess < 1 or guess > 50:
                raise ValueError("Guess must stay between 1 and 50.")

            list_of_num.append(guess)
            attempts += 1
            
            if guess == random:
                print("Correct")
                print(f"You got it in {len(list_of_num)} guesses.")
                print(f"Your guess: {list_of_num}")
                break
            elif guess > random:
                print("Too High")
            else:
                print("Too Low")
            
            
            if attempts >= 7:
                print("You have used too many attempts.")
                print(f"Here is what you typed {list_of_num}.")
                break 
       

        except ValueError as e:
            print(e)

def main():
    while True:
        ask_for_number()

        play_again = input("Would you like to play agian.").lower()

        if play_again != "yes" and play_again != "y":
            print("Thatnks for playing!")
            break

main()