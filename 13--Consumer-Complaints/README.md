# Analyze Consumer Complaint Data

## Description

Use pandas to read and analyze data from the [CFPB Consumer Complaint
Database](http://www.consumerfinance.gov/complaintdatabase/). This database is
a collection of all complaints made by American consumers to the Consumer
Financial Protection Bureau.

## Tasks
```markdown
* [ ] Blank slate
  * [ ] Create a GitHub repo called `consumer-complaints`
  * [ ] Put `README.md` and `requirements.txt` files in it
  * [ ] Make sure any necessary libraries are in `requirements.txt`
  * [ ] Make sure your `consumer-complaints` folder has its own virtual environment (`.envrc`), but **do not commit `.envrc` or `.direnv`**
  * [ ] Install the requirements using `pip install -r requirements.txt`
* [ ] Normal mode
  * [ ] Read in the data file
  * [ ] Calculate and chart:
    * [ ] Number of complaints by product
    * [ ] Number of complaints by company (top 10)
    * [ ] Number of complaints by company response
    * [ ] Mean number of complaints by day of the week
    * [ ] Any other insights you find interesting
  * [ ] Summary text for each chart
* [ ] Hard mode
  * [ ] Combine the complaints data with the population of each state and chart the frequency of complaints by state per capita
  * [ ] Find statistically significant outliers of # of complaints by ZIP code and try to find a possible reason for the outliers
* [ ] Nightmare mode
  * [ ] Make an infographic of a map of the US, showing the frequency of complaints per capita using shading of each state, with lighter colors representing low frequency and darker colors representing high frequency
```


## Objectives

### Learning Objectives

After completing this assignment, you should understand:

* the joy and power of Pandas

### Performance Objectives

After completing this assignment, you should be able to:

* read in CSV files using Pandas
* pull out and summarize data
* turn Pandas data frames into charts

## Details

### Deliverables

* A Git repo called consumer-complaints containing at least:
  * `README.md` file explaining how to run your project
  * a `requirements.txt` file
  * an IPython notebook and/or a Python package called consumer-complaints

### Requirements

* No PEP8 or Pyflakes warnings or errors

## Normal Mode

Use Pandas to read in the included file, `complaints_dec_2014.csv`.

Calculate and chart:

* Number of complaints by product
* Number of complaints by company (top 10 companies only)
* Number of complaints by company response
* Mean number of complaints by day of week
* Any other insights you find interesting

Write up a summary of what you found from each chart you made.

## Hard Mode

In addition to the requirements from **Normal Mode**:

* Combine the complaints data with US population by state data (find this
  yourself) and then chart the frequency of complaints by state per capita.
* Find statistically significant outliers of complaints by ZIP code. Look these
  up to see if there's a possible reason (military bases are often surrounded
  by predatory lending companies, for example.)

## Nightmare Mode

In addition to the requirements from **Hard Mode**:

* Take the frequency of complaints by state per capita and then make a chart
  of the US, with frequency of complaints matched to a scale of lighter color
  (low frequency) to darker color (high frequency), with a legend.

## Additional Resources

* [CFPB Consumer Complaint Database data and visualizations](http://www.consumerfinance.gov/complaintdatabase/)

## Credit

The [Consumer Financial Protection Bureau](http://www.consumerfinance.gov/) is
pretty great! Thanks for making your data public.
