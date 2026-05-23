from flask import Flask, request, jsonify, make_response
import joblib
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

app = Flask(__name__)

print("Loading model...")
model = joblib.load('best_model.pkl')
X_train = pd.read_csv('X_train.csv')
feature_names = X_train.columns.tolist()
print(f"Model loaded! Features: {len(feature_names)}")

@app.route('/')
def home():
    html = """<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Phishing Website Detector</title>
<style>
body{margin:0;padding:0;font-family:Arial,sans-serif;background-color:#0f172a;color:#e2e8f0}
.header{background:linear-gradient(135deg,#1e3a8a,#3b82f6);padding:30px;text-align:center}
.header h1{color:white;font-size:28px;margin:0}
.header p{color:#bfdbfe;margin-top:8px;font-size:14px}
.container{max-width:800px;margin:20px auto;padding:0 20px}
.card{background:#1e293b;border-radius:10px;padding:20px;margin-bottom:15px;border:1px solid #334155}
.card h2{color:#60a5fa;font-size:16px;margin-top:0;margin-bottom:15px}
.stats{display:grid;grid-template-columns:1fr 1fr 1fr 1fr;gap:10px;margin-bottom:10px}
.stat{background:#0f172a;border-radius:8px;padding:10px;text-align:center;border:1px solid #334155}
.stat-num{color:#3b82f6;font-size:20px;font-weight:bold}
.stat-lbl{color:#64748b;font-size:11px;margin-top:3px}
.grid{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-bottom:15px}
.field label{display:block;color:#94a3b8;font-size:12px;margin-bottom:3px}
.field input{width:100%;padding:8px;background:#0f172a;border:1px solid #475569;border-radius:6px;color:#e2e8f0;font-size:14px}
.buttons{margin-top:10px}
.btn{padding:10px 18px;border:none;border-radius:6px;font-size:14px;font-weight:bold;cursor:pointer;margin-right:8px;margin-bottom:8px}
.btn-blue{background:#3b82f6;color:white}
.btn-red{background:#ef4444;color:white}
.btn-green{background:#10b981;color:white}
#loading{display:none;color:#60a5fa;margin-top:10px;font-size:14px}
#resultBox{display:none;margin-top:15px}
.phishing{background:#450a0a;border:2px solid #ef4444;border-radius:10px;padding:15px;text-align:center}
.legitimate{background:#052e16;border:2px solid #22c55e;border-radius:10px;padding:15px;text-align:center}
.result-title{font-size:24px;font-weight:bold;margin-bottom:5px}
.phishing .result-title{color:#ef4444}
.legitimate .result-title{color:#22c55e}
.result-conf{color:#94a3b8;font-size:14px;margin-bottom:10px}
.prob-row{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:10px}
.prob-box{background:#0f172a;border-radius:6px;padding:10px;text-align:center}
.prob-lbl{color:#94a3b8;font-size:12px}
.prob-val{font-size:18px;font-weight:bold;margin-top:3px}
.prob-bar-bg{background:#1e293b;height:6px;border-radius:3px;margin-top:6px}
.prob-bar-fill{height:6px;border-radius:3px}
.code-box{background:#0f172a;border:1px solid #334155;border-radius:6px;padding:12px;font-family:monospace;font-size:12px;color:#a5f3fc;line-height:1.8}
footer{text-align:center;padding:15px;color:#475569;font-size:12px}
</style>
</head>
<body>

<div class="header">
  <h1>&#x1F6E1; Phishing Website Detector</h1>
  <p>ML-powered detection using Random Forest &nbsp;|&nbsp; Built by Dhanshree Sarang &nbsp;|&nbsp; Code-B Solutions Internship</p>
</div>

<div class="container">

  <div class="card">
    <h2>&#x1F4CA; Model Performance</h2>
    <div class="stats">
      <div class="stat"><div class="stat-num">95.58%</div><div class="stat-lbl">Accuracy</div></div>
      <div class="stat"><div class="stat-num">99.12%</div><div class="stat-lbl">ROC-AUC</div></div>
      <div class="stat"><div class="stat-num">11,430</div><div class="stat-lbl">Samples</div></div>
      <div class="stat"><div class="stat-num">7</div><div class="stat-lbl">Models</div></div>
    </div>
  </div>

  <div class="card">
    <h2>&#x1F50D; Check a Website</h2>
    <p style="color:#94a3b8;font-size:13px;margin-bottom:15px">Enter website features to predict if it is Phishing or Legitimate.</p>
    <div class="grid">
      <div class="field"><label>URL Length</label><input type="number" id="f1" value="75"></div>
      <div class="field"><label>Hostname Length</label><input type="number" id="f2" value="20"></div>
      <div class="field"><label>Number of Dots</label><input type="number" id="f3" value="3"></div>
      <div class="field"><label>Number of Hyphens</label><input type="number" id="f4" value="0"></div>
      <div class="field"><label>Has HTTPS (1=Yes, 0=No)</label><input type="number" id="f5" value="1"></div>
      <div class="field"><label>Google Index (1=Yes, 0=No)</label><input type="number" id="f6" value="1"></div>
      <div class="field"><label>Page Rank (0-10)</label><input type="number" id="f7" value="4"></div>
      <div class="field"><label>Web Traffic</label><input type="number" id="f8" value="3"></div>
      <div class="field"><label>IP in URL (1=Yes, 0=No)</label><input type="number" id="f9" value="0"></div>
      <div class="field"><label>Number of Hyperlinks</label><input type="number" id="f10" value="50"></div>
      <div class="field"><label>DNS Record (1=Yes, 0=No)</label><input type="number" id="f11" value="1"></div>
      <div class="field"><label>Phishing Hints</label><input type="number" id="f12" value="0"></div>
    </div>
    <div class="buttons">
      <button class="btn btn-blue" onclick="predict()">Predict</button>
      <button class="btn btn-red" onclick="loadPhishing()">Load Phishing Sample</button>
      <button class="btn btn-green" onclick="loadLegit()">Load Legit Sample</button>
    </div>
    <div id="loading">Analyzing website...</div>
    <div id="resultBox">
      <div id="resultCard">
        <div id="resultTitle" class="result-title"></div>
        <div id="resultConf" class="result-conf"></div>
        <div class="prob-row">
          <div class="prob-box">
            <div class="prob-lbl">Legitimate</div>
            <div class="prob-val" id="pLegit" style="color:#22c55e"></div>
            <div class="prob-bar-bg"><div class="prob-bar-fill" id="bLegit" style="background:#22c55e;width:0%"></div></div>
          </div>
          <div class="prob-box">
            <div class="prob-lbl">Phishing</div>
            <div class="prob-val" id="pPhish" style="color:#ef4444"></div>
            <div class="prob-bar-bg"><div class="prob-bar-fill" id="bPhish" style="background:#ef4444;width:0%"></div></div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <div class="card">
    <h2>API Endpoints</h2>
    <div class="code-box">
      GET &nbsp;/health &nbsp; - Health check<br>
      POST /predict &nbsp;- Get prediction
    </div>
  </div>

</div>
<footer>Built by <strong>Dhanshree Sarang</strong> | Data Science Intern at Code-B Solutions | Random Forest | 95.58% Accuracy</footer>

<script>
var fields = {
  length_url:'f1', length_hostname:'f2', nb_dots:'f3', nb_hyphens:'f4',
  https_token:'f5', google_index:'f6', page_rank:'f7', web_traffic:'f8',
  ip:'f9', nb_hyperlinks:'f10', dns_record:'f11', phish_hints:'f12'
};
function getData(){
  var d={};
  for(var k in fields){ d[k]=parseFloat(document.getElementById(fields[k]).value)||0; }
  return d;
}
function predict(){
  document.getElementById('loading').style.display='block';
  document.getElementById('resultBox').style.display='none';
  fetch('/predict',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(getData())})
  .then(function(r){return r.json();})
  .then(function(d){
    document.getElementById('loading').style.display='none';
    var isP = d.label==='Phishing';
    var card = document.getElementById('resultCard');
    card.className = isP ? 'phishing' : 'legitimate';
    document.getElementById('resultTitle').textContent = isP ? 'PHISHING DETECTED!' : 'LEGITIMATE WEBSITE';
    document.getElementById('resultConf').textContent = 'Confidence: ' + d.confidence + '%';
    document.getElementById('pLegit').textContent = d.prob_legitimate + '%';
    document.getElementById('pPhish').textContent = d.prob_phishing + '%';
    document.getElementById('bLegit').style.width = d.prob_legitimate + '%';
    document.getElementById('bPhish').style.width = d.prob_phishing + '%';
    document.getElementById('resultBox').style.display='block';
  })
  .catch(function(e){ alert('Error: '+e.message); document.getElementById('loading').style.display='none'; });
}
function loadPhishing(){
  document.getElementById('f1').value=150; document.getElementById('f2').value=40;
  document.getElementById('f3').value=8;   document.getElementById('f4').value=5;
  document.getElementById('f5').value=0;   document.getElementById('f6').value=0;
  document.getElementById('f7').value=0;   document.getElementById('f8').value=0;
  document.getElementById('f9').value=1;   document.getElementById('f10').value=5;
  document.getElementById('f11').value=0;  document.getElementById('f12').value=4;
}
function loadLegit(){
  document.getElementById('f1').value=30;  document.getElementById('f2').value=10;
  document.getElementById('f3').value=2;   document.getElementById('f4').value=0;
  document.getElementById('f5').value=1;   document.getElementById('f6').value=1;
  document.getElementById('f7').value=7;   document.getElementById('f8').value=8;
  document.getElementById('f9').value=0;   document.getElementById('f10').value=80;
  document.getElementById('f11').value=1;  document.getElementById('f12').value=0;
}
</script>
</body>
</html>"""
    response = make_response(html)
    response.headers['Content-Type'] = 'text/html; charset=utf-8'
    return response

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No input data'}), 400
        features = [float(data.get(feat, 0)) for feat in feature_names]
        arr = np.array(features).reshape(1, -1)
        prediction = int(model.predict(arr)[0])
        probability = model.predict_proba(arr)[0]
        label = 'Phishing' if prediction == 1 else 'Legitimate'
        return jsonify({
            'status': 'success',
            'prediction': prediction,
            'label': label,
            'confidence': round(float(max(probability)) * 100, 2),
            'prob_legitimate': round(float(probability[0]) * 100, 2),
            'prob_phishing': round(float(probability[1]) * 100, 2)
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy', 'model': 'Random Forest', 'accuracy': '95.58%'})

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
