[![get-latest-offers](https://github.com/Ffyud/kortings/actions/workflows/get-latest-offers.yml/badge.svg)](https://github.com/Ffyud/kortings/actions/workflows/get-latest-offers.yml) [![deploy-to-gh-pages](https://github.com/Ffyud/kortings/actions/workflows/deploy-to-gh-pages.yml/badge.svg)](https://github.com/Ffyud/kortings/actions/workflows/deploy-to-gh-pages.yml) [![run-parse-offers-test](https://github.com/Ffyud/kortings/actions/workflows/run-parse-offers-test.yml/badge.svg)](https://github.com/Ffyud/kortings/actions/workflows/run-parse-offers-test.yml) [![code-coverage](./parse_offers/coverage-badge.svg?dummy=8484744)](./parse_offers/htmlcov/index.html)

# Teerkost
![](https://teerkost.nl/logo192.png)

[https://teerkost.nl](https://teerkost.nl)

Teerkost collects the current discounts from popular Dutch supermarkets.

- It is fast - there is no backend it needs to call upon.
- It is uncluttered - filter by category, shop, discount or do a search.
- Bookmark offers by saving them locally using IndexedDb (i.e. "cookies").
- It is made to feel like an app.

## Running or building the app

Start the app called *kortings-app* locally:
```
npm start
```

## Getting discounts

The data is collected trough a Python package called *parse_offers*. 

It will populate a json file containing all the discounts and move it to the app source code.

Run the Python script:

```
python parse_offers
```

Run the tests from within the parse_offers folder:
```
python -m unittest -b -v
```
Run the tests and output Junit XML reporting:
```
python -m xmlrunner discover
```
Generate a code coverage report
```
coverage run -m unittest
coverage report
coverage html
```


## Continuous deployment

Through Github workflows the app is continously being updated, tested and deployed to Github Pages.

### 1. run-parse-offers-test.yml
Runs unittests against the parse_offers package to see if it returns complete results.

### 2. run-py-test-coverage.yml
Generates a code coverage report for the parse_offers package.

### 3. get-latest-offers.yml
Runs parse_offers by a daily schedule. A json file is populated with the offers found.

### 4. deploy-to-gh-pages.yml
Creates a build from the *kortings-app* and pushes it to the *gh-pages* branch. Github Pages uses this branch as the source.

### 5 Pylint on CircleCi
CircleCi [runs a code quality review](https://app.circleci.com/pipelines/github/Ffyud/teerkost?branch=main) of parse_offers with *Pylint*.