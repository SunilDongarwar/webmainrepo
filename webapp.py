import os

from flask import Flask, render_template

app = Flask(__name__)

# Define the home route
@app.route('/')
def home():
    return render_template('home.html')

# Define the contact route
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Define the about route
@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
