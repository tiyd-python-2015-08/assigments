# Classifying spam

## Description

Use the Spambase dataset to classify spam. This data is already parsed down from email to features.

## Tasks
```markdown
* [ ] Blank slate
  * [ ] Create a GitHub repo called `spambase`
  * [ ] Set up your requirements/virtual environment
  * [ ] Download the spambase dataset, but do not commit it to your repository
  * [ ] Create an IPython notebook to write your code and collect your findings
* [ ] Normal mode
  * [ ] Load in the data file, doing any cleaning necessary to get usable data
  * [ ] Subsample the data set into training and test data
  * [ ] Write code to classify the data into spam/not-spam, making sure that you just use your training data to build your model, and checking your results with your test data
* [ ] Hard mode
  * [ ] Try reducing or changing your features in order to get better results
  * [ ] Find another dataset and break it down into features
  * [ ] Test your algorthm on the new dataset and compare its performance

```

## Objectives

### Learning Objectives

After completing this assignment, you should understand:

* Simple Bayesian analysis
* The importance of separating training and test data

### Performance Objectives

After completing this assignment, you should be able to:

* Create a Bayesian classifier
* Train your classifier
* Test your classifier

## Details

### Deliverables

* A Git repo called spambase containing at least:
  * `README.md` file explaining how to run your project
  * a `requirements.txt` file

### Requirements  

* No PEP8 or Pyflakes warnings or errors

## Normal Mode

Go to the UCI Machine Learning repository and [download the Spambase dataset](https://archive.ics.uci.edu/ml/datasets/Spambase). Make sure you [read the documentation for the data](https://archive.ics.uci.edu/ml/machine-learning-databases/spambase/spambase.DOCUMENTATION). This explains what the attributes are in the data file.

Subsample the data set so 60% is training data and 40% is test data. You can subsample however you like, including splitting the original file. Just make sure that you have a representative data set. (The original is about 60% not-spam and 40% spam.)

Then write code to classify the data into spam and not-spam, training with your training data and testing on your test data.

## Hard Mode

In addition to the normal mode requirements, try reducing or changing your features in order to get better results.

Find another source of spam/not-spam data, break it down into features, and perform the same exercise as above. How well does your algorithm perform on the new data?
