import openai
import nltk
import pickle
import os

from flask import Flask, request, jsonify, render_template, url_for, redirect
from modules.generative_chatbot.open_ai import chat_with_gpt
from modules.sentiment_analysis.sentiment_analysis import perform_sentiment_analysis
# from pyabsa import AspectTermExtraction as ATEPC

app = Flask(__name__)

# model_to_load = ATEPC.ATEPCModelList.FAST_LCF_ATEPC

# model_to_load.load_state_dict(self=model_to_load, state_dict=torch.load('D:\\Akademik\\Deploy Model\\checkpoints\\fast_lcf_atepc_100.CustomDataset_cdw_apcacc_80.32_apcf1_79.94_atef1_67.85\\fast_lcf_atepc.state_dict'))

# model_to_load.eval()

# Definisikan path absolut ke folder models
models_dir = r"D:\Akademik\Deploy Model\models"
regression_path = os.path.join(models_dir, "regression.pkl")
sentiment_analysis_path = os.path.join(models_dir, "sentiment_analysis.pkl")

# Memuat model dan scaler dari file pickle
with open(regression_path, 'rb') as file:
    loaded_items = pickle.load(file)

# Mengakses model dan scaler yang telah dimuat
model_rf_loaded = loaded_items['model']
scaler_loaded = loaded_items['scaler']

# Load the sentiment analysis model
with open(sentiment_analysis_path, 'rb') as file:
    vectorizer, clf = pickle.load(file)

nltk.download('punkt')

# @app.route("/predict_absa", methods=["POST"])
# def predict():

#     # Get the text from the request
#     data = request.get_json(force=True)
#     text = data["text"]

#     # Predict
#     result = model_to_load.predict(text)

#     return jsonify(result)

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
    
@app.route("/chatbot", methods=["POST"])
def chatbot():
    user_input = request.json['text']
    if user_input.lower() == 'quit':
        return jsonify({'response': 'Goodbye!'})
    else:
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
            return redirect(url_for('dashboard'))
        else:
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route("/dashboard")
def dashboard():
    return render_template("index.html")

@app.route('/onboard')
def onboard():
    return render_template('onboard.html')

@app.route('/pitch')
def pitch():
    return render_template('pitch.html')

@app.route('/project_management')
def project_management():
    return render_template('project_management.html')

if __name__ == "__main__":
    app.run(port=29500, debug=True)