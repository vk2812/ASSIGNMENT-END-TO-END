import numpy as np
import pickle
import pandas as pd
import sklearn

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/')
def Home():
    return render_template('50startup.html')


@app.route('/predict', methods=["POST", 'GET'])
def results():
    RD Spend=float(request.form['RD Spend'])

 RD Spend = float(request.form['RD Spend'])
 Administration = float(request.form['Administration'])
 Marketing Spend = float(request.form['Marketing Spend'])
 Profit = float(request.form['Profit'])
 X = np.array([["RDSpend","Administration","Marketing Spend","Profit "]])
 model = pickle.load(open('50startup.pkl', 'rb'))
 Y_prediction = model.predict(X)

    return jsonify({'Prediction': float(Y_prediction)})


if __name__ == '__main__':
    app.run(debug=True, port=1234)
