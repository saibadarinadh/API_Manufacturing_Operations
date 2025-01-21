from flask import Flask, request, jsonify
import pandas as pd
from model import DowntimePredictor
import os

app = Flask(__name__)
predictor = DowntimePredictor()

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file and file.filename.endswith('.csv'):
        df = pd.read_csv(file)
        df.to_csv('uploaded_data.csv', index=False)
        return jsonify({'message': 'File uploaded successfully', 'rows': len(df)}), 200
    return jsonify({'error': 'Invalid file format'}), 400

@app.route('/train', methods=['POST'])
def train():
    try:
        if not os.path.exists('uploaded_data.csv'):
            return jsonify({'error': 'No data uploaded yet'}), 400
        data = pd.read_csv('uploaded_data.csv')
        metrics = predictor.train(data)
        return jsonify(metrics), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    if 'Temperature' not in data or 'Run_Time' not in data:
        return jsonify({'error': 'Missing required parameters'}), 400
    try:
        prediction = predictor.predict(data['Temperature'], data['Run_Time'])
        return jsonify(prediction), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)