# Visa_Status_Prediction



## 📝 Description

Visa_Status_Prediction is a sophisticated machine learning solution designed to forecast the outcome of visa applications by analyzing historical datasets. This project leverages predictive modeling to identify key factors influencing visa approvals, such as applicant demographics, professional background, and employer information. By implementing a comprehensive data science pipeline—encompassing rigorous data cleaning, exploratory data analysis (EDA), and the deployment of classification algorithms like Random Forest or Gradient Boosting—the tool provides valuable insights for applicants and immigration professionals alike. The goal is to improve decision-making transparency and streamline the evaluation process through accurate, data-driven predictions.

## 📁 Project Structure

```
.
├── MIT license.txt
├── Visa_Status_Prediction.ipynb
└── visa_dataset.csv
```
## Dataset
- Cleaned dataset (`visa_dataset.csv`) is included in this repository.
- Columns include:
  - Application and decision dates
  - Applicant demographics (country, education, experience)
  - Employer information (city, state, number of employees)
  - Job details (title, experience, salary)
  - Other flags and indicators for visa processing

## Features
- Cleaned and preprocessed dataset
- Numeric and categorical columns normalized
- Y/N flags converted to numeric
- Missing values handled

## How to Use
1. Clone this repository:
   ```bash
   git clone https://github.com/Pavani-3101/Visa_Status_Prediction.git
2. Load the dataset in Python or Jupyter Notebook:
   
   import pandas as pd
   
   df = pd.read_csv("visa_dataset.csv")
4. Begin your analysis or build machine learning models.

## License
This project is licensed under the MIT License - see MIT_license.txt for details.

## Author
Pavani Manupati

---
