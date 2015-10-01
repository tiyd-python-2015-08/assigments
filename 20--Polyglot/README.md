# Classify code snippets into programming languages

## Description

Create a classifier that can take snippets of code and guesses the programming language of the code.

## Tasks
```markdown
* [ ] Blank slate
  * [ ] Create a GitHub repo called `programming-language-classifier`
  * [ ] Set up your requirements/virtual environment
  * [ ] Copy all the files from this folder into your repo
* [ ] Normal mode
  * [ ] Collect a corpus of programming language snippets to use for training data
  * [ ] Extract features from your corpus for your classifier, either using an existing Transformer or one you've written
    * [ ] **Be sure you can explain at a high-level how your Transfomer works**
  * [ ] Write a classifier function that takes a string of code and returns a guess for the language the code was written in
  * [ ] Test your classifier using the provided test files
    * [ ] **Be sure you do not use the test files as your training data**
  * [ ] Demonstrate the use/results of your classifier in an IPython notebook
* [ ] Hard mode
  * [ ] Create a runnable Python file that takes a command-line argument of a source code file and prints out the guessed programming language
  * [ ] Calculate the probability of various programming languages, and return the top percentages probable
  * [ ] Add command-line flags to make your program more versatile

```

## Objectives

### Learning Objectives

After completing this assignment, you should understand:

* Feature extraction
* Classification
* The varied syntax of programming languages

### Performance Objectives

After completing this assignment, you should be able to:

* Build a robust classifier

## Details

### Deliverables

* A Git repo called programming-language-classifier containing at least:
  * `README.md` file explaining how to run your project
  * a `requirements.txt` file
  * a suite of tests for your project

### Requirements  

* Passing unit tests
* No PEP8 or Pyflakes warnings or errors

## Normal Mode

### Getting a corpus of programming languages

Option 1: Get code from the [Computer Language Benchmarks Game](http://benchmarksgame.alioth.debian.org/). You can [download their code](https://alioth.debian.org/snapshots.php?group_id=100815) directly. In the downloaded archive under `benchmarksgame/bench`, you'll find many directories with short programs in them. Using the file extensions of these files, you should be able to find out what programming language they are.

Option 2: Scrape code from [Rosetta Code](http://rosettacode.org/wiki/Rosetta_Code). You will need to figure out how to scrape HTML and parse it. [BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/) is your best bet for doing that.

Option 3: Get code from GitHub somehow. The specifics of this are left up to you.

You are allowed to use other code samples as well.

**For your sanity, you only have to worry about the following languages:**

* C (.gcc, .c)
* C#
* Common Lisp (.sbcl)
* Clojure
* Haskell
* Java
* JavaScript
* OCaml
* Perl
* PHP (.hack, .php)
* Python
* Ruby (.jruby, .yarv)
* Scala
* Scheme (.racket)

Feel more than free to add others!

### Classifying new snippets

Using your corpus, you should extract features for your classifier. Use whatever classifier engine that works best for you _and that you can explain how it works._

Your initial classifier should be able to take a string containing code and return a guessed language for it. It is recommended you also have a method that returns the snippet's percentage chance for each language in a dict.

### Testing your classifier

The `test/` directory contains code snippets. The file `test.csv` contains a list of the file names in the `test` directory and the language of each snippet. Use this set of snippets to test your classifier. _Do not use the test snippets for training your classifier._

## Hard Mode

In addition to the requirements from **Normal Mode**:

Create a runnable Python file that can classify a snippet in a text file, run like this:

`guess_lang.py code-snippet.txt`

where `guess_lang.py` is whatever you name your program and `code-snippet.txt` is any snippet. Your program should print out the language it thinks the snippet is.

To do this, you will likely want to either pre-parse your corpus and output it as features to load or save out your classifier for later use. Otherwise, you'll have to read your entire corpus every time you run the program. That's acceptable, but slow.

You may want to add some command-line flags to your program. You could allow people to choose the corpus, for example, or to get percentage chances instead of one language. To understand how to write a command-line program with arguments and flags, see the [argparse](https://docs.python.org/3/library/argparse.html) module in the standard library.

## Additional Resources

* [TextBlob](http://textblob.readthedocs.org/en/dev/)
* [Beautiful Soup](http://www.crummy.com/software/BeautifulSoup/)
* [Rosetta Code](http://rosettacode.org/wiki/Rosetta_Code)
* [Working with Text Files](https://opentechschool.github.io/python-data-intro/core/text-files.html)
