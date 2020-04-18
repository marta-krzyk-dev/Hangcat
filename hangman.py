import os
from termcolor import colored  # requires to run  "pip install termcolor" in terminal before starting this program
from random import choice
import converters


def readWordsFromFile(filename):
    words = []
    with open(filename, 'r') as file:
        for line in file:
            for word in line.split():
                words.append(word.strip())
    return words


class Hangcat:

    def __init__(self):
        self.mode = 2
        self.word = ""
        self.guessed_letters = set()
        self.words = readWordsFromFile("word_bank.txt")
        self.guessBoard = []
        self.wordBoard = []

        self.drawing = [
            """ 
  ||             _
  ||             \`\\
  ||   /./././.   | |
  || /        `/. | |
  ||/     __    `/'/'
 /\|_/\ /'  `\    /
|  oo  |      `.,.|
 \\vvvv/        ||||
   ||||        ||||
   ||||        ||||
   `'`'        `'`'""",

            """ 
                 _
                 \`\\
       /./././.   | |
     /        `/. | |
    /     __    `/'/'
 /\__/\ /'  `\    /
|  oo  |      `.,.|
 \\vvvv/        ||||
   ||||        ||||
   ||||        ||||
   `'`'        `'`'""",
            """ 
                 _
                 \`\\
       /./././.   | |
     /        `/. | |
    /     __    `/'/'
 /\__/\ /'  `\    /
|  oo  |      `.,.|
 \\vvvv/        ||
   ||||        ||
   ||||        ||
   `'`'        `'""",
            """ 
                 _
                 \`\\
       /./././.   | |
     /        `/. | |
    /     __    `/'/'
 /\__/\ /'  `\    /
|  oo  |      `.,.|
 \\vvvv/       
   ||||        
   ||||        
   `'`'        """,
            """ 
                 _
                 \`\\
       /./././.   | |
     /        `/. | |
    /     __    `/'/'
 /\__/\ /'  `\    /
|  oo  |      `.,.|
 \\vvvv/       
   ||       
   ||        
   `'       """,
            """ 
                 _
                 \`\\
       /./././.   | |
     /        `/. | |
    /     __    `/'/'
 /\__/\ /'  `\    /
|  oo  |      `.,.|
 \\vvvv/        
  

                    """,
            """ 
                
                 
       /./././.   
     /        `/. 
    /     __    `
 /\__/\ /'  `\    /
|  oo  |      `.,.|
 \\vvvv/        
          
   
                   """,
            """ 
                
                 
         
          
      
 /\__/\ 
|  oo  |      
 \\vvvv/        
          
   
                   """,
            """ 
                
                 
         
          
      

   oo        
  vvvv        
          
   
                   """,
            """ 
                
                 
         
          
      

   oo        
    
          
   
                   """,
            "\n" * 11  # Blank drawing
        ]

        self.max_chances = len(self.drawing) - 1
        self.chances = self.max_chances

    def Draw(self):
        index = self.chances
        if len(self.drawing) > index > -1:
            print(colored(self.drawing[index], "green", attrs=["bold"]))
        else:
            print(self.drawing[0])

    def ChooseMode(self):
        print(colored("*** HANGCAT - the GAME ***", "grey", "on_cyan", attrs=["underline", "bold", "blink"]))
        while True:
            answer = input("""1) 1 Player
2) 2 Players\nq) Quit the game\nChoose option >>> """)

            mode = converters.tryConvertToInt(answer)

            if mode == 1 or mode == 2:
                self.mode = mode
                return mode
            if len(answer) > 0 and answer[0].lower() == "q":
                return "q"
            else:
                self.ClearScreen()
                print("Incorrect option. Try again.")

    def Play(self):
        option = self.ChooseMode()
        if option == 1:
            self.PlayMode1()
        elif option == 2:
            self.PlayMode2()
        else:
            return False

    def PlayMode1(self):
        # self.ClearScreen()
        word = choice(self.words).upper()  # Pick up a random word from dictionary
        self.InitializeBoards(word)

        self.Guess()

    def InitializeBoards(self, word_to_guess):
        self.word = word_to_guess.upper()
        self.guessBoard = ['_'] * len(self.word)
        self.wordBoard = list(self.word)

    def PlayMode2(self):
        while True:
            word = input(colored("Player 1 choose a word >>> ", "grey", "on_yellow", attrs=["bold"])).upper().strip()
            if word.isalpha():
                break
            else:
                print(colored("Word must contain only letters.", "red", attrs=["bold"]))

        self.InitializeBoards(word)

        self.ClearScreen()
        self.Guess()

    def ClearScreen(self):
        os.system('cls')  # on Windows System

    def DrawGuessBoard(self):
        print("  ".join(self.guessBoard))

    def ShowGuessWord(self):
        print("  ".join(self.wordBoard))

    def Guess(self):

        message = ""

        while self.chances > 0:

            self.ClearScreen()

            print(colored(message, "magenta", "on_yellow", attrs=["bold"]))

            self.Draw()
            self.DrawGuessBoard()
            self.printChances()

            if "_" in self.guessBoard:
                letter = self.GetLetter()

                indexes = [i for i, x in enumerate(self.wordBoard) if x == letter]
                if len(indexes) > 0:
                    for index in indexes:
                        self.guessBoard[index] = letter.upper()
                        message = "WAY TO GO!"
                else:
                    message = "NO LUCK THIS TIME!"
                    self.chances -= 1

            if "_" not in self.guessBoard:
                break

        self.ShowEndScreen(self.chances > 0)

    def ShowEndScreen(self, won):
        self.ClearScreen()
        self.Draw()
        self.ShowGuessWord()
        self.printChances()
        if won:
            print(colored("YOU WON =D", "magenta", "on_yellow", attrs=["bold"]))
        else:
            print(colored("YOU LOST :(", "red", attrs=["bold", "reverse"]))

    def printChances(self):
        print(colored(f"{self.chances}/{self.max_chances} chances left!", "magenta", attrs=["bold"]))

    def GetLetter(self):
        while True:
            letter = input("Guess a letter >>> ").upper()

            if len(letter) > 0:
                letter = letter[0]

            if letter.isalpha():
                if letter not in self.guessed_letters:
                    self.guessed_letters.add(letter)
                    return letter
                else:
                    print(f"You have already asked for {letter} before. Try another one")
            else:
                print("It's not a letter. Try again.")


# Main program
while True:
    game = Hangcat()
    game.ClearScreen()

    if not game.Play():
        break
    else:
        input(colored("Click ENTER to go back to the menu", "green", attrs=["bold"]))
