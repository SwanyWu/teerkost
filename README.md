[![get-latest-offers](https://github.com/Ffyud/kortings/actions/workflows/get-latest-offers.yml/badge.svg)](https://github.com/Ffyud/kortings/actions/workflows/get-latest-offers.yml) [![deploy-to-gh-pages](https://github.com/Ffyud/kortings/actions/workflows/deploy-to-gh-pages.yml/badge.svg)](https://github.com/Ffyud/kortings/actions/workflows/deploy-to-gh-pages.yml) [![run-parse-offers-test](https://github.com/Ffyud/kortings/actions/workflows/run-parse-offers-test.yml/badge.svg)](https://github.com/Ffyud/kortings/actions/workflows/run-parse-offers-test.yml)

# Kortings

Kortings collects the current discounts from popular Dutch supermarkets.

## Running the app

Start the app called *kortings-app* locally:
```
npm start
```

Build the app:
```
npm build
```

## Getting discounts

The data is collected trough a Python package called *parse_offers*. It will populate a json file containing all the discount and move it to the app source code.

Run the Python script:

```
python parse_offers
```

## Continuous deployment

Through three workflows the app is continously being updated, tested and deployed to Github Pages.

### 1. run-parse-offers-test.yml
Runs unittests against the parse_offers package to see if it returns actual results.

### 2. get-latest-offers.yml
Runs parse_offers by a daily schedule. A JSON file is populated with the offers found.

### 3. deploy-to-gh-pages.yml
Creates a build from the *kortings-app* and pushes it to the *gh-pages* branch. Github Pages uses this branch as the source.

