import boto3
import uuid

from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy

ALLOWED_EXTENSIONS = {'txt'}
def allowed_file(filename):
  return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS
  
db = SQLAlchemy()

class File(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  original_filename = db.Column(db.String(100))
  filename = db.Column(db.String(100))
  bucket = db.Column(db.String(100))
  region = db.Column(db.String(100))
  

def create_app():
  app = Flask(__name__)
  app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
  
  db.init_app(app)
  
  @app.route('/', methods = ['GET', 'POST'])
  def index():
    if request.method == "POST": 
      uploaded_file = request.files["file-to-save"]
      if not allowed_file(uploaded_file.filename):
        return "FILE NOT ALLOWED! ONLY .TXT ALLOWED"

      new_filename = uuid.uuid4().hex + uploaded_file.filname.rsplit('.',1)[1].lower()
      bucket_name = "gepeto"
      s3 = boto3.resource("s3")
      s3.Bucket(bucket_name).upload_fileobj(uploaded_file, new_filename)
      return redirect.url_for("index")
      
    files = File.query.all()
    return render_template('index.html', files = files)

  return app
# def index():
#   return render_template('index.html')


# app.run(host='0.0.0.0', port=81)
