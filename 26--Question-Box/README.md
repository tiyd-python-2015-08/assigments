# Question Box

## Description

Build a Stack-Overflow type app using Django and deploy it to Heroku.

## Tasks
```markdown
* Yak shaving
  * [ ] Create a GitHub organization for your team to use
* Normal mode
  * [ ] Plan your models together
  * [ ] Plan for incremental feature build-out
  * [ ] Plan for the division of work among your team-members
  * [ ] Create models, views, and templates for each feature in feature branches, and merge them into master as features are completed
  * [ ] Deploy to Heroku after every merge into master - don't put this off to the last minute!
* Hard mode
  * [ ] Accepted answer
  * [ ] Question editing
  * [ ] API
* Nightmare mode
  * [ ] Votes and comments for questions
  * [ ] Track and display events per user
  * [ ] Look for inefficient queries and optimize them
```

## Objectives

This assignment is meant to test your whole knowledge of Django as a tool to build web applications. In addition, it is a test of working in a team, much like you will be for the final project.

### Deliverables

* A Git repo called question-box containing at least:
  * `README.md` file explaining how to run your project
  * a `requirements.txt` file
  * a Django project
* A link to a deployed instance of your project on Heroku. Put the URL where it is deployed in your pull request.

### Requirements  

* No PEP8 or Pyflakes warnings or errors

## Normal Mode

Build a Django app used to ask questions and accept good answers. The
functionality of this is much like Stack Overflow.

Logged-in users should be able to:

* Ask questions
* Answer questions
* Vote on answers positively or negatively

Questions should have:

* a title
* question text
* any number of tags (tags being short phrases that show the topics of the question)
* any number of answers

Answers should have:

* the answer text
* a score based on the sum of all votes

Besides the normal things users have, they should also have a score. The score
starts at 0, and increases in the following ways:

* When a user asks a question, +5 points.
* When a user's answer is upvoted, +10 points per positive vote.
* When a user's answer is downvoted, -5 points per negative vote.
* When a user downvotes an answer, -1 point (yes, it costs from your score to vote something down).

Each user should have their own profile page that shows their score and other
info.

## Hard Mode

In addition to the above:

Questions can have:

* An accepted answer. The question's author can accept one and only one answer
given. The author of the answer gets +100 points.

Answers can have:

* Any number of comments about the answer.

Questions and answers can be edited or deleted by their owners until:

* 10 minutes have passed.
* In the case of a question, it cannot be edited or deleted after it has one
or more answers.
* In the case of an answer, it cannot be edited or deleted after it has one
or more votes or comments.

Lastly, add an API to do everything you can do through the web interface.

## Nightmare Mode

In addition to the above:

* Add votes and comments to questions as well.
* Track all events that change a user's points and show them on the user's
profile page.
