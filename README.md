[![get-latest-offers](https://github.com/Ffyud/kortings/actions/workflows/get-latest-offers.yml/badge.svg)](https://github.com/Ffyud/kortings/actions/workflows/get-latest-offers.yml) [![deploy-to-gh-pages](https://github.com/Ffyud/kortings/actions/workflows/deploy-to-gh-pages.yml/badge.svg)](https://github.com/Ffyud/kortings/actions/workflows/deploy-to-gh-pages.yml) ![W3C Validation](https://img.shields.io/w3c-validation/default?targetUrl=https%3A%2F%2Fffyud.github.io%2Fkortings)

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

The data is collected trough a Python package called *parse_offers*. It will create a json file containing all the discount and move it to the app source code.

Run the Python script:

```
python parse_offers
```

## Github Actions

Through two workflows that run in *Github Actions* the app is continously being updated and deployed to *Github Pages*.

### get-latest-offers.yml
Runs the parse_offers script by a daily schedule.

### deploy-to-gh-pages.yml
Creates a build from the *kortings-app* and pushes it to the *gh-pages* branch. Github Pages uses this branch as the source.


