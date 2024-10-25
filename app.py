from flask import Flask, render_template, jsonify
import pandas as pd
import json

app = Flask(__name__)

# Assuming `column_names` is defined in your Jupyter Notebook or can be loaded here
with open('column_names.json', 'r') as f:
    column_names = json.load(f)

@app.route('/')
def home():
    return render_template('index.html', columns=column_names)

@app.route('/get_regions', methods=['GET'])
def get_regions():
    return jsonify(column_names)

if __name__ == '__main__':
    app.run(debug=True)