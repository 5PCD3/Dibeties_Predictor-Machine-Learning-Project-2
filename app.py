import pickle
from flask import Flask, request, render_template
from pymongo import MongoClient
from sklearn.preprocessing import StandardScaler

application = Flask(__name__)
app = application

# Load scaler and model
scaler = pickle.load(open('Model/StandardScaler.pkl', 'rb'))
model = pickle.load(open('Model/modelForPrediction.pkl', 'rb'))

# Connect to MongoDB
client = MongoClient("mongodb+srv://pcd:mypassword@cluster0.1oyubnl.mongodb.net/?retryWrites=true&w=majority")
db = client['Dibeties_Prediction_Database']
Dibeties_Parameters = db['Dibeties_Parameters']
Predictions = db['Predictions']

@app.route('/', methods=['GET', 'POST'])
def predict_datapoint():
    result = ''

    if request.method == 'POST':
        try:
            Pregnancies = float(request.form.get("Pregnancies"))
            Glucose = float(request.form.get("Glucose"))
            BloodPressure = float(request.form.get("BloodPressure"))
            SkinThickness = float(request.form.get("SkinThickness"))
            Insulin = float(request.form.get("Insulin"))
            BMI = float(request.form.get("BMI"))
            DiabetesPedigreeFunction = float(request.form.get("DiabetesPedigreeFunction"))
            Age = float(request.form.get("Age"))
          
            new_data_scaled = scaler.transform([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
            result = model.predict(new_data_scaled)

            if result[0] == 1:
                result = 'Diabetic'
            else:
                result = 'Non-Diabetic'

            # Store user-entered data
            user_data = {
                "Pregnancies": Pregnancies,
                "Glucose": Glucose,
                "BloodPressure": BloodPressure,
                "SkinThickness": SkinThickness,
                "Insulin": Insulin,
                "BMI": BMI,
                "DiabetesPedigreeFunction": DiabetesPedigreeFunction,
                "Age": Age,
            }
            Dibeties_Parameters.insert_one(user_data)

            # Store prediction data
            prediction_data = {
                "result": result
            }
            Predictions.insert_one(prediction_data)

            return render_template('prediction.html', result=result)
        except Exception as e:
            print("Error:", e)
            return render_template('index.html')

    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0")
