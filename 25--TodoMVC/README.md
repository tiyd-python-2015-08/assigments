# TodoMVC - AngularJS + Django

## Description

Create a REST API for use with the AngularJS TodoMVC app.

## Tasks
```markdown
* Yak shaving
  * [ ] Fork the [todomvc-django](https://github.com/tiyd-python-2015-08/todomvc-django) repository
* Normal mode
  * [ ] Create your model(s)
  * [ ] Create an API with the following endpoints:
    * GET `/api/todos/`
    * POST `/api/todos/`
    * PUT `/api/todos/{id}`
    * DELETE `/api/todos/{id}`
* Hard mode
  * [ ] Write functional tests for your API
```

## Objectives

After completing this assignment, you should be able to:

* Summarize the REST architecture.
* Design a simple REST API.

### Deliverables

* A Git repo called todomvc-django containing at least:
  * `README.md` file explaining how to run your project
  * a `requirements.txt` file
  * a Django project

### Requirements  

* No PEP8 or Pyflakes warnings or errors

## Normal Mode

Using the Django REST Framework, build an API with one resource: `todos`.

Your URLs should be nested under `/api/`, and will look like:

* GET `/api/todos/`
* POST `/api/todos/`
* PUT `/api/todos/{id}`
* DELETE `/api/todos/{id}`

The todo resource should have the following fields:

* id
* title - string, required
* completed - boolean, default false
* order - integer, not required, can be null

When your project is complete, you should be able to run it by visiting your local web server at "/" and get the AngularJS-backed Todo MVC application. Try testing it using an incognito browser to be sure it works and is storing data in your Django project.

## Hard Mode

For hard mode, do everything shown above, plus add functional tests for your API.
