from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello_world():
    current_year = datetime.now().year
    return render_template('index.html', year=current_year)

@app.route('/about')
def about():
    current_year = datetime.now().year
    return render_template('about.html', year=current_year)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)