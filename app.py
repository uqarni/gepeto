from distutils.log import debug
from fileinput import filename
from flask import *
from replit import db
import os



app = Flask(__name__)

@app.route('/')
def main():
  return render_template("index.html")


@app.route('/success', methods=['POST'])
def success():
  if request.method == 'POST':
    f = request.files['file']
    f.save(os.path.join("user-uploads", f.filename))
    return render_template("acknowledge.html", name=f.filename)

@app.route('/submit-form', methods=['POST'])
def submit_form():
    model = request.form['model']
    prompt = request.form['prompt']
    temperature = request.form['temperature']
    max_tokens = request.form['max_tokens']
    top_p = request.form['top_p']
    frequency_penalty = request.form['frequency_penalty']
    presence_penalty = request.form['presence_penalty']
    stop = request.form['stop']
    n = request.form['n']
    echo = request.form.get('echo')

    # Here you can save the form data to a database, write to a file, or do any other processing you need.
    # For example, you can print the data to the console:
    

    return render_template("fine-tune-submitted.html")

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=81, debug=True)
