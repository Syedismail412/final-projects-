# final-projects-
#readme-1
# HR Employee Attrition Analysis

This project performs an exploratory data analysis (EDA) and builds a machine learning model to understand and predict employee attrition using the **HR Employee Attrition** dataset.

## 📊 Project Overview

The goal is to identify the key factors that contribute to employee attrition and use those insights to build a predictive model. The analysis includes:

- Data cleaning and inspection
- Univariate and bivariate visualizations
- Numerical feature analysis
- Random Forest Classifier for prediction

## 🧰 Tools & Libraries

- Python
- Pandas
- NumPy
- Seaborn
- Matplotlib
- Scikit-learn

## 🧾 Dataset

The dataset used is `HR-Employee-Attrition.csv`, which contains information about employees, including personal, professional, and salary-related features. The target variable is `Attrition` (Yes/No).

## 📈 EDA Highlights

- Countplots to analyze categorical variables like `BusinessTravel`, `Gender`, `OverTime`, etc.
- Histograms to study the distribution of numerical variables like `MonthlyIncome`, `DistanceFromHome`, etc.
- Correlation between features and employee attrition.

## 🤖 Model Building

- **Algorithm used:** Random Forest Classifier
- **Preprocessing:** Label encoding for the target, one-hot encoding for categorical features
- **Train/Test Split:** 80/20 ratio
- **Evaluation Metrics:** Confusion Matrix, Classification Report (Precision, Recall, F1-score)

## 📝 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/hr-employee-attrition.git
   cd hr-employee-attrition
