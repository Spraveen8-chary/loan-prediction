from flask import Flask, render_template, request
import numpy as np
import pickle
import pandas as pd

app = Flask(__name__)

# Load the saved model
with open('model.pickle', 'rb') as f:
    model = pickle.load(f)


@app.route('/',  methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        # Get user inputs from the form
        Gender = int(request.form['Gender'])
        Married = int(request.form['Married'])
        Dependents = int(request.form['Dependents'])
        Education = int(request.form['Education'])
        Self_Employed = int(request.form['Self_Employed'])
        Credit_History = int(request.form['Credit_History'])
        Property_Area = int(request.form['Property_Area'])
        ApplicantIncomeLog = (float(request.form['ApplicantIncomeLog']))
        CoApplicantIncomeLog =(float(request.form['CoApplicantIncomeLog']))
        LoanAmountLog = (float(request.form['LoanAmountLog']))
        Loan_Amount_Term_Log =(float(request.form['Loan_Amount_Term_Log']))

        Total_Income_Log = ApplicantIncomeLog + CoApplicantIncomeLog
        ApplicantIncomeLog = np.log(ApplicantIncomeLog)
        LoanAmountLog = np.log(LoanAmountLog)
        Loan_Amount_Term_Log = np.log(Loan_Amount_Term_Log)
        Total_Income_Log = np.log(Total_Income_Log)
        # Create a feature vector
        input_data = np.array([[
            Gender, Married, Dependents, Education, Self_Employed,
            Credit_History, Property_Area, ApplicantIncomeLog,
            LoanAmountLog, Loan_Amount_Term_Log, Total_Income_Log
        ]])

        # Make a prediction using the model
        prediction = model.predict(pd.DataFrame(input_data))
        predicted_labels = ['Approved' if prediction == 1 else 'Not Approved' for prediction in prediction]


        # Render the prediction result in a simple HTML page
        
        return render_template('index.html',predicted_labels = predicted_labels[0])
    return render_template('index.html',predicted_labels = None)

if __name__ == '__main__':
    app.run(debug=True)
