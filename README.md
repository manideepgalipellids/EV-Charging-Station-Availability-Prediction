# EV Charging Station Availability Prediction

## Project Overview
This project applies supervised machine learning techniques to predict EV charging station availability using the EV Charging Station Availability Tracking dataset.

The project investigates multiple research questions related to:
- baseline model performance,
- preprocessing impact,
- feature importance,
- robustness,
- and practical deployment suitability.

---

## Dataset

Dataset Source:
https://www.kaggle.com/datasets/likithagedipudi/ev-charging-station-availability-tracking

Dataset Name:
EV Charging Station Availability Tracking

---

## Machine Learning Models Used

- Logistic Regression
- Decision Tree
- Random Forest
- Naive Bayes

---

## Research Questions

1. Baseline model performance
2. Model comparison
3. Effect of preprocessing
4. Feature importance analysis
5. Sensitivity to evaluation metrics
6. Robustness and generalization
7. Practical usefulness and deployment suitability

---

## Repository Structure

```text
EV-Charging-ML-Project/
│
├── figures/
├── tables/
├── EV_Charging_ML_Code.ipynb
├── Proposal.pdf
├── app.py
├── requirements.txt
└── README.md

## How to Run

### Option 1: Run Locally

1. Download dataset from Kaggle
2. Open Jupyter Notebook
3. Run:

```python
EV_Charging_ML_Code.ipynb
```

Install dependencies:

```bash
pip install -r requirements.txt
```

### Option 2: Use Live Application

Access the deployed system directly:

https://manideep950-ev-charging-recommendation.hf.space

---

## Deployment

A Gradio-based interactive web application was developed for practical EV charging station recommendation.

The system allows users to:

- Select Date
- Select Preferred Charging Time
- Select City
- View Available Charging Stations
- Get Best Recommended Charging Station

---

## Live Application

Try the deployed application here:

https://manideep950-ev-charging-recommendation.hf.space