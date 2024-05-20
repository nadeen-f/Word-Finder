from flask import Flask, render_template, request
from dictionary import make_word_array

app = Flask(__name__)

@app.route('/')
def welcome_page():
    return render_template("index.html")

@app.route('/word_list', methods=['POST'])
def results_page():
    letters = request.form['letter_field']
    return generate_words(letters)

def generate_words (letters):
    words_array = make_word_array(letters.lower())
    return render_template('index.html', 
                           words_array = words_array,
                           letters = letters)
