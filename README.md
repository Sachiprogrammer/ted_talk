# 🎤 TED Talk Popularity Prediction

## 📌 Overview
This project leverages **deep learning** to predict the popularity of TED Talks (measured by views) based on various attributes such as speaker occupation, event type, number of comments, and ratings. The model is trained using a **Neural Network (ANN)** and evaluates key features influencing TED Talk engagement.

## 🚀 Features
- 📊 **Data Preprocessing**: Cleans and encodes categorical variables.
- 🔍 **Feature Engineering**: Extracts insights like time-to-publish, number of tags, and ratings distribution.
- 🧠 **Deep Learning Model**: Uses a **fully connected neural network (ANN)** with Dropout layers to enhance generalization.
- 📈 **Performance Metrics**: Evaluates model accuracy using **MAE, RMSE, and R² Score**.
- 🏆 **Feature Importance Analysis**: Identifies the most significant factors affecting TED Talk views.

## 📂 Dataset
The dataset used is from **[Kaggle: TED Talks Dataset](https://www.kaggle.com/datasets/rounakbanik/ted-talks/data)**.

## ⚙️ Installation
```bash
git clone https://github.com/yourusername/ted-talk-popularity.git
cd ted-talk-popularity
pip install -r requirements.txt
```

## 🏗️ Usage
```bash
python ted_talk_.py
```

## 📊 Model Performance
- **Mean Absolute Error (MAE)**: Measures average absolute error.
- **Root Mean Squared Error (RMSE)**: Captures large deviations.
- **R² Score**: Evaluates model’s accuracy in predicting TED Talk views.

## 🔥 Results
| Metric  | Score |
|---------|------------|
| MAE     | 976,776.31 |
| RMSE    | 1,947,763.55 |
| R² Score | 4.29% |
