import openai
import nltk
import pickle
import os
import logging
import pandas as pd

from flask import Flask, request, jsonify, render_template, url_for, redirect
from modules.generative_chatbot.open_ai import chat_with_gpt
from modules.sentiment_analysis.sentiment_analysis import perform_sentiment_analysis
from pyabsa import AspectTermExtraction as ATEPC

# Konfigurasi logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

app = Flask(__name__)
openai.api_key = 'sk-proj-WlWxxOwxqT9URBV7XqgCT3BlbkFJ6qm9vDs5stEDDUTQ36OA'

# model_to_load = ATEPC.ATEPCModelList.FAST_LCF_ATEPC

# model_to_load.load_state_dict(self=model_to_load, state_dict=torch.load('D:\\Akademik\\Deploy Model\\checkpoints\\fast_lcf_atepc_100.CustomDataset_cdw_apcacc_80.32_apcf1_79.94_atef1_67.85\\fast_lcf_atepc.state_dict'))

# model_to_load.eval()

# Definisikan path absolut ke folder models
# models_dir = r"D:\Akademik\Deploy Model\models"
# relative path
models_dir = os.path.join(os.getcwd(), "models")
regression_path = os.path.join(models_dir, "regression.pkl")
sentiment_analysis_path = os.path.join(models_dir, "sentiment_analysis.pkl")
effort_estimator_path = "d:\\Akademik\\Deploy Model\\models\\best_svr_model.pkl"

# Memuat model dan scaler dari file pickle
with open(regression_path, 'rb') as file:
    loaded_items = pickle.load(file)

# Mengakses model dan scaler yang telah dimuat
model_rf_loaded = loaded_items['model']
scaler_loaded = loaded_items['scaler']

# Load the sentiment analysis model
with open(sentiment_analysis_path, 'rb') as file:
    vectorizer, clf = pickle.load(file)

with open(effort_estimator_path, 'rb') as file:
    best_model = pickle.load(file)

nltk.download('punkt')

@app.route("/predict_absa", methods=["POST"])
def predict_absa():
    # Load the model
    triplet_extractor = ATEPC.AspectExtractor("multilingual")

    # Get the text from the request
    data = request.get_json(force=True)
    text = data["text"]

    # Predict
    result = triplet_extractor.predict(text, save_result=False)

    return jsonify(result)

# @app.route('/analyze_sentiment', methods=['POST'])
# def analyze_sentiment():
#     if 'file' not in request.files:
#         return jsonify({'error': 'No file part'}), 400
#     file = request.files['file']
#     if file.filename == '':
#         return jsonify({'error': 'No selected file'}), 400
#     if file:
#         content = file.read().decode('utf-8')
#         results = perform_sentiment_analysis(content)
#         return jsonify(results)

@app.route('/effort-estimator', methods=['POST'])
def effort_estimator():
    try:
        data = request.get_json()
        logging.debug("Data diterima: %s", data)  # Logging data untuk memastikan formatnya benar
        
        columns = ['Length', 'Transactions', 'Entities', 'PointsNonAdjust', 'PointsAjust']
        df = pd.DataFrame([data], columns=columns)
        df = df.astype(float)
        logging.debug("DataFrame untuk prediksi: \n%s", df)  # Logging DataFrame

        prediction = best_model.predict(df)[0]
        logging.debug("Prediksi: %s", prediction)  # Logging prediksi
        
        return jsonify({'Prediction': prediction})
    except Exception as e:
        logging.error("Error saat melakukan prediksi: %s", str(e))
        return jsonify({'error': str(e)}), 500
    
@app.route("/chatbot", methods=["POST"])
def chatbot():
    data = request.json
    user_input = data.get('text')
    
    if not user_input:
        return jsonify({'error': 'No text provided'}), 400
    
    if user_input.lower() == 'quit':
        return jsonify({'response': 'Goodbye!'})
    
    try:
        response = chat_with_gpt(user_input)
        return jsonify({'response': response})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@app.route('/predict_regression', methods=['POST'])
def predict():
    data = request.json
    year = data['year']
    proglang = data['programmingLanguage']

    # Load the serialized model based on the programming language
    model_path = os.path.join('models', proglang, f'{proglang}_model.pkl')
    if not os.path.exists(model_path):
        return jsonify({'error': f'Model not found for programming language {proglang}'}), 404

    with open(model_path, 'rb') as f:
        model_info = pickle.load(f)
    model = model_info['model']
    scaler = model_info['scaler']

    # Perform the same preprocessing on input data
    year_scaled = scaler.transform([[year]])
    # Make prediction
    prediction = model.predict(year_scaled)[0]
    return jsonify({'prediction': prediction})


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_id = request.form['user-id']
        password = request.form['password']
        if user_id == 'admin' and password == 'admin':
            return redirect(url_for('index'))
        else:
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route("/index")
def index():
    return render_template("index.html")

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/onboard')
def onboard():
    return render_template('onboard.html')

@app.route('/pitch')
def pitch():
    return render_template('pitch.html')

@app.route('/software_effort_estimator')
def software_effort_estimator():
    return render_template('software_effort_estimator.html')

@app.route('/project_management')
def project_management():
    return render_template('project_management.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)