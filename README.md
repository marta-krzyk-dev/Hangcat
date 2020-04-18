# Hangcat
The console game **entirely in Python.** Guess the word in 1-player and 2-player mode.
In 1-player mode computer choose the word for you to guess.
In 2-player mode one of the players chooses word for the other.

### Features
- [x] The game logic is encapsulated in Hangcat class
- [x] Guess words for 1-player mode are read from a text file
- [x] A picture of a cat is being drawn after loosing a chance
- [x] Player has 10 chances to guess
- [x] Player can't enter the same letter again, they will be prompted to choose another letter
- [x] Player can't enter non-letter as a guess
- [x] If guess is more than 1 character long, first letter is taken as a guess

![Hangcat](https://github.com/marta-krzyk-dev/Hangcat/blob/master/hangcat.jpg?raw=true=300x300)

## Install
Run
```
pip install termcolor
```
in terminal (cmd) to install termcolor library be able run the script. :shipit:

You might also need to run
```
pip install converters
```
## Run
Make sure Python is installed on the machine. 
In terminal (cmd) run:
```
python hangcat.py
```
