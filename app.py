from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

app = Flask(__name__)

# Load model
print("Loading model...")
model = joblib.load('best_model.pkl')
X_train = pd.read_csv('X_train.csv')
feature_names = X_train.columns.tolist()
print(f"✓ Model loaded | Features: {len(feature_names)}")

# ─────────────────────────────────────────────
# ROUTES
# ─────────────────────────────────────────────

@app.route('/')
def home():
    return render_template('index.html', feature_names=feature_names)


@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No input data provided'}), 400

        features = [float(data.get(feat, 0)) for feat in feature_names]
        features_array = np.array(features).reshape(1, -1)

        prediction  = int(model.predict(features_array)[0])
        probability = model.predict_proba(features_array)[0]
        label       = 'Phishing' if prediction == 1 else 'Legitimate'
        confidence  = float(max(probability))

        return jsonify({
            'status':          'success',
            'prediction':      prediction,
            'label':           label,
            'confidence':      round(confidence * 100, 2),
            'prob_legitimate': round(float(probability[0]) * 100, 2),
            'prob_phishing':   round(float(probability[1]) * 100, 2)
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/health', methods=['GET'])
def health():
    return jsonify({
        'status':   'healthy',
        'model':    'Random Forest - Phishing Detector',
        'accuracy': '95.58%',
        'features': len(feature_names)
    })


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
