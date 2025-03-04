from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
import joblib
import pandas as pd
from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
import joblib
from tensorflow.keras.losses import MeanSquaredError 

app = Flask(__name__)

train_df = pd.read_csv("train.csv")
SEQ_LENGTH=30

model = load_model("inventory_lstm_model.h5", custom_objects={"mse": MeanSquaredError()}) 
model.compile(loss='mse', optimizer='adam', metrics=['mean_absolute_error'])
scaler = joblib.load("scaler.pkl")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    store = data['store']
    item = data['item']
    date = pd.to_datetime(data['date'])

    past_data = train_df[(train_df['store'] == store) & (train_df['item'] == item)].tail(SEQ_LENGTH)

    if len(past_data) < SEQ_LENGTH:
        return jsonify({"error": "Not enough historical data"}), 400

    past_sales = past_data['sales_scaled'].values.reshape(1, SEQ_LENGTH, 1)

    predicted_sales_scaled = model.predict(past_sales)[0][0]
    predicted_sales = scaler.inverse_transform([[predicted_sales_scaled]])[0][0]

    return jsonify({"store": store, "item": item, "date": str(date.date()), "predicted_sales": round(predicted_sales, 2)})

if __name__ == '__main__':
    app.run()