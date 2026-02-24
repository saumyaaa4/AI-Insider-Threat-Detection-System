# 🔐 AI-Powered Insider Threat Detection System

🚧 **Project Status:** Work in Progress – Core anomaly detection pipeline completed. Deployment and dashboard integration under development.

---

## 📌 Project Overview

This project implements a **machine learning-based anomaly detection system** to identify potential insider threats using employee behavioral log data.

The system analyzes patterns such as login activity, file access frequency, data download volume, and device usage behavior to detect abnormal activities that may indicate malicious intent.

The goal of this project is to simulate a real-world enterprise monitoring framework capable of identifying high-risk users using behavioral analytics.

---

## 🎯 Problem Statement

Insider threats are difficult to detect because malicious behavior often blends with normal activity. Traditional rule-based systems fail to identify subtle behavioral deviations.

This project applies **unsupervised machine learning techniques** to detect anomalies without relying on labeled fraud data.

---

## 📊 Dataset Description

A synthetic enterprise log dataset was generated containing features such as:

- Login frequency
- Login time deviation (after-hours access)
- File access count
- Data download volume
- Device usage anomalies
- System access irregularities

The dataset simulates realistic organizational activity patterns with behavioral variations.

---

## 🧹 Data Preprocessing

- Handled missing values  
- Standardized numerical features using **StandardScaler**  
- Performed exploratory data analysis (EDA)  
- Inspected feature distributions and behavioral trends  

---

## 📈 Exploratory Data Analysis (EDA)

EDA revealed:

- Significant variation in login timing among users  
- High file access activity correlated with increased anomaly scores  
- After-hours login behavior contributed strongly to suspicious patterns  

Visualizations included distribution plots, correlation heatmaps, and behavioral comparisons.

---

## 🤖 Model Implementation

### 1️⃣ Isolation Forest

- Used for unsupervised anomaly detection  
- Identified abnormal user behavior based on isolation depth  

### 2️⃣ One-Class SVM

- Implemented to compare anomaly detection performance  
- Evaluated sensitivity to rare behavioral patterns  

---

## 📊 Results

- Successfully detected anomalous behavioral patterns in employee activity logs  
- Isolation Forest demonstrated better stability in handling outliers  
- Users with unusual login hours combined with high data transfer showed higher anomaly scores  
- Implemented a **risk scoring mechanism** to classify employees based on anomaly intensity  

This approach demonstrates how machine learning can assist in proactive insider threat monitoring.

---

## 💡 Key Insights

- Behavioral deviation is a stronger indicator than individual activity spikes  
- Login timing irregularity significantly impacts anomaly detection  
- Unsupervised models can identify high-risk users without labeled fraud data  

---

## 🛠 Tech Stack

**Programming:** Python  
**Data Processing:** Pandas, NumPy  
**Machine Learning:** Scikit-learn (Isolation Forest, One-Class SVM)  
**Visualization:** Matplotlib, Seaborn  
**Tools:** Jupyter Notebook, Git, GitHub  

---

## 🔮 Future Enhancements

- Deep learning-based anomaly detection (Autoencoders)  
- Real-time monitoring dashboard using Streamlit  
- Integration with real enterprise log datasets  
- Advanced risk scoring and alert system  

---

## 👩‍💻 Author

**Saumya Bhagat**  
B.Tech | Data Analytics & Machine Learning  
GitHub: https://github.com/saumyaaa4  

---

## 📌 Project Status

Core anomaly detection pipeline completed. Future enhancements planned for deployment and real-time monitoring.
