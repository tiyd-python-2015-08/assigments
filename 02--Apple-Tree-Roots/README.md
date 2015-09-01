# 02 -- Apple Tree Roots

## Description

Write a program that asks the user for a positive number and then outputs the
approximated square root of the number. Use Newton's method to find the square
root, with epsilon = 0.01. (_Epsilon_ is the allowed error, plus or minus, when
you square your calculated square root and compare it to your original number.)

## Tasks
```markdown
* [ ] Blank slate
  * [ ] Create a GitHub repo called `approximate-square-root`
  * [ ] Put a README.md file in the root of the repository describing what your program will do. (_feel free to start with the description above_)
  * [ ] Make sure you commit your README.md file
* [ ] Round fruit, square roots
  * [ ] Create a blank file called square_root.py and commit it to your repo
  * [ ] Have your program ask the user for a positive number and store it in a variable
  * [ ] Have your program perform Newton's method of successive approximations to approximate the square root of the inputted number
* [ ] Hard mode (optional)
  * [ ] Each time through the loop, print out the number of iterations that have occurred
  * [ ] Show an error message if the user enters any invalid input (negative number or non-numeric string)
* [ ] Nightmare mode (optional)
  * [ ] Allow negative numbers as input and display the result as a complex number
* [ ] Submitting
  * [ ] Make sure you commit and push your changes, and paste a link to the repo as a comment
```

## Objectives

### Learning Objectives

After completing this assignment, you should understand:

* How variables work
* How `while` works
* The concept of successive approximation

### Performance Objectives

After completing this assignment, you should be able to:

* Create a GitHub repository
* Write a Python script
* Ask for input
* Print output

## Details

### Deliverables

* A GitHub repo called approximate-square-root containing at least:
  * This `README.md` file
  * a file called `square_root.py`

### Requirements  

Here is an example of the program running correctly:

```
$ python square_root.py
Enter a positive number: 4
The square root of 4 is 2.0.

$ python square_root.py
Enter a positive number: 20
The square root of 20 is 4.472137791286727.
```

## Normal Mode

Newton's method of successive approximations says that whenever we have a guess
`y` for the value of the square root of a number `x`, we can get a better guess
(one closer to the actual square root) by averaging `y` with `x/y`. If we do
this over and over, we should be able to get a very accurate guess.

You have to write a script that asks the user for a positive number and then
compute the square root with a maximum error of 0.01. You then print out your
answer to the user.

## Hard Mode

In each iteration of your loop, print out the current number of iterations and
the current guess.

Examine the input into your program and give an appropriate error message if
a non-number or negative number is given.

## Nightmare Mode

Look up [complex numbers in Python][]. Allow negative numbers as input into
your program.

## Additional Resources

* Read more about [the Babylonian/Newton's method of approximating square roots](https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Babylonian_method).
* [Numeric types in Python](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex).

## Credit

This assignment is adapted from
[SICP](https://mitpress.mit.edu/sicp/chapter1/node9.html) by Abelson and
Sussman.


[complex numbers in Python]: https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex
