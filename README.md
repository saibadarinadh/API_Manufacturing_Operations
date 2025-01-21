# Manufacturing Operations Predictive API

A Flask-based RESTful API for predicting machine downtime in manufacturing operations using machine learning. This API provides endpoints for data upload, model training, and making predictions based on temperature and runtime parameters.

## Features

- Upload manufacturing data via CSV files
- Train machine learning model on uploaded data
- Make downtime predictions with confidence scores
- Simple and intuitive REST API endpoints

## Installation

1. Clone the repository:
```bash
git clone https://github.com/saibadarinadh/API_Manufacturing_Operations.git
cd API_Manufacturing_Operations
```

2. Create and activate a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

## API Endpoints and Usage

### 1. Upload Data (POST /upload)
Upload your manufacturing data CSV file through this endpoint.

![Upload Endpoint](https://raw.githubusercontent.com/saibadarinadh/API_Manufacturing_Operations/main/upload.png)

Example Response:
```json
{
    "message": "File uploaded successfully",
    "rows": 100
}
```

### 2. Train Model (POST /train)
Train the model using the uploaded dataset.

![Train Endpoint](https://raw.githubusercontent.com/saibadarinadh/API_Manufacturing_Operations/main/train.png)

Example Response:
```json
{
    "accuracy": 0.85,
    "f1_score": 0.83
}
```

### 3. Make Prediction (POST /predict)
Get downtime predictions for specific parameters.

![Predict Endpoint](https://raw.githubusercontent.com/saibadarinadh/API_Manufacturing_Operations/main/predict.png)

Example Request:
```json
{
    "Temperature": 85,
    "Run_Time": 180
}
```

Example Response:
```json
{
    "Downtime": "Yes",
    "Confidence": 0.92
}
```

## Project Structure

```
API_Manufacturing_Operations/
├── app.py              # Main Flask application
├── model.py            # Machine learning model implementation
├── data_generator.py   # Script to generate sample data
├── uploaded_data.csv   # Sample dataset
├── *.png              # Screenshot demonstrations
└── requirements.txt    # Project dependencies
```

## Dataset Format

The API expects CSV files with the following columns:
- Machine_ID: Unique identifier for each machine
- Temperature: Operating temperature
- Run_Time: Duration of operation
- Downtime_Flag: Binary indicator (0/1) for downtime events

Example:
```csv
Machine_ID,Temperature,Run_Time,Downtime_Flag
1,75.5,120.3,0
2,88.2,195.7,1
```

## Sample Data Generation

To generate sample data for testing:
```bash
python data_generator.py
```

This will create a `uploaded_data.csv` file with synthetic manufacturing data.

## Requirements

- Python 3.7+
- Flask
- pandas
- scikit-learn
- Additional dependencies are listed in `requirements.txt`

## Error Handling

The API includes error handling for:
- Missing files in upload requests
- Invalid file formats
- Missing parameters in prediction requests
- Model training errors

