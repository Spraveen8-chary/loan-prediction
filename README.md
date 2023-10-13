# Loan Prediction Web Application
This is a simple Flask-based web application for predicting loan approval status based on user inputs. It uses a machine learning model that has been previously trained and saved using pickle. Users can enter various factors related to their loan application, and the application will predict whether their loan will be approved or not.

# Prerequisites
Before running this application, make sure you have the following:

-Python installed on your system (Python 3.x recommended).
-Required libraries and packages installed (Flask, NumPy, pickle, pandas).
-The trained machine learning model (saved as model.pickle).
# Installation and Setup
1. Clone or download this repository to your local machine.

- git clone https://github.com/Spraveen8-chary/loan-prediction.git
  
2. Navigate to the project directory.

- cd loan-prediction-app
  
3. Install the required Python libraries using pip.
   
- pip install flask numpy pandas
- Place the pre-trained machine learning model file (model.pickle) in the project directory.
  
# Usage
### Run the Flask application.

- python app.py
- Open a web browser and go to http://localhost:5000 to access the loan prediction form.

- Fill out the form with the requested information, such as gender, marital status, education, credit history, income details, etc.

- Click the "Predict" button to submit the form.

- The application will process your input data through the machine learning model and display the predicted loan approval status on the webpage.

# Files and Structure
- app.py: The main Flask application file containing the route for handling loan predictions.
- model.pickle: The pre-trained machine learning model used for making predictions.
- templates/index.html: HTML template for rendering the loan prediction form and results.
- README.md: This README file with instructions and information about the application.
# Additional Notes
- The machine learning model used in this application should be trained separately and saved as model.pickle. Ensure that it's a valid model for loan prediction.

- You can modify the HTML template (templates/index.html) to change the appearance and layout of the prediction form.

- This is a simple example of a machine learning-powered web application. In a production environment, you should consider security, error handling, and other best practices.

# Output 
![image](https://github.com/Spraveen8-chary/loan-prediction/assets/108536707/b5e5e27b-167f-4641-9d03-b191b8c2afae)
