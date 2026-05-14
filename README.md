# 🩺 Diabetes Prediction System

[![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML%20Model-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=flat-square&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=flat-square&logo=jupyter&logoColor=white)](https://jupyter.org/)
[![Live Demo](https://img.shields.io/badge/🤗%20Hugging%20Face-Live%20Demo-yellow?style=flat-square)](https://huggingface.co/spaces/Prabhath6/Diabetes_Prediction)

> **A clinical health risk analysis system powered by K-Nearest Neighbors (KNN) that predicts whether a patient is Non-Diabetic, Pre-Diabetic, or Diabetic — based on real blood biomarker inputs via an interactive Streamlit interface.**

🌐 **[Live Demo → Try it on Hugging Face Spaces](https://huggingface.co/spaces/Prabhath6/Diabetes_Prediction)**

---

## 📖 Table of Contents

- [About the Project](#-about-the-project)
- [How It Works](#-how-it-works)
- [Features](#-features)
- [Input Parameters](#-input-parameters)
- [ML Pipeline](#-ml-pipeline)
- [Prediction Output](#-prediction-output)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
- [How to Use](#-how-to-use)
- [Notebook Overview](#-notebook-overview)
- [Contributing](#-contributing)
- [Disclaimer](#-disclaimer)
- [License](#-license)

---

## 🧠 About the Project

The **Diabetes Prediction System** is a machine learning–powered web application that takes a patient's clinical blood report values as input and predicts their diabetes status in real time — classifying them as **Non-Diabetic**, **Pre-Diabetic**, or **Diabetic**.

The system is built around a **K-Nearest Neighbors (KNN)** classifier trained on real patient biomarker data, with a complete preprocessing pipeline including **OneHot Encoding** for categorical features, **Ordinal Encoding** for the target class, and **Standard Scaling** for numerical features — all saved as serialized `.pkl` files for seamless deployment.

This project demonstrates a full end-to-end ML workflow: from raw data exploration and model training in a Jupyter Notebook, to a production-ready Streamlit web app.

---

## ⚙️ How It Works

```
User fills in blood report values
          ↓
Gender → OneHot Encoded  (OneHot.pkl)
Numerical features → Standard Scaled  (Standard.pkl)
          ↓
KNN Classifier predicts class  (KNN.pkl)
          ↓
Ordinal label decoded → "Non-Diabetic / Pre-Diabetic / Diabetic"
          ↓
Contextual health message displayed to user
```

---

## ✨ Features

- 🩸 **Real Blood Biomarker Inputs** — uses clinically meaningful values (HbA1c, cholesterol, triglycerides, LDL, HDL, VLDL, BMI, creatinine, urea)
- 🤖 **KNN Classifier** — trained and serialized model for instant inference
- 🔄 **Full Preprocessing Pipeline** — OneHot encoding + Standard scaling applied automatically on each prediction
- 🎯 **3-Class Output** — distinguishes Non-Diabetic, Pre-Diabetic, and Diabetic with color-coded alerts
- 💬 **Contextual Health Advice** — each result comes with a relevant health message (info / warning / error)
- 🖥️ **Clean 2-Column Layout** — all inputs organized in a responsive grid via Streamlit columns
- ⚡ **Instant Prediction** — single button click triggers end-to-end inference in milliseconds

---

## 🔬 Input Parameters

The app collects **11 clinical features** from the user:

| Feature | Description | Range |
|---|---|---|
| **Gender** | Patient's gender | M / F |
| **Age** | Patient's age in years | — |
| **Urea** | Blood urea level | 0.5 – 40.0 |
| **Creatinine (Cr)** | Kidney function marker | 6 – 800 |
| **HbA1c** | Glycated hemoglobin — key diabetes marker | 0.9 – 16.0 |
| **Cholesterol (Chol)** | Total cholesterol level | 0.0 – 10.3 |
| **Triglycerides (TG)** | Blood fat level | 0.3 – 13.8 |
| **HDL** | High-density lipoprotein ("good" cholesterol) | 0.2 – 9.9 |
| **LDL** | Low-density lipoprotein ("bad" cholesterol) | 0.3 – 9.9 |
| **VLDL** | Very low-density lipoprotein | 0.1 – 35.0 |
| **BMI** | Body Mass Index | 19 – 48 |

> 💡 **HbA1c** is the most clinically significant feature — values above 6.5% are typically diagnostic of diabetes.

---

## 🧪 ML Pipeline

### Preprocessing

| Step | Tool | File |
|---|---|---|
| Categorical encoding of Gender | `OneHotEncoder(drop="first")` | `OneHot.pkl` |
| Numerical feature scaling | `StandardScaler` | `Standard.pkl` |
| Target label encoding | `OrdinalEncoder` | `Ordinal.pkl` |

### Model

| Property | Detail |
|---|---|
| **Algorithm** | K-Nearest Neighbors (KNN) |
| **Task** | Multi-class classification (3 classes) |
| **Serialization** | `pickle` (`.pkl`) |
| **Model file** | `KNN.pkl` |

### Training (Notebook)

The full ML workflow is documented in `Diabetes_Prediction2.ipynb`, covering:

- Exploratory Data Analysis (EDA)
- Feature engineering and encoding
- Model training and hyperparameter selection
- Model evaluation and serialization

---

## 🎯 Prediction Output

| Result | Alert Type | Message |
|---|---|---|
| ✅ **Non-Diabetic** | 🔵 Info | You are healthy. Keep maintaining a balanced diet and regular exercise. |
| ⚠️ **Pre-Diabetic** | 🟡 Warning | You are at risk. Consult a doctor soon and maintain a healthy lifestyle. |
| 🚨 **Diabetic** | 🔴 Error | You have diabetes. Please consult your doctor regularly and maintain a healthy diet. |

---

## 🛠️ Tech Stack

| Technology | Role |
|---|---|
| **Python 3.9+** | Core language |
| **Streamlit** | Web app UI and deployment |
| **Scikit-learn** | KNN classifier, encoders, scaler |
| **Pandas** | Input data structuring |
| **Pickle** | Model and preprocessor serialization |
| **Jupyter Notebook** | Model training and EDA |

---

## 📁 Project Structure

```
Diabetes_Prediction/
│
├── app.py                        # Streamlit web app — UI, preprocessing, inference
├── Diabetes_Prediction2.ipynb    # Full ML workflow — EDA, training, evaluation
│
├── KNN.pkl                       # Trained K-Nearest Neighbors classifier
├── OneHot.pkl                    # Fitted OneHotEncoder for Gender feature
├── Ordinal.pkl                   # Fitted OrdinalEncoder for target labels
├── Standard.pkl                  # Fitted StandardScaler for numerical features
│
└── requirements.txt              # Python dependencies
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.9 or higher
- pip

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Prabhath66/Diabetes_Prediction.git
   cd Diabetes_Prediction
   ```

2. **Create and activate a virtual environment (recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate        # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Streamlit app:**
   ```bash
   streamlit run app.py
   ```

5. Open your browser at `http://localhost:8501`

---

## 📌 How to Use

1. **Open the app** — either locally at `localhost:8501` or via the [Hugging Face live demo](https://huggingface.co/spaces/Prabhath6/Diabetes_Prediction).

2. **Enter patient details** — fill in all 11 fields using the 2-column input grid. All values correspond to standard blood report readings.

3. **Click "Predict"** — the model preprocesses the inputs and runs KNN inference instantly.

4. **Read the result** — the app displays:
   - The predicted diabetes class (Non-Diabetic / Pre-Diabetic / Diabetic)
   - A color-coded alert (blue / yellow / red)
   - A contextual health recommendation

---

## 📓 Notebook Overview

`Diabetes_Prediction2.ipynb` covers the complete ML pipeline:

- **Data Loading & Exploration** — dataset shape, feature distributions, class balance
- **Preprocessing** — handling nulls, encoding categoricals, scaling numerics
- **Model Training** — KNN classifier with cross-validation
- **Evaluation** — accuracy, confusion matrix, classification report
- **Serialization** — saving all fitted transformers and the model as `.pkl` files

---

## 🤝 Contributing

Contributions are welcome! Here's how:

1. Fork the repo
2. Create your feature branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m "Add: your feature"`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a Pull Request

### Ideas for Contributions

- 📊 Add a feature importance / SHAP explainability chart
- 🔁 Compare KNN against Random Forest, SVM, or XGBoost
- 📁 Add support for CSV batch prediction (upload a file, predict all rows)
- 📈 Display model confidence / probability scores alongside the result
- 🌐 Add multilingual support for wider accessibility
- 📋 Add a downloadable prediction report as PDF

---

## ⚠️ Disclaimer

> This application is intended for **educational and research purposes only**. It is **not** a substitute for professional medical advice, diagnosis, or treatment. Always consult a qualified healthcare provider for any health concerns or before making any medical decisions.

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

Made with ❤️ and 🩺 by [Prabhath66](https://github.com/Prabhath66)

⭐ **If this project helped you, drop a star!** ⭐
