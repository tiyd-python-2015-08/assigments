# 04 -- Frequency Filer

## Description

Write a program that looks for a file called `sample.txt`. This file will contain the text of a book, part of a book, or speech in plain text format. It reads this file and then returns the top 20 words used in the text and the number of times they are used.

## Tasks
```markdown
* [ ] Blank slate
  * [ ] Create a GitHub repo called `frequency-filer`
  * [ ] Put a `README.md` file in it and copy word_frequency.py, word_frequency_test.py, and sample.txt from this repository into it.
* [ ] Normal Mode
  * [ ] Open `sample.txt` and read in the text
  * [ ] Count the number of times each word is used, regardless of capitalization
  * [ ] Find the top 20 words used and output them and their frequency to stdout
  * [ ] Run word_frequency_test.py and ensure you pass all the tests
* [ ] Hard Mode (optional)
  * [ ] Add a list of ignored words and don't count these in the word frequencies
  * [ ] Make your program take the name of the file to read on the command line, so it doesn't just have to work with `sample.txt`.
* [ ] Nightmare Mode (optional)
  * [ ] Output the top 20 words' frequencies using a simple text-based histogram
  * [ ] Normalize the histogram so there are never more than 50 `#` marks.

```

## Objectives

### Learning Objectives

After completing this assignment, you should understand:

* Reducing a collection into another form

### Performance Objectives

After completing this assignment, you should be able to:

* Open and read files
* Create a dictionary
* Sort a list

## Details

### Requirements  

* Your program must pass my tests in `word_frequency_test.py`. You should be able to run this with `python word_frequency_test.py`.
* You need a function called `word_frequency` that takes a string and returns a dictionary of all the words used in the string and the number of times they were used.

## Normal Mode

Your program should open `sample.txt` and read in the entirety of its text.
You'll need to normalize the text so that words in different cases are still
the same word and so it's scrubbed of punctuation. Once you've done that, go
through the text and find the number of times each word is used.

After that, find the top 20 words used and output them to the console in
reverse order, along with their frequency, like this:

```
peanut 33
racket 31
and 29
common 21
religion 15
fate 14
algorithm 10
the 9
...
```

## Hard Mode

In addition to the requirements from **Normal Mode**:

1. Add a list of ignored words to your program and do not count those words in the word
frequencies. A suggested list:

```
a,able,about,across,after,all,almost,also,am,among,an,and,any,are,as,at,be,
because,been,but,by,can,cannot,could,dear,did,do,does,either,else,ever,every,
for,from,get,got,had,has,have,he,her,hers,him,his,how,however,i,if,in,into,is,
it,its,just,least,let,like,likely,may,me,might,most,must,my,neither,no,nor,
not,of,off,often,on,only,or,other,our,own,rather,said,say,says,she,should,
since,so,some,than,that,the,their,them,then,there,these,they,this,tis,to,too,
twas,us,wants,was,we,were,what,when,where,which,while,who,whom,why,will,with,
would,yet,you,your
```

2. Change your program so that you have to give it the name of the file to read
on the command line, like so: `python word_frequency.py sample.txt`.

## Nightmare Mode

3. Output the words to the console in a simple text-based histogram format,
like so:

```
peanut    #################################
racket    ###############################
and       #############################
common    #####################
religion  ###############
fate      ##############
algorithm ##########
the       #########
...
```

4. Normalize the histogram so that you never have more than 50 `#` marks.
You'll have to scale all the lines by some divisor if you have more than 50 of
one word. It is ok to round down decimals with this. For example, if you have
the word "the" 75 times and the word "and" 47 times, you'd have 50 `#` for
"the" and 31 `#` for "and".

## Additional Resources

* [Project Gutenberg](https://www.gutenberg.org/) - good source of free texts.
* [String type in Python](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str).
* [Regular expression operations](https://docs.python.org/3/library/re.html).
