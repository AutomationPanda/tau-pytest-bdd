# tau-pytest-bdd
This repository contains example code for the
*Behavior-Driven Python with pytest-bdd* course
from [Test Automation University](https://testautomationu.applitools.com/).
There is a branch for each chapter of the course showing the state of the code at the completion of the chapter.

## Setup
This project requires an up-to-date version of Python 3.
It also uses [pipenv](https://pipenv.readthedocs.io/) to manage packages.

To set up this project on your local machine:
1. Clone it from this GitHub repository.
2. Run `pipenv install` from the command line in the project's root directory.
3. For Web UI tests, install the appropriate WebDriver executables
  (like [ChromeDriver](http://chromedriver.chromium.org/) or [geckodriver](https://github.com/mozilla/geckodriver/releases)).

## Running Tests
Run tests simply using the `pytest` command.
Depending upon your environment, it may be better to use `python -m pytest`.
If you are using `pipenv`, then run `pipenv run python -m pytest`.
Use the "-k" option to filter tests by tags.

## More Info
For the best experience, take the full TAU course chapter-by-chapter.
Check out the branch for each chapter and follow along.
