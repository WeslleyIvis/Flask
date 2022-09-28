from flask import Flask, render_template, request
from vsearch import search4letters


app = Flask(__name__)

@app.route('/flask', methods=['POST'])
def inf() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results:'
    results = str(search4letters(phrase, letters))
    return render_template('results.html',
                            the_phrase = phrase,
                            the_letters = letters,
                            the_title = title,
                            the_results = results,
                            )

@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', 
                the_title='Welcome to Search4letters on the web! aaaaaaa')

app.run(debug=True) 