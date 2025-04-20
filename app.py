from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)

# Load the saved model
model = joblib.load('salary_predictor.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        experience = float(request.form['experience'])
        prediction = model.predict(np.array([[experience]]))
        salary = round(prediction[0], 2)
        return render_template('index.html', prediction_text=f'Expected Salary: ₹{salary}')
    except:
        return render_template('index.html', prediction_text='Invalid input! Please enter a number.')

if __name__ == '__main__':
    app.run(debug=True)