# Inventory-Prediction-Program (LSTM + Flask) 
This project provides an **Inventory Prediction API** that forecasts future sales of a product in a store using a **Long Short-Term Memory (LSTM) model** trained on historical sales data.  

###Tech Stack: 
- Python
- TensorFlow
- Flask
- Pandas
- NumPy
- Matplotlib
    
###Features:
- Predicts future sales based on **store, item, and date**  
- Uses **LSTM deep learning model** for accurate time-series forecasting  
- Exposes a **REST API** endpoint (`/predict`)  
- Returns **numerical predictions** and **graph visualizations**  
- Deployable in **Google Colab** using `ngrok`

## 🚀 **Installation & Setup**  

### 1️⃣ **Clone the Repository**  
`git clone https://github.com/Anuradha-Ranathunga/Inventory-Prediction-Program
cd Inventory-Prediction-Program`

###2️⃣ Install Dependencies
`pip install flask flask-ngrok tensorflow pandas numpy scikit-learn joblib matplotlib`

###3️⃣ Run the Flask Server
`python app.py`

##🌍 Running on Google Colab
Since Google Colab doesn’t support local servers, use ngrok to expose the API:
`!pip install flask-ngrok
from flask_ngrok import run_with_ngrok
run_with_ngrok(app)
app.run()`

After running, you'll get a URL like: `Running on https://xyz.ngrok.io`
Use this ngrok URL to test the API

##📡 API Endpoints






