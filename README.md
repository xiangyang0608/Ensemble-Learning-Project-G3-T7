# Electricity Price Explanation

## Project Overview

This project is an assignment for an ensemble learning course, conducted by a team comprising Irene Sunny, Wenjing Zhao, Hongyang Ye, and Zheng Wan. The focus of this project is to model electricity prices based on weather, energy (commodities), and commercial data for two European countries: France and Germany. This project aims to explain electricity prices with simultaneous variables rather than predicting them.

### Challenge Goals

The main goal is to create a model that accurately predicts daily price changes in electricity futures contracts for France and Germany. These contracts represent expected future electricity prices over a short-term period (24 hours). The data provided includes daily information such as weather conditions (temperature, rainfall, wind), energy production (changes in commodity prices), and electricity usage (consumption, exchanges between countries, import-export with the rest of Europe). The performance of the model will be evaluated using Spearman's correlation coefficient between the predicted and actual daily price changes on the test dataset.

##  Methodology

### EDA

- A concise EDA was performed to identify key data characteristics.
- Findings are detailed in the EDA folder.

### Preprocessing

- Missing values were interpolated or filled with zero where appropriate.
- Data was scaled to a standard range using `StandardScaler`.
- PCA was employed to address multicollinearity, retaining 95% variance.

*For detailed EDA, see the EDA folder. Preprocessing helper functions are located in the Util folder.*

### Models Overview

- Explored a wide range of single models including decision trees, linear regression, and LSTM.
- Implemented ensemble methods taught in class, specifically boostraping and bagging.
- Concluded our experimentation with a stacked model to leverage the strengths of individual models.

*All models and their variations are documented within the Models folder. boostraping and bagging methods can be found under their respective filenames.*

### Feature Engineering

- Through analysis, identified temporal characteristics in the dataset (see MA.ipynb for details).
- Hypothesized that the target time-series data fits a Moving Average (MA) model based on PACF plot observations.
- Based on the previous assumptions, we engineered new features by incorporating lagged data from previous days, enhancing the model's predictive strength.
- This addition led to notable performance improvements in our models, as evidenced by the comparison between Bagging (baseline) and Bagging_FE (feature-engineered) notebooks, with the exception of KNN and SVR.

*Feature engineering details and model comparisons are available in the respective notebook files within the Models folder.*

### Future Improvements

- **Code and Repository Management**: Our project's GitHub repository and codebase could benefit from better organization and management. Streamlining the structure and documentation will enhance readability and collaboration efficiency.

- **Model Overfitting**: There appears to be a significant overfitting issue on the training set, as indicated by the stacked model's underperformance compared to the best base model. Future efforts could focus on refining the tuning process to enhance the models' interpretability and address their shortcomings.

- **Model Performance Anomalies**: The negative correlation observed in the performance of SVR and KNN regressors with the introduction of new features is puzzling. This warrants further investigation to understand the underlying causes and to improve the robustness of these models.

*Addressing these points will be crucial for the continued development and success of the project.*

### Project Link

For more information and resources, visit the project's original link: [Electricity Price Explanation Challenge](https://challengedata.ens.fr/participants/challenges/97/)

Our highest achievements on the website have reached a public score of 0.4641.

---
**Team Members**: Irene Sunny, Wenjing Zhao, Hongyang Ye, Zheng Wan
