# tau-pytest-bdd
This repository contains example code for the
*Behavior-Driven Python with pytest-bdd* course
from [Test Automation University](https://testautomationu.applitools.com/).
There is a branch for each chapter of the course showing the state of the code at the completion of the chapter.

## Version 4 Warning
The TAU course was developed with `pytest-bdd` version 3.
Unfortunately, **the version 4 update has incompatible changes.**
`@given` methods must now include a `target_fixture` parameter in order to work like pytest fixtures.
The TAU videos and transcripts use the old style of code,
but the example code here now uses the new style of code.
Below is an example of the new style of code needed:

```python
@given("the basket has 2 cucumbers", target_fixture='basket')
def basket():
    return CucumberBasket(initial_count=2)
```

## Setup
This project requires an up-to-date version of Python 3.
It also uses [pipenv](https://pipenv.readthedocs.io/) to manage packages.

To set up this project on your local machine:
1. Clone it from this GitHub repository.
2. Run `pipenv install` from the command line in the project's root directory.
3. For Web UI tests, install the appropriate browser and WebDriver executable.
   * These tests use Firefox and [geckodriver](https://github.com/mozilla/geckodriver/releases).

## Running Tests
Run tests simply using the `pytest` command.
Depending upon your environment, it may be better to use `python -m pytest`.
If you are using `pipenv`, then run `pipenv run python -m pytest`.
Use the "-k" option to filter tests by tags.

## More Info
For the best experience, take the full TAU course chapter-by-chapter.
Check out the branch for each chapter and follow along.

