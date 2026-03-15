# Visa_Status_Prediction



## 📝 Description

Visa Status Processing Time Prediction is a machine learning project that analyzes historical visa application records to predict the number of days required to process a visa application.

Instead of predicting approval or rejection, this project focuses on estimating processing_days, helping to identify patterns and delays across visa types, applicant countries, employer regions, and seasonal trends.

The project follows a structured data science pipeline including:

- Data cleaning and preprocessing

- Exploratory Data Analysis (EDA)

- Feature engineering

- Preparation for predictive modeling

## Project Objective

To build a data-driven model that can:

- Analyze historical visa processing trends

- Identify key factors influencing processing delays

- Engineer meaningful features

- Prepare the dataset for regression modeling

## Project Structure

```
├── visa_dataset.csv
├── Milestone_1.ipynb
├── Milestone_2.ipynb
├── Milestone_3.ipynb
├── README.md
└── MIT_license.txt
```
## Dataset
- Cleaned dataset (`visa_dataset.csv`) is included in this repository.
- Columns include:
  - Application and decision dates
  - Applicant demographics (country, education, experience)
  - Employer information (city, state, number of employees)
  - Job details (title, experience, salary)
  - Other flags and indicators for visa processing

## Target Variable

processing_days — Number of days taken to process a visa application.

## Data Preprocessing
- Dataset inspection
- Missing value handling
- Data cleaning
- Target variable validation
- Ready-for-model dataset

## Exploratory Data Analysis
The following analyses were performed:

- Distribution of processing time

- Visa type-wise processing comparison

- Country-level processing trends

- Seasonal pattern analysis (month & season extraction)

- Employer state-level variation

- Correlation analysis for numeric features


## Feature Engineering
- Extracted month from case received date
- Created seasonal categories
- Generated country-level average processing feature
- Prepared numeric features for modeling

# Machine Learning Models (Milestone 3)

The project implements regression models to predict visa processing time.

### Model Used

**Random Forest Regressor**

Random Forest is an ensemble learning algorithm that builds multiple decision trees and combines their predictions to improve accuracy and reduce overfitting.

---

# Hyperparameter Tuning

To improve model performance, **GridSearchCV** was used to tune key parameters such as:

- Number of trees (`n_estimators`)
- Maximum tree depth (`max_depth`)
- Minimum samples split
- Minimum samples per leaf

Hyperparameter tuning helps identify the best combination of parameters for optimal prediction performance.

---

# Model Evaluation

Model performance was evaluated using regression metrics such as:

- **Mean Absolute Error (MAE)**
- **Mean Squared Error (MSE)**
- **Root Mean Squared Error (RMSE)**
- **R² Score**

These metrics help measure how accurately the model predicts visa processing time.

---

# Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook

## How to Use
1. Clone this repository:
   ```bash
   git clone https://github.com/Pavani-3101/Visa_Status_Prediction.git
2. Load the dataset in Python or Jupyter Notebook:
   
   import pandas as pd
   
   df = pd.read_csv("visa_dataset.csv")


## License
This project is licensed under the MIT License - see MIT_license.txt for details.

## Author
Pavani Manupati

---
