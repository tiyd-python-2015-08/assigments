# Weather Report

## Description

Create a Python application that will pull data from multiple Weather Underground API endpoints and present a weather report to the user.

## Tasks
```markdown
* Yak shaving
  * [ ] Create a GitHub repo called weather-report
  * [ ] Create a `requirement.txt` containing the `requests` and `requests-mock` libraries and any other dependencies
* Normal mode
  * [ ] Prompt the user for a ZIP code
  * [ ] Construct classes and API calls for the following features:
    * [ ] Current conditions at ZIP code
    * [ ] 10 day forecast for ZIP code
    * [ ] Sunrise and sunset times for ZIP code
    * [ ] Any current weather alerts for ZIP code
    * [ ] All active hurricanes (anywhere)
  * [ ] Use `requests-mock` to provide expected responses for testing purposes
  * [ ] Write test cases to cover each of the features of your classes
* Hard mode
  * [ ] Allow for city, state input in addition to ZIP code input
  * [ ] Turn your application into a Django web app
* Nightmare mode
  * [ ] Cache responses for recently made API calls
```

## Learning Objectives

After completing this assignment, you should:


* Understand the purpose and structure of Web APIs
* Understand JSON structure
* Be able to access an API using a token
* Be able to make HTTP requests via requests
* Be able to pull and merge information from multiple API endpoints
* Be able to write tests that mock API responses


## Details

### Deliverables

* A Git repo called urly-bird containing at least:
  * `README.md` file explaining how to run your project
  * a `requirements.txt` file
  * `weather.py`

### Requirements  

* No PEP8 or Pyflakes warnings or errors

## Normal Mode

Create a Python application which will query multiple API endpoints from Weather Underground and present a weather summary to the user. When the user runs the application, he or she will be asked for a zip code, and the summary will be for that location.

Your summary should be printed to the screen, and must include the following:

* Current conditions at that location
* 10 day forecast for that location
* Sunrise and sunset times
* Any current weather alerts
* A list of all active hurricanes (anywhere)

Make sure that the summary you display is easy to read for users. A pile of numbers with no descriptors won't do anyone any good.

Your code must be written in classes and be spread across multiple files. I suggest that you build one class for each API endpoint which you access, and then you create instances of each class when you have parameters to make a call to that endpoint. If you can think of a better way that still involves classes, though, go for it.

Testing is going to be tricky on this one. You should mock the API responses so that you don't need to hit the API every time you run your tests. You should also write unit tests using these mock responses for each of your features to help you judge your progress. Finally, you should able to explain WHY mocking is good for testing API calls.

No database is needed for Normal Mode.

## Hard Mode

Rather than just receiving a zip code from the user, allow him or her to type in a city and state instead (for instance: Durham, NC or Durham, North Carolina).

You should use regular expressions to determine which format (zip or city, state or city, st) the user has entered, and then make the appropriate API calls based on that.

Turn your application into a web app using Django.

No database is needed for Hard Mode. In Django, this means you might have an empty models.py file.

## Nightmare Mode

Store the responses in some way so that if the same request is made twice by your users, the information is pulled out of the database rather than hitting the APIs each time.

You may or may not need to use a database for this challenge.


## Resources

* [Requests](http://docs.python-requests.org/)
* [Weather Underground documentation](http://www.wunderground.com/weather/api/d/docs?MR=1)
* [requests-mock](http://requests-mock.readthedocs.org/)
