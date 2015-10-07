# MovieLens Online

## Description

Create an interface in Django to the [MovieLens dataset][movielens].

## Tasks
```markdown
* [ ] Night 1
  * [ ] Miscellaneous
    * [ ] Make commits after every significant change
    * [ ] Use feature branches whenever you add something to a stable product
    * [ ] Use requirements.txt and Django best practices for laying out your project
  * [ ] Normal mode
    * [ ] Create a Django project called movieratings
    * [ ] Create a Django app inside your project
    * [ ] Create models for users (raters), movies, and ratings
    * [ ] Create Django admin pages for the models
  * [ ] Hard mode
    * [ ] Add methods to your models
    * [ ] Test your methods
* [ ] Night 2
  * [ ] Normal mode
    * [ ] Create fixtures from your MovieLens dataset
    * [ ] Top 20 movies view
    * [ ] Movie detail view
    * [ ] Rater detail view
  * [ ] Hard mode
    * [ ] Work on a recommendation algorithm, runnable via the shell
```


## Objectives

After completing this assignment, you should be able to...

### Night 1

* Create a new Django application
* Translate real-world data to Django models
* Explain what a database is
* Explain what a model is
* Use the Django admin
* Structure the Django admin to reflect your data

## Deliverables

* A Git repo called django-movies containing at least:
  * a `requirements.txt` file
  * a `README.md` file
  * a Django project called `movieratings`

## Night 1

### Normal Mode

Choose a dataset from the [MovieLens dataset options][movielens] and read its
README.

Create a new Django application in the `movieratings` project to hold your
models.

Create Django models for users (call the model `Rater` so as not to
confuse it with Django users), movies, and ratings. Make sure that your models
can contain the data from your dataset.

Create Django admin pages for your models.

[movielens]: http://grouplens.org/datasets/movielens/

### Hard Mode

Start adding methods to your models that you will need later. For `movie`,
you'll want the average rating for each movie, and the ability to get the
top movies by rating.

For `rater`, you'll want the average rating that rater gave to a movie, and
the ability to get the top movies that rater has not seen. You will also want
to be able to find the Euclidean distance between that rater and another using
their movie ratings. (See [our command-line version of this](https://github.com/tiyd-python-2015-05/movie-recommendations)
to see more.)

In order to do this, you'll want to [read up on the model layer of Django](https://docs.djangoproject.com/en/1.8/#the-model-layer).

Try to test these new methods. Read [Testing in Django](https://docs.djangoproject.com/en/1.8/topics/testing/)
and then either look at [django-nose](https://pypi.python.org/pypi/django-nose) or [pytest-django](https://pytest-django.readthedocs.org/en/latest/).

## Night 2

### Normal Mode

Write function(s) that will create fixtures from your dataset. Load in your fixture data. _DO NOT COMMIT THE FIXTURES!!!_

In your Django application, create views and templates for:

* The top 20 movies rated. This list of movies should have their average rating, and each movie listed should have a link to its individual page.
* Each individual movie. This page should have the movie, its average rating, and each person who rated it. The list of people should have the rating with each person and should have a link to that person's page.
* Each individual user (rater). This page should have their demographic data, and a list of all movies they've rated, with the rating they gave it. Each movie listed should have the rating they gave it beside it and should have a link to that movie's page.

### Hard Mode

Try to build a recommendation algorithm inside your Django project, using the data from the database. Don't worry about incorporating it into a view yet - just test it out using the shell. We will be putting it into our Django project at some point.
