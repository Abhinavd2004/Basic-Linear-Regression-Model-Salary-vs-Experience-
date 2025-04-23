# 📊 Basic Linear Regression Model – Salary vs Experience

## 🧠 Problem Statement  
Predict a person’s **salary** based on their **years of experience** using a **simple linear regression model**.

---

## 📘 Model Type: Simple Linear Regression

Simple Linear Regression is a statistical technique that models the relationship between two variables:

- **Independent Variable (X)**: Years of Experience  
- **Dependent Variable (Y)**: Salary

---

## 📐 Mathematical Representation

Salary = β₀ + β₁ * Experience + ε



Where:  
- `β₀`: Intercept (base salary when experience = 0)  
- `β₁`: Slope (increment in salary per year of experience)  
- `ε`: Error term (residual)

---

## 🛠️ Steps to Build the Model

1. **Data Collection**  
   - Collect historical data of employees with their years of experience and salaries.

2. **Data Preprocessing**  
   - Clean the dataset.
   - Handle missing or inconsistent values.
   - Format the data properly for modeling.

3. **Train-Test Split**  
   - Split the data into training and testing sets (e.g., 80% training, 20% testing).

4. **Model Training**  
   - Fit a simple linear regression model using training data.

5. **Prediction**  
   - Predict salaries for new experience values using the trained model.

---

## 📈 Output Visualization

- Scatter plot of `Years of Experience` vs `Salary`.
- A regression line fitted over the data points.

---

## ✅ Usage

This model is useful for:
- HR salary estimation
- Forecasting salary trends
- Salary benchmarking based on experience

---

## 📂 Example

```python
from sklearn.linear_model import LinearRegression
import pandas as pd

# Load data
data = pd.read_csv("salary_data.csv")
X = data[['YearsExperience']]
y = data['Salary']

# Train model
model = LinearRegression()
model.fit(X, y)

# Predict
experience = [[5]]
predicted_salary = model.predict(experience)
print(f"Predicted Salary for 5 years experience: ₹{predicted_salary[0]:.2f}")
