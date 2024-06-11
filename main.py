from flask import Flask, jsonify, render_template
from flask_cors import CORS
import pandas as pd
import numpy as np

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def data():
    # Generating random data
    df = pd.DataFrame({
        'x': np.arange(1, 101),
        'y': np.random.randint(1, 100, size=100)
    })
    data = {
        'labels': df['x'].tolist(),
        'values': df['y'].tolist()
    }
    return jsonify(data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
