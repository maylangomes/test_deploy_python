from flask import Blueprint, jsonify, render_template
import pandas as pd
import numpy as np

bp = Blueprint('routes', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/data')
def data():
    df = pd.DataFrame({
        'x': np.arange(1, 101),
        'y': np.random.randint(1, 100, size=100)
    })
    data = {
        'labels': df['x'].tolist(),
        'values': df['y'].tolist()
    }
    return jsonify(data)
