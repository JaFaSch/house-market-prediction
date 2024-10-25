from flask import Flask, render_template, jsonify
import pandas as pd

app = Flask(__name__)

# Assuming `column_names` is defined in your Jupyter Notebook or can be loaded here
column_names = sorted(["region1", "region2", "region3"])  # Replace with your actual column_names list

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_regions', methods=['GET'])
def get_regions():
    return jsonify(column_names)

if __name__ == '__main__':
    app.run(debug=True)