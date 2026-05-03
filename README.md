# Student Performance Prediction using Machine Learning

## Project Overview

This project predicts a student's math score based on various academic and demographic features such as reading score, writing score, gender, parental education, lunch type, and test preparation.

The model is built using a Random Forest Regressor and deployed as a web application using Flask on Hugging Face Spaces.

---

## Features

* Predict student math score from input features
* Data preprocessing (encoding and scaling)
* Model training using Random Forest Regression
* Model evaluation using:

  * Mean Squared Error (MSE)
  * R² Score
  * K-Fold Cross Validation
* Visualization:

  * Decision Tree
  * Feature Importance
* Web interface using Flask
* Deployment using Docker on Hugging Face Spaces

---

## Technologies Used

* Python
* Pandas, NumPy
* Scikit-learn
* Matplotlib
* Flask
* Docker
* Hugging Face Spaces

---

## Project Structure

```
├── app.py
├── train_model.py
├── model.pkl
├── scaler.pkl
├── encoders.pkl
├── requirements.txt
├── Dockerfile
├── students.csv
├── templates/
    └── index.html

```

---

## How It Works

1. User inputs data through the web interface
2. Flask receives and processes the input
3. Categorical features are encoded and numerical features are scaled
4. The processed data is passed to the trained model
5. The model predicts the math score
6. The result is displayed on the interface

---

## Model Details

* Model: Random Forest Regressor
* Problem Type: Regression
* Evaluation Metrics:

  * Mean Squared Error (MSE)
  * R² Score
  * K-Fold Cross Validation

---

## Visualization

* Decision Tree visualization to understand model decision logic
* Feature Importance graph to identify influential features

---

## Deployment

* The application is deployed using Docker on Hugging Face Spaces.
* Live Application: <https://huggingface.co/spaces/jyothi-varshin/Student_Maths_Score_Prediction>

---

## Conclusion
This project demonstrates an end-to-end machine learning pipeline including data preprocessing, model training, evaluation, visualization, and deployment as a web application.
