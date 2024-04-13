# Sri Lanka Labor Market Trend Project
Sri Lanka's Labor Market Trend Analysis Data Science Project

## Problem Statement:
The labor market in Sri Lanka is a crucial component of its economic landscape, influencing employment rates, workforce dynamics, and overall socio-economic development. However, amidst shifting global economic paradigms, technological advancements, and domestic policy reforms, understanding the current state and emerging trends within Sri Lanka's labor market is imperative for policymakers, businesses, researchers, and stakeholders alike. This study aims to delve into the intricacies of the Sri Lankan labor market to identify, analyze, and interpret the prevailing trends, challenges, and opportunities.

## Objectives:
* To analyze the correlation between educational attainment levels and employment opportunities, as well as wage differentials within the Sri Lankan labor market.
* To investigate the factors influencing labor force participation, including socio-cultural determinants, educational attainment, and regional disparities.
* To assess the impact of technological advancement and automation on job creation, skill requirements, and workforce dynamics within Sri Lanka.

## Deliverables:
* Code
* Streamlit UI
* Data Visualization Report


## Project Solution:
### 1.Data Collection and Analysis: 
Dataset is collected from the ILOSTAT website and the key factors that influence the Labor Force Participation( Gender, Education Level, Sector, Year ) are identified. After removing unwanted columns from the dataset, few columns are renamed for better understanding and rows with null target values are removed. This dataset is then plotted in a graph for better understanding and visualization using plotly express and graph objects.

### 2.Data Preprocessing: 
In this step, the dataset is checked for Categorical and numerical columns. Using the Impute Strategy as Median, the missing values are imputed for numerical columns. Using the Impute strategy and One-hot encoding for Categorical columns, the missing values are imputed and the categorical columns are transformed into columns with numerical values respectively.
Here the Categorical Columns are Gender, Sector and Education Level.

### 3.Model selection, Training and Evaluation: 
The dataset is divided into training , validation and test dataset. Using the training set, the model is trained for different machine learning algorithms like Linear Regression, Decision Tree Regression, Random Forest Regression and Support Vector Machine Regression. The model is used to predict values for data in the validation set and below are the metrics obtained ( Mean Absolute Error, Mean Squared Error and R2 Error ). 
| Model                     |Mean Absolute Error |Mean Squared Error| R2 Score | 
| :--------------           | :--------------:   | ---------------: |:--------:|
| Linear Regression         |8.47                |106.75            |0.80      |
| Random Forest Regressor   |1.79                |15.21             |0.97      |
| Decision Tree Regressor   |10.24               |217.78            |0.59      |
| Support Vector Regression |22.39               |726.66            |-0.33     |

### 4.Deployment: 
Based on the metrics obtained for different algorithms considered, Random Forest Regression has performed better, hence Random Forest Regression is used for prediction of results for test dataset. A Streamlit application [SriLankaLaborMarketTrend](https://sri-lanka-labor-market-trend.streamlit.app/) is created where user can provide values for features( Gender, Education Level, Sector and Year ) and predict the target value, i.e.Labor Force Participation Rate in %.

