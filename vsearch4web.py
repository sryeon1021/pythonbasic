from flask import Flask, render_template, request
from vsearch2 import search4letters

app= Flask(__name__)

def log_request(req:'flask_request', res:str) ->None:
    with open('vsearch2.log', 'a') as log:
        print(req, res,file=log)

@app.route('/search4',methods= ['POST'])
def do_search() ->'html':
    phrase= request.form['phrase']
    letters= request.form['letters']
    title='here are your results:'
    results=str(search4letters(phrase, letters))
    return render_template('results.html',
                            the_phrase=phrase,
                            the_letters=letters,
                            the_title=title,
                            the_results=results,)

@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                            the_title='Welcome to search4letters on the web!')

@app.route('/viewlog')
def view_the_log() -> 'html':
    '''display the contents of the log fole as a HTML table'''
    contents=[]
    with open ('vsearch.log') as log:
        contents=log.read()
    return contents

if __name__ == '__main__':
    app.run(debug=True)