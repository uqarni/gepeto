from distutils.log import debug
from fileinput import filename
from flask import *
from replit import db
import uuid
import os

app = Flask(__name__)


@app.route('/')
def main():
  return render_template("index.html")


@app.route('/describe-file', methods=['POST'])
def describefile():
  if request.method == 'POST':
    f = request.files['file']
    f.save(os.path.join("user-uploads", f.filename))
    files = os.listdir("user-uploads")
    return render_template("j-describe-file.html",
                           files=files,
                           name=f.filename)


@app.route('/fine-tuner', methods=['POST'])
def finetuner():
  from python.model_functions import raw_pr
  
  filename = request.form["filename"]
  description = request.form["description"]
  cycles = request.form["cycles"]
  new_id = uuid.uuid4().hex
  
  db["pr-"+new_id] = {
    "filename": filename,
    "description": description,
    "cycles": cycles,
    "file-type": filename.rsplit(".",1)[1],
    "prompt-response-docs": {}
  }
  file_path = "user-uploads/"+filename
  
  with open(file_path, "r") as f:
    text = f.read()
  
  cleansed = raw_pr(file = text, topic = description, cycles = cycles)
  return render_template('k-fine-tuner.html')




if __name__ == '__main__':
  app.run(host='0.0.0.0', port=81, debug=True)
