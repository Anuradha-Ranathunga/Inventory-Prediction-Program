# Inventory-Prediction-Program (LSTM + Flask) 
This project provides an **Inventory Prediction API** that forecasts future sales of a product in a store using a **Long Short-Term Memory (LSTM) model** trained on historical sales data.  

### Tech Stack: 
- Python
- TensorFlow
- Flask
- Pandas
- NumPy
- Matplotlib
    
### Features:
- Predicts future sales based on **store, item, and date**  
- Uses **LSTM deep learning model** for accurate time-series forecasting  
- Exposes a **REST API** endpoint (`/predict`)  
- Returns **numerical predictions** and **graph visualizations**  

## 🚀 **Installation & Setup**  

### 1️⃣ **Clone the Repository**  
`git clone https://github.com/Anuradha-Ranathunga/Inventory-Prediction-Program
cd Inventory-Prediction-Program`

### 2️⃣ Install Dependencies
`pip install flask flask-ngrok tensorflow pandas numpy scikit-learn joblib matplotlib`

### 3️⃣ Run the Flask Server
`python app.py`

## 📡 API Endpoints

### 🔹 Predict Sales
**Request (POST)**
**Endpoint:** `/predict`
**Content-Type:** `application/json`
**Body Parameters:**
`{
    "store": 1,
    "item": 1,
    "date": "2018-01-01"
}`

**Response**
`{
    "store": 1,
    "item": 1,
    "date": "2018-01-01",
    "predicted_sales": 20.45,
    "plot": "data:image/png;base64,..."
}`

- `predicted_sales`: Forecasted sales for the given date
- `plot`: Base64-encoded graph showing historical data + prediction

## 📊 Visualizing the Prediction Graph
To view the generated graph, run this Python script:

`import requests
from PIL import Image
import base64
import io
url = "https://xyz.ngrok.io/predict"  # Replace with your API URL
data = {"store": 1, "item": 1, "date": "2018-01-01"}
response = requests.post(url, json=data).json()
plot_data = base64.b64decode(response["plot"].split(",")[1]) ## Decode and display the image
img = Image.open(io.BytesIO(plot_data))
img.show()`
This will display a plot of past sales with the forecasted point.

## ⚡ Project Structure

📂 inventory-prediction-api
│── 📄 app.py               `# Flask API`
│── 📄 inventory_lstm_model.h5  `# Trained LSTM model`
│── 📄 scaler.pkl           `# Scaler for data normalization`
│── 📄 train.csv            `# Training data`
│── 📄 README.md            `# Project documentation`


## 🤖 Future Improvements
✅ Add multi-day predictions
✅ Deploy on AWS/GCP for real-world use
✅ Optimize LSTM model with hyperparameter tuning

## 📜 License
This project is licensed under the MIT License.













