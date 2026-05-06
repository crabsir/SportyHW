# Sporty Task

SportyHW is a Python automation test framework for running UI and API tests. It uses pip for dependency resolution, 
PyTest for test management and running tests, Selenium Webdriver for UI tests, and Python Requests for API testing.

Component versions are listed in `requirements.txt`.

## Pre-requisites

To be able to use this framework Python 3.9+ and pip 21.4+ are needed.

Install using your package manager (example for Homebrew):

```
brew install python3
brew install pip
```

Chromedriver will be needed for UI tests. Setup guide is available here: 
https://developer.chrome.com/docs/chromedriver/get-started

## Setting up resources

Sporty QA account with balance greater than 10 EUR will be required.

## Install dependencies

Use `pip` to install required project dependencies:

```
source <venv>/bin/activate
% pip install -r requirements.txt
```

## Running tests

Run tests using pytest in project's Python environment from project root. 
Make sure to specify `user_id` for authentication:

```
source <venv>/bin/activate
% pytest --user_id <yourUserId>
```

It is possible to run tests in specific test file using:

```
% pytest test_file.py --user_id <yourUserId>
```

Markers can be used to run specific groups of tests:

```
% pytest -m <api|ui> --user_id <yourUserId>
```
