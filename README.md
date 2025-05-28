# 🚀 SpaceX Launch Success Prediction

> Capstone project for the **IBM Data Science Professional Certificate**.  
> Predicting Falcon 9 rocket landing success using SpaceX launch data, EDA, ML models, and interactive dashboards.

---

## 📌 Project Summary

This project explores SpaceX's Falcon 9 launch records to identify key factors that influence whether the rocket’s first stage successfully lands. The goal is to build machine learning models to predict landing success and create interactive tools for exploring the data.

---

## 🧠 Problem Statement

SpaceX aims to reduce launch costs by recovering and reusing rockets, but landing is not always successful.  
Can we **predict landing success** based on parameters like:

- Launch site
- Payload mass
- Orbit type
- Booster version

---

## 🛠️ Tech Stack

- **Languages**: Python, SQL  
- **Libraries**: Pandas, Scikit-learn, Plotly, Folium, Dash  
- **Tools**: Jupyter, Git, REST APIs (SpaceX), Web Scraping (Wikipedia)  
- **Models**: Logistic Regression, SVM, Decision Tree, K-Nearest Neighbors  

---

## 📈 Project Components

### 1. Data Collection & Cleaning
- Collected data via [SpaceX API](https://api.spacex.com/v4/launches/past) and Wikipedia.
- Cleaned and filtered for Falcon 9 launches.
- Engineered binary target variable (`landing_class`: 0 = fail, 1 = success).

### 2. Exploratory Data Analysis (EDA)
- Used SQL queries and visualizations to explore patterns.
- Key correlations: payload mass, booster version, launch site.
- Visualized trends and outcomes over time.

### 3. Interactive Visualization
- Built an interactive dashboard using **Plotly Dash**:
  - Dropdown to select launch site
  - Range slider for payload mass
  - Pie chart for site-wise success rates
  - Scatter plot to analyze payload vs. outcome
- Geospatial maps with **Folium** to locate and analyze launch sites.

### 4. Machine Learning Models
- Trained and evaluated:
  - Logistic Regression
  - SVM
  - Decision Tree
  - KNN
- Achieved ~83% accuracy across models.
- Evaluated results with confusion matrices and accuracy scores.

