from flask import Flask, request, jsonify
import pandas as pd
import yfinance as yf
from ta.volatility import BollingerBands
from ta.trend import MACD, EMAIndicator, SMAIndicator
from ta.momentum import RSIIndicator
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from xgboost import XGBRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.metrics import r2_score, mean_absolute_error

app = Flask(__name__)

@app.route('/visualize', methods=['GET'])
def visualize():
    stock_symbol = request.args.get('stock_symbol', default='SPY', type=str)
    duration = request.args.get('duration', default=3000, type=int)
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    
    # Download data
    data = download_data(stock_symbol, start_date, end_date)
    
    # Visualize data
    # Implement your visualization code here
    return jsonify({'message': 'Visualization data here'})

@app.route('/recent_data', methods=['GET'])
def recent_data():
    stock_symbol = request.args.get('stock_symbol', default='SPY', type=str)
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    
    # Download data
    data = download_data(stock_symbol, start_date, end_date)
    
    # Return recent data
    return jsonify(data.tail(10).to_dict())

@app.route('/predict', methods=['POST'])
def predict():
    stock_symbol = request.json.get('stock_symbol', 'SPY')
    num_days = request.json.get('num_days', 5)
    model_type = request.json.get('model_type', 'LinearRegression')
    start_date = request.json.get('start_date')
    end_date = request.json.get('end_date')
    
    # Download data
    data = download_data(stock_symbol, start_date, end_date)
    
    # Predict using the specified model
    model = get_model(model_type)
    forecast = make_prediction(data, model, num_days)
    
    return jsonify({'forecast': forecast})

def download_data(stock_symbol, start_date, end_date):
    # Download data using yfinance
    df = yf.download(stock_symbol, start=start_date, end=end_date, progress=False)
    return df.to_dict()

def get_model(model_type):
    # Return the selected model
    if model_type == 'LinearRegression':
        return LinearRegression()
    elif model_type == 'RandomForestRegressor':
        return RandomForestRegressor()
    elif model_type == 'ExtraTreesRegressor':
        return ExtraTreesRegressor()
    elif model_type == 'KNeighborsRegressor':
        return KNeighborsRegressor()
    elif model_type == 'XGBRegressor':
        return XGBRegressor()

def make_prediction(data, model, num_days):
    # Perform prediction
    # Implement your prediction logic here
    return ['day 1 forecast', 'day 2 forecast', ...]

if __name__ == '__main__':
    app.run(debug=True)