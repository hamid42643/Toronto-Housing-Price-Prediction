# Toronto Housing Price Prediction

This repository contains the code and datasets used for building and evaluating machine learning models to predict housing prices in the Toronto Area. Our goal is to develop a  prediction model given the variability and complexity of the Toronto real estate market.

## Project Structure

- `get-data/`: Scripts for data collection and preprocessing.
  - `zillow.py`: Fetch data from Zillow API.
  - `geoapify.py`: Script to enrich data with latitude and longitude information.

## Setup

To set up the project environment:

1. Install Python 3.8 or above.
2. Install required Python packages:
   ```bash
   pip install -r requirements.txt

To run the data collection scripts, ensure that config.py is set up with the correct api keys from rapidapi:

