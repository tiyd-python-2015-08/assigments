# Money Ball

## Description

Put together an all-time best roster of cheap players who had great on base percentages

## Tasks
```markdown
* [ ] Blank slate
  * [ ] Create a GitHub repo called `moneyball`
  * [ ] Copy all the files from this repo into it
  * [ ] Set up your requirements/virtual environment
  * [ ] Create a `data` folder and put the baseball statistics data into it
* [ ] Normal mode
  * [ ] Join together the relevant tables into DataFrame object(s)
  * [ ] Calculate OBP of players and discard outliers
  * [ ] Given a specific year, put together a 9-player roster that maximizes the OBP of the players while minimizing their salary
  * [ ] Ensure that you have a complete roster with players who played at each position and that you aren't planning on using clones of players
* [ ] Hard mode
  * [ ] Adjust player salaries for inflation
  * [ ] Build an all-star moneyball dream team using the adjusted salaries
```

## Objectives

### Learning Objectives

After completing this assignment, you should understand:

* How to use public data for analysis
* How to relate many datasets and perform analysis on the related data
* How to publish your own data analysis as a notebook

### Performance Objectives

After completing this assignment, you should be able to:

* Join / Merge many external datasets
* Perform statistical analysis to solve a problem
* Report your findings in a notebook in a professional manner.

## Details

### Deliverables

* A Git repo called moneyball containing at least:
  * `README.md` file explaining how to run your project
  * a `moneyball.ipynb` file showing your analysis
  * a `requirements.txt` file

### Requirements

* No PEP8 or Pyflakes warnings or errors

## Normal Mode

In the movie / book [Moneyball](http://www.imdb.com/title/tt1210166/) - data analysis
is employed to discover that teams that had a roster containing players with a high
on base percentage (OBP) did very well in the regular season. Using this knowledge
the General Manager was able to create a very successful team on a shoestring budget
with players that had a high OBP.

First get the most recent complete baseball statistics dataset from [Sean Lahman's website](http://www.seanlahman.com/baseball-archive/statistics/). Unzip it into a `data/` directory inside your repository.

With this data downloaded, create an IPython Notebook called `moneyball.ipynb` that
joins together many of the different tables so you are able to find each player's OBP
and their salary.

YOUR JOB is to put together the starting 9 player roster for a single season.  How?
You need to find the players with the highest OBP and the lowest salary in any specific year. Make
sure you are removing outliers (an OBP of 1.0 is not an indicator of a perfect player, more like
they possibly only played 4 or 5 games and had good luck, alternatively an OBP of 0 is pretty
bad).  Your 9 player roster should include:

 - (1st, 2nd, 3rd) Baseman
 - (Left, Center, Right) Fielders
 - Short Stop
 - Pitcher
 - Catcher

A player that historically played multiple positions can not account for 2 places on your roster.

## Hard Mode

In addition to the required objectives outlined above you should adjust each player's salary
for inflation based on the year they earned the salary.

Also you are required to put together an "all time best" legacy team based on their adjusted salary.

#### Note

You will have to calculate the on base percentage for each player.  Here is the formula you
might want to use [On Base Percentage](https://en.wikipedia.org/wiki/On-base_percentage)
