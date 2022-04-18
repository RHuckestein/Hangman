from words import word_list
import random
guessed_words = []
def get_word():
    word = random.choice(word_list)
    return word.upper()

def user_menu():
    print(
        """
        Welcome To Hangman!!! 
        
        Rules: To play a game, a random word will be selected, and you have to enter a letter to see if it exist in the chosen word.
        If the letter exist, the letter will show up in the blank spaces of the word to be guessed.
        You can miss a maximum of 6 letters or you loose the game!
        If you guess the word without 6 incorrect guesses, you win!!
        
        Would you like to play a game?
        
        ********
        1. Yes *
        ********
        2. No  *
        ********
        """)

def play_hangman(word):
    finish_game = False
    tries = 6
    word_status = "_" * len(word)
    guessed_letters = []       
              
    while not finish_game:
        if guessed_letters:
            print("The letters you have guessed so far are:", guessed_letters)
            print(show_hangman(tries))
            print("___________________________________________________")
            print("\nYou have", tries, "turns remaining!")
        print("\nGuess the word:", word_status)
        letter_choice = input("\nPlease select a letter from A to Z:").upper()
        if len(letter_choice) == 1 and letter_choice.isalpha():
            if letter_choice in guessed_letters:
                print("\nYou already guessed the letter", letter_choice)
            elif(letter_choice not in word):
                print(letter_choice, "is not in the word!")
                tries -= 1                    
                guessed_letters.append(letter_choice)
                if tries == 0:
                    print("\nNice try, but you are out of turns! Better luck next time!")
                    print("The word was", word)
                    finish_game = True
            else:           
                print("\nYay! You guessed a correct letter!", letter_choice, "is in the word!")
                guessed_letters.append(letter_choice)
                word_as_list = list(word_status)
                for i in range(len(word)):
                    if word[i] == letter_choice:
                        word_as_list[i] = letter_choice
                        word_status = "".join(word_as_list)
                if "_" not in word_status:
                    print("\nYou Won!!")
                    guessed_words.append(word_status)
                    finish_game = True
    return guessed_words
                        
        
def show_hangman(tries):
    hangman_guesses = [ """
                             --------
                            |       |
                            |       O
                            |      \|/
                            |       |
                            |      / \
                            |
                           ___
                        """, 
                        """
                             --------
                            |       |
                            |       O
                            |      \|/
                            |       |
                            |      / 
                            |
                           ___
                        """,
                        """
                             --------
                            |       |
                            |       O
                            |      \|/
                            |       |
                            |      
                            |
                           ___
                        """,
                        """
                             --------
                            |       |
                            |       O
                            |      \|
                            |       |
                            |      
                            |
                           ___
                        """,
                        """
                             --------
                            |       |
                            |       O
                            |       |
                            |       |
                            |      
                            |
                           ___
                        """,
                        """
                             --------
                            |       |
                            |       O
                            |      
                            |       
                            |      
                            |
                           ___
                        """,
                        """
                             --------
                            |       |
                            |       
                            |      
                            |       
                            |     
                            |
                           ___
                        """
                        ]
    return hangman_guesses[tries]

def main():
        word = get_word()
        word_size = len(word)
        count = 1
        user_menu()
        while True:
            play_game = input("Please enter 1 or 2:")
            if play_game == "1" or play_game.lower() == "yes":
                print("\nAwesome! Lets Play!\n")
                print(f"Here is your first word! This word has {word_size} letters!\n")
                play_hangman(word)
                print(", ".join(guessed_words))
                break          
            if play_game == "2" or play_game.lower() == "no":
                print("OK! See you next time!")
                return False  
        while input("Play Again? Enter Yes or No").upper() == "YES" or "Y":
            count += 1
            print("This is game number:", count)
            word = get_word()
            play_hangman(word)
            print(", ".join(guessed_words))
                      
main()
            
                            