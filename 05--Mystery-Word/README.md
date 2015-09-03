# Mystery Word

## Description

Implement the game of Mystery Word.

## Tasks
```markdown
* [ ] Blank slate
  * [ ] Create a GitHub repo called `mystery-word`
  * [ ] Put a `README.md` file in it and copy mystery_word.py and mystery_word_test.py from this repository into it.
* [ ] Normal Mode
  * [ ] Load words from `/usr/share/dict/words`
  * [ ] Write functions to select a subset of the complete word list
  * [ ] Write a function to select a word at random from the word list
  * [ ] Write a function to display a word with blanks/letters filled in the appropriate spots
  * [ ] Write a function to check if a word has been completely guessed
  * [ ] Write other helper functions as necessary to help with the flow of the game
  * [ ] Run mystery_word_test.py and ensure you pass all the tests
* [ ] Hard Mode (optional)
  * [ ] Implement the evil version of the game and put it in evil_mystery_word.py
  * [ ] Write tests and put them in evil_mystery_word_tests.py

```

## Objectives

### Learning Objectives

After completing this assignment, you should understand:

* All the basics of Python!

### Performance Objectives

After completing this assignment, you should be able to:

* Create an interactive program.
* Read from a file.
* Choose a random value.
* Keep track of state.
* Test your code.

## Details

### Deliverables

* A Git repo called mystery-word containing at least:
  * a `README.md` file explaining how to run your project
  * your main program and functions in mystery_word.py
  * a suite of tests for your project in mystery_word_test.py

### Requirements  

* Passing unit tests

## Normal Mode

You will implement the game Mystery Word. In your game, you will be playing
against the computer.

The computer must select a word at random from the list of words in the file
`/usr/share/dict/words`. This file exists on your computer already.

The game must be interactive; the flow of the game should go as follows:

1. Let the user choose a level of difficulty at the beginning of the program.
Easy mode only has words of 4-6 characters; normal mode only has words of 6-8
characters; hard mode only has words of 8+ characters.
1. At the start of the game, let the user know how many letters the computer's
word contains.
1. Ask the user to supply one guess (i.e. letter) per round. This letter can be
upper or lower case and it should not matter. If a user enters more than one
letter, tell them the input is invalid and let them try again.
1. Let the user know if their guess appears in the computer's word.
1. Display the partially guessed word, as well as letters that have not been
guessed. For example, if the word is BOMBARD and the letters guessed are a, b,
and d, the screen should display:

```
B _ _ B A _ D
```

A user is allowed 8 guesses. Remind the user of how many guesses they have left
after each round.

*A user loses a guess only when they guess incorrectly.* If they guess a letter
that is in the computer's word, they do not lose a guess.

If the user guesses the same letter twice, do not take away a guess. Instead,
print a message letting them know they've already guessed that letter and ask
them to try again.

The game should end when the user constructs the full word or runs out of
guesses. If the player runs out of guesses, reveal the word to the user when
the game ends.

When a game ends, ask the user if they want to play again. The game begins
again if they reply positively.

## Hard Mode

Implement the [evil version of this game](http://nifty.stanford.edu/2011/schwarz-evil-hangman/).
Put it in a new Python program called "evil_mystery_word.py".

You should write tests for new functionality you introduce.

## Notes

When testing, keep in mind that testing user input and output is hard. Testing
functions that have no side-effects -- that is, they take some arguments and
return a value without getting information from `input()` or using `random` --
is much easier. Try to keep all your logic in _pure functions_ and then have an
outer crust of functions that talk to the user or read from files surrounding
your delicious pure function middle. If you are able to do this, you will not
need to test that outer crust.

## Additional Resources

* [nose](https://nose.readthedocs.org/en/latest/).
* [Working with Text Files](https://opentechschool.github.io/python-data-intro/core/text-files.html)

## Credit

This lab is based off a similar exercise in MIT's 6.00.1x course.
