<<<<<<< HEAD
# Electricity Price Explanation

## Project Overview

This project is an assignment for an ensemble learning course, conducted by a team comprising Irene Sunny, Wenjing Zhao, Hongyang Ye, and Zheng Wan. The focus of this project is to model electricity prices based on weather, energy (commodities), and commercial data for two European countries: France and Germany. It's crucial to understand that this project aims to explain electricity prices with simultaneous variables rather than predicting them.

### Challenge Goals

The primary objective is to develop a model that uses explanatory variables to accurately estimate the daily price variation of electricity futures contracts in France and Germany. These futures contracts are financial instruments that provide an expected value on the future price of electricity, focusing on short-term maturity contracts (24h). The dynamic market of electricity future exchange in Europe is the context of this challenge.

Participants are given daily data for each country, including weather quantitative measurements (temperature, rain, wind), energetic production (commodity price changes), and electricity usage (consumption, exchanges between the two countries, import-export with the rest of Europe). The performance metric for this challenge is the Spearman's correlation between the participant's output and the actual daily price changes over the test dataset.

For more details about the challenge and Q&A, participants are encouraged to visit our dedicated forum and LinkedIn page.

### Data Description

The provided dataset consists of three CSV files: `X_train` (training inputs), `Y_train` (training outputs), and `X_test` (test inputs), with the following structure:

- **Input Datasets (`X_train` and `X_test`)**: Represent the same explanatory variables over two different time periods, comprising 35 columns, including unique row identifiers (ID), day and country identifiers (DAY_ID, COUNTRY), daily commodity price variations, weather measures, energy production measures, and electricity use metrics.
- **Output Datasets**: Composed of two columns (ID, TARGET), where `TARGET` is the daily price variation for futures of 24H electricity baseload.

### Benchmark Description

The benchmark for this challenge is a simple linear regression model, with missing values filled with zeros and the COUNTRY column omitted, using the same model for France and Germany. The public score obtained with this benchmark is 15.86%.

For further details and examples, refer to the notebook in the "supplementary files" section of the challenge website.

### Project Link

For more information and resources, visit the project's original link: [Electricity Price Explanation Challenge](https://challengedata.ens.fr/participants/challenges/97/)

---
**Team Members**: Irene Sunny, Wenjing Zhao, Hongyang Ye, Zheng Wan
=======
# Ensemble-Learning-Project-G3-T7
Team report for the course Ensemble Learning
>>>>>>> 0e6c340dd7a2df5fe5b9d5a467eca7a1bb5c3b1e
