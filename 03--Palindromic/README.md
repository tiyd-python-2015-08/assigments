# Palindromic

## Description

Write a program that asks the user for one or more sentences and then lets the user know if it is a palindrome.

## Tasks

```markdown
* [ ] Blank slate
  * [ ] Create a GitHub repo called `palindromic`
  * [ ] Put a `README.md` file in it and copy palindrome.py and palindrome_test.py from this repository into it.
* [ ] Normal Mode
  * [ ] Write your `main()` function to ask the user for a word/sentence, pass it into the is_palindrome function, and state whether or not the the sentence is palindromic
  * [ ] Write your `is_palindrome` function **using recursion**
  * [ ] Run palindrome_test.py and ensure you pass all the tests
* [ ] Hard Mode (optional)
  * [ ] Make an iterative version of your `is_palindrome` function (using loops instead of recursion), and ensure it passes the tests too
```

## Objectives

### Learning Objectives

After completing this assignment, you should understand:

* Manipulating strings
* How strings are related to lists
* Recursion

### Performance Objectives

After completing this assignment, you should be able to:

* Strip characters out of strings
* Change the case of strings
* Look at substrings

## Details

### Deliverables

* A GitHub repo called palindrome containing at least:
  * This `README.md` file
  * a file called `palindrome.py`

### Requirements  

* Your program must pass my tests in `palindrome_test.py`. You should be able to run this with `python palindrome_test.py`.
* You need a function called `is_palindrome` that takes a string and returns a boolean (`True` or `False`). Your program should use this function.

## Normal Mode

You have to write a program that, when run, asks the user to input some text. It can be a phrase, a sentence, or multiple sentences. After it is entered, your program will let the user know if it is a palindrome or not. Use "is a palindrome" and "is not a palindrome" in your output in order for the tests to pass.

Letter casing and punctuation do not matter when testing a palindrome. All of the following are valid palindromes:

* stunt nuts
* Lisa Bonet ate no basil.
* A man, a plan, a cat, a ham, a yak, a yam, a hat, a canal: Panama!
* Doc, note, I dissent. A fast never prevents a fatness. I diet on cod.

## Hard Mode

Make both an iterative and recursive version of your palindrome test function.

## Notes

You may want to use the `re.sub` function to strip out punctuation and spaces. A regular expression you can use to match all space and punctuation is `r'[^A-Za-z]'`.

## Additional Resources

* [Palindrome list](http://www.palindromelist.net/).
* [String type in Python](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str).
* [Regular expression operations](https://docs.python.org/3/library/re.html).
