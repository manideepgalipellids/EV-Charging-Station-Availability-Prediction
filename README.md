# ⚡ EV Charging Station Availability Prediction

An interactive EV charging station finder built using Python, Streamlit, and Machine Learning.

## 🚗 Project Overview

This project explores EV charging station availability using supervised machine learning techniques and the **EV Charging Station Availability Tracking** dataset.

The project focuses on evaluating different machine learning models, investigating data preprocessing techniques, analyzing feature importance, and studying model robustness and practical deployment suitability.

It also includes an interactive web application, **EV ChargeFinder**, that helps users discover available EV charging stations based on their preferred date, time, and city.

## 🌐 Live Application

**Try EV ChargeFinder here:**

[https://ev-charging-station-availability-prediction.streamlit.app/](https://ev-charging-station-availability-prediction.streamlit.app/)

## 📊 Dataset

- **Dataset Name:** EV Charging Station Availability Tracking
- **Source:** Kaggle
- **Dataset Link:** [EV Charging Station Availability Tracking](https://www.kaggle.com/datasets/likithagedipudi/ev-charging-station-availability-tracking)
- **Original Dataset Size:** 1,317,750 records
- **Number of Charging Stations:** 150
- **Number of Cities:** 15

A lightweight deployment dataset containing 3,600 station-hour records is used by the Streamlit application to support faster loading and deployment.

## 🤖 Machine Learning Models

The project evaluates the following supervised machine learning algorithms:

- Logistic Regression
- Decision Tree
- Random Forest
- Naive Bayes

## 🔬 Research Questions

The project investigates seven research questions:

1. **Baseline Model Performance** – Evaluate baseline machine learning performance.
2. **Model Comparison** – Compare the performance of different algorithms.
3. **Preprocessing Impact** – Analyze the effect of data preprocessing techniques.
4. **Feature Importance** – Identify important features influencing predictions.
5. **Metric Sensitivity** – Study model performance using different evaluation metrics.
6. **Robustness and Generalization** – Evaluate model stability and generalization.
7. **Practical Usefulness** – Investigate practical deployment suitability.

## ✨ Application Features

EV ChargeFinder provides an interactive interface with the following features:

- Select a preferred charging date.
- Choose a preferred charging time.
- Select a city.
- View available EV charging stations.
- Identify the recommended charging station.
- Compare available and occupied charging points.
- View estimated waiting times.
- Explore the top available charging stations.

## 🛠️ Technologies Used

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Data Analysis | Pandas, NumPy |
| Machine Learning | Scikit-learn |
| Data Visualization | Matplotlib, Seaborn |
| Interactive Application | Streamlit |
| Notebook Environment | Jupyter Notebook |
| Dataset Source | Kaggle |
| Version Control | Git, GitHub |
| Deployment | Streamlit Community Cloud |

## 📁 Repository Structure

```text
EV-Charging-ML-Project/
│
├── .streamlit/
│   └── config.toml
│
├── deploy/
│   ├── app.py
│   └── requirements.txt
│
├── figures/
│   ├── RQ1_Baseline_Figure.pdf
│   ├── RQ2_Model_Comparison_Figure.pdf
│   ├── RQ3_Preprocessing_Figure.pdf
│   ├── RQ4_Feature_Importance_Figure.pdf
│   ├── RQ5_Metric_Sensitivity_Figure.pdf
│   ├── RQ6_Robustness_Figure.pdf
│   └── RQ7_Practical_Usefulness_Figure.pdf
│
├── tables/
│   ├── RQ1_Baseline_Table.csv
│   ├── RQ2_Model_Comparison_Table.csv
│   ├── RQ3_Preprocessing_Table.csv
│   ├── RQ4_Feature_Importance_Table.csv
│   ├── RQ5_Metric_Sensitivity_Table.csv
│   ├── RQ6_Robustness_Table.csv
│   └── RQ7_Decision_Matrix_Table.csv
│
├── EV_Charging_ML_Code.ipynb
├── Proposal.pdf
├── app.py
├── ev_charging_station_data_deploy.csv
├── requirements.txt
└── README.md
```

## ⚙️ How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/manideepgalipellids/EV-Charging-Station-Availability-Prediction.git
```

### 2. Navigate to the Project Directory

```bash
cd EV-Charging-Station-Availability-Prediction
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit Application

```bash
streamlit run app.py
```

The application will open in your browser at:

```text
http://localhost:8501
```

### 5. Run the Machine Learning Notebook

Open `EV_Charging_ML_Code.ipynb` using Jupyter Notebook or JupyterLab.

Download the original dataset from Kaggle and configure its path before running the notebook.

## 🚀 Deployment

The EV ChargeFinder application is deployed using **Streamlit Community Cloud** and connected to this GitHub repository.

The application automatically updates when new changes are pushed to the connected GitHub branch.

**Live Demo:** [EV ChargeFinder](https://ev-charging-station-availability-prediction.streamlit.app/)

## ⚠️ Limitations

- The deployed application uses a lightweight dataset containing 3,600 station-hour records rather than the complete original dataset.
- Station availability is based on the records available in the dataset and should not be interpreted as real-time information from physical charging stations.
- The selected date is displayed in the application, while station filtering is based on the available city and time fields.

## 🔮 Future Improvements

- Integrate real-time EV charging station APIs.
- Improve station availability prediction using advanced machine learning models.
- Add interactive maps and distance-based recommendations.
- Include live traffic and weather information.
- Expand the application to support more cities and charging networks.

## 👨‍💻 Author

**Manideep Galipelli**

Master's Student in Data Science

- GitHub: [@manideepgalipellids](https://github.com/manideepgalipellids)

---

⭐ If you find this project interesting, consider giving the repository a star!