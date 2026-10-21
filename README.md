# ChurnIQ Analytics

**Telecom Customer Churn Prediction using Machine Learning**

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Streamlit-FF4B4B?logo=streamlit&logoColor=white)](https://churniq-analytics.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Machine Learning](https://img.shields.io/badge/ML-XGBoost-orange)](https://xgboost.readthedocs.io/)

ChurnIQ Analytics is a machine learning web app that estimates the likelihood that a telecom customer will leave the service. Enter a customer's account and service details to receive a churn probability and a risk classification.

## 🚀 Live Demo

**Try it here:** https://churniq-analytics.streamlit.app/

## ✨ Features

- Predicts customer churn probability from customer and service information.
- Presents a simple risk result to help explore potential churn cases.
- Uses a trained XGBoost model in a Streamlit interface.
- Applies the same preprocessing pipeline used during model training.
- Uses a configurable probability threshold to prioritize identifying more potential churners.

## 🧰 Tech Stack

- **Language:** Python
- **App:** Streamlit
- **Data processing:** pandas
- **Machine learning:** scikit-learn, XGBoost
- **Model persistence:** joblib
- **Dataset:** IBM Telco Customer Churn dataset

## 📊 Dataset

The project uses the IBM Telco Customer Churn dataset, containing customer demographics, subscribed services, account information, charges, tenure, and churn status.

The dataset contains **7,043 customer records and 21 columns**. `Churn` is the target variable. `customerID` is excluded from the model features.

### Data preparation

- Converted `TotalCharges` to a numeric column.
- The 11 blank `TotalCharges` values were converted to missing values and then filled with `0`; these records had `tenure = 0`.
- Checked for missing values and duplicate rows after cleaning.
- Encoded the target as `No = 0` and `Yes = 1`.
- Split the data into training and test sets using stratification.

## 🧠 Model and Evaluation

The project compared multiple classification approaches, including Logistic Regression, Decision Tree, Random Forest, Gradient Boosting, and XGBoost. The XGBoost pipeline was tuned using cross-validation.

The selected XGBoost model's reported test-set results at the default **0.50 threshold** were:

| Metric | Score |
|---|---:|
| Accuracy | 77.08% |
| Precision | 55.07% |
| Recall | 74.06% |
| F1-score | 63.17% |

### Why use a lower threshold?

Churn is the positive class. A lower probability threshold flags more customers as potential churners, which can increase recall but also produce more false positives.

Cross-validated predictions on the training set were used to compare thresholds. A **0.20 threshold** was selected to prioritize recall:

| Threshold | Recall | Precision | F1-score |
|---:|---:|---:|---:|
| 0.50 | 73.0% | 56.8% | 63.9% |
| 0.40 | 81.9% | 51.0% | 62.8% |
| 0.30 | 88.8% | 46.4% | 60.9% |
| 0.20 | 93.0% | 40.9% | 56.8% |

**Important:** The threshold comparison above comes from cross-validated predictions on the training set. The test-set metrics shown earlier use a 0.50 threshold. These results should not be presented as if they were measured on the same evaluation split.

## 🖥️ Run Locally

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd telecom-customer-churn-prediction
```

Replace `<YOUR_GITHUB_REPOSITORY_URL>` with the URL of your GitHub repository.

### 2. Create and activate a virtual environment (optional but recommended)

```bash
python -m venv .venv
```

On Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the app

Make sure `app.py` and `churn_model.pkl` are in the same project directory, then run:

```bash
streamlit run app.py
```

Streamlit will print a local URL in your terminal.

## 📁 Project Structure

```text
telecom-customer-churn-prediction/
├── Data/
│   └── raw/
│       └── WA_Fn-UseC_-Telco-Customer-Churn.csv
├── Telecom.ipynb
├── app.py
├── churn_model.pkl
├── requirements.txt
└── README.md
```

The trained model file contains the preprocessing and classification pipeline. Keep the model and application code compatible with the dependency versions used to create the model.

## ⚠️ Limitations

- Predictions are estimates based on patterns in the training dataset; they are not guarantees of future customer behavior.
- The selected 0.20 threshold favors finding more potential churners, at the cost of more false alarms.
- The dataset is historical and may not represent every telecom provider or current customer population.
- This project is intended for learning and demonstration. Business use would require further validation, monitoring, privacy review, and evaluation on representative data.

## 🔮 Possible Improvements

- Add model explainability to show which customer factors influence a prediction.
- Evaluate calibration and compare precision-recall trade-offs.
- Add a batch prediction workflow for multiple customers.
- Monitor model performance and data drift on new data.
- Add automated tests and input validation.

## 👤 Author

**Meet Kansara**  
Computer Science & Engineering student

- GitHub: [Meetkansara06](https://github.com/Meetkansara06)

---

If you find this project useful, consider giving the repository a ⭐ on GitHub.
