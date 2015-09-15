# Chart data

## Description

Chart data about coin flips.

## Tasks

```markdown
* [ ] Blank slate
  * [ ] Create a GitHub repo called `flipping-out`
  * [ ] Put `README.md` and `requirements.txt` files in it
  * [ ] Make sure ipython[all] and any necessary plotting libraries are in `requirements.txt`
  * [ ] Make sure your flipping-out folder has its own virtual environment (`.envrc`), but **do not commit `.envrc` or `.direnv`**
  * [ ] Install the requirements using `pip install -r requirements.txt`
* [ ] Normal mode
  * [ ] Create an IPython Notebook file called `coin-flips.ipynb`
  * [ ] Create a function to flip a coin
  * [ ] Create a function to simulate flipping a coin _n_ times, recording how many heads and tails it has seen at exponential intervals (2<sup>0</sup>, 2<sup>1</sup>, 2<sup>2</sup>..._n_)
    * [ ] Make a line plot of the **difference** between heads and tails at each point
    * [ ] Make a line plot of the **ratio** of heads to tails at each point
    * [ ] Create the above two plots as scatter plots with a logarithmic scale for the x-axis
    * [ ] Write notes about your observations and add other plots as necessary
  * [ ] Create a function that uses your above simulation function, but runs 20 trials where _n_ = 2<sup>16</sup>
    * [ ] Create a scatter plot of the mean heads/tails ratio at each recorded point
    * [ ] Create a scatter plot of the standard deviation of the heads/tails ratio at each recorded point
    * [ ] Use a logarithmic scale for the x-axis with both of the above plots, and a logarithmic scale for the y-axis for the standard deviation plot
  * [ ] Create a function to run 100,000 trials of 100 flips per trial
    * [ ] Plot a histogram of the ratio of heads to total flips for each trial.
    * [ ] Plot a box plot of the same results
  * [ ] Create a function to run 100,000 trials of 1,000 flips per trial
    * [ ] Plot a histogram of the ratio of heads to total flips for each trial.
    * [ ] Plot a box plot of the same results
    * [ ] Compare the 1,000 flips per trial results to the 100 flips per trial results
* [ ] Hard Mode
  * [ ] Use seaborn and clean up your Notebook file for presentation
```

## Objectives

### Learning Objectives

After completing this assignment, you should understand:

* Basic statistics
* The use of different plot types

### Performance Objectives

After completing this assignment, you should be able to:

* Use matplotlib
* Use IPython Notebook
* Use the statistics module

## Details

### Deliverables

* A Git repo called charting containing at least:
  * an IPython notebook
  * a `requirements.txt` file

## Normal Mode

All of the following should be done in an IPython Notebook. You should put necessary imports in the topmost cell(s) of the Notebook, and each task involving code or analysis should be done in its own discrete cell.

Create a function to flip a coin. It is up to you to determine what this returns to signify heads or tails. Then create a function to run a simulation of flipping a coin _n_ number of times, default 2<sup>16</sup>, recording how many heads and tails it has at different intervals. The intervals are exponential, so record at 2<sup>0</sup>, 2<sup>1</sup>, 2<sup>2</sup>, and so on until you reach _n_. Record the final number as well.

Then make a line plot of the difference between heads and tails at each
recorded point, and another with the ratio of heads to tails at each recorded point.

Create these plots again, but as scatter plots with a logarithmic scale for the x-axis.

Write notes about what you observe. Feel free to add more plots to help you.

Now we will look at the mean and standard deviation of these trials of flipping coins. Flip coins as before, but run 20 trials of 2<sup>16</sup> each.

Use a scatter plot to plot the mean heads/tails ratio at each recorded point, and another scatter plot to plot the standard deviation of the heads/tails ratio at each recorded point. You will want to use a logarithmic scale for the x-axis in both. You may want to do the same for the y-axis with the standard deviation.

Write notes about what you observe. Feel free to add more plots to help you.

Lastly, run 100,000 trials of 100 coin flips each. Plot a histogram of the ratio of heads to total flips for each trial. Run 100,000 trials of 1,000 coin flips each and plot that histogram as well. Lastly, plot a box plot of your results from the 100 coin flip trials and your results from the 1,000 coin flip trials.

What do you observe? Write up your notes.

## Hard Mode

Use seaborn and clean up your Notebook file for presentation. Use MarkDown effectively to highlight key observations. (Hint: you can write exponents using the `<sup>` tag, e.g., `2<sup>16</sup>` becomes 2<sup>16</sup>)

Add the mean and standard deviation as text to each applicable histogram.

## Additional Resources

* [matplotlib](http://matplotlib.org/)
* [seaborn](http://stanford.edu/~mwaskom/software/seaborn/)
* [IPython](http://ipython.org/)

## Credit

Some assignments adapted from _Introduction to Computation and Programming Using Python_.
