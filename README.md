# Diabetes Prediction System

## Overview

The Diabetes Prediction System is a web application that uses a Logistic Regression model to predict whether a person is diabetic based on various health parameters. The system leverages a machine learning model trained on a dataset and allows users to input their health data to receive predictions. The predictions and user data are stored in a MongoDB database.

## Project Structure

    Dibeties_Predictor-Machine-Learning-Project-2/
        │
        ├── env/                  
        │
        ├── Dataset/
        |         └──diabetes2.csv
        ├── Model/
        │       ├── StandardScaler.pkl
        │       └── modelForPrediction.pkl
        ├── Notebook/
        │       └── Untitled(2).ipynb
        ├── static/
        │       └── style.css
        ├── templates/
        │        ├── index.html
        │        └── prediction.html
        ├── README.md    
        │
        ├── app.py               
        │
        └── requirements.txt             


## Setup

### Prerequisites

- Python 3.8
- Flask
- Pandas
- NumPy
- Scikit-Learn
- PyMongo
- MongoDB

## Installation
1. **Clone the repository**:
    ```sh
    git clone https://github.com/5PCD3/Face_Detection_Attendence_System.git
    cd Face_Detection_Attendence_System
    ```

2. **Create and activate a virtual environment**:
    ```sh
    python3.8 -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    ```

3. **Install the dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

## Run the application

1. **Start the Flask Application**:
    ```sh
    python app.py
    ```

2. **Access the Application**:
    - Open a web browser and navigate to http://localhost:5000 to access the application.

## How It Works
1. **Data Preparation**:
    - The dataset diabetes2.csv is loaded and preprocessed. Missing values are replaced with the mean of the respective columns.



2. **Model Training**:
    - The data is split into training and testing sets.
    - Features are standardized using StandardScaler.
    - A Logistic Regression model is trained on the standardized training data.
    - The trained model and scaler are saved using pickle.

3. **Web Application**:
   - The Flask application serves a web form where users can input their health parameters.
   - The input data is standardized using the pre-trained scaler.
   - The standardized data is fed into the Logistic Regression model to make predictions.
   - The results and user data are stored in a MongoDB database.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgements
  - The dataset used for training is from Kaggle.
  - The project is built using Flask and Scikit-Learn.



---

This readme provides a clear and structured guide to set up and use of this project. If you have any questions, feedback, or issues, please feel free to contact at [pcdpcdjbx@gmail.com](mailto:pcdpcdjbx@gmail.com) .

