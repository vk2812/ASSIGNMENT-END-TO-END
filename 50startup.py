import numpy as np
import pandas as pd
import pickle
import sklearn

from flask import Flask, render_template, request,jasonify

app=Flask (_name_)

@app.route('/')
def home():
 return _render_template('50STARTUP.HTML')


@app.route('/predict', methods=["POST", 'GET'])
def results():

 R&D Spend= float(request.form['R&D Spend'])
 Administration = float(request.form['Administration'])
 Marketing Spend = float(request.form['Marketing Spend'])
 profit = float(request.form['Profit'])
 x = np.array([['R&D Spend', 'Administration', 'Marketing Spend']])
 model = pickle.load(open('model.pkl', 'rb'))
y_prediction = model.predict(X)
return jsonify({'Prediction': float(Y_prediction)})
if __name__ == '__main__':
    app.run(debug=True, port=1234)