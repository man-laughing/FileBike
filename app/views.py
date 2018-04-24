import os
import urllib
import hashlib
import base64
import time
import ConfigParser
from flask import Flask,render_template,request,send_from_directory,jsonify,url_for,make_response
app = Flask(__name__)
conf = ConfigParser.ConfigParser()
conf.read("config.ini")
mydir = conf.get("storage","dir")
servername = conf.get("web","server_name")
app.config['UPLOAD_FOLDER']   = mydir
app.config['SERVER_NAME']     = servername

def ComputeMD5(msg):
    h = hashlib.md5()
    h.update(msg)
    h.digest()
    result = base64.b64encode(h.digest()).replace('+','-').replace('/','_').replace('=','')
    return result

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/download/<filename>", methods=['GET'])
def download(filename):
    url  = app.send_static_file(filename)
    return url

@app.route("/upload",methods=['POST'])
def upload():
    if os.path.exists(app.config.get('UPLOAD_FOLDER')) == False:os.mkdir(app.config.get('UPLOAD_FOLDER'))
    f = request.files['file']
    fname = f.filename
    f.save(app.config.get('UPLOAD_FOLDER') + "/" +fname)
    if os.path.exists(app.config.get('UPLOAD_FOLDER') + "/" + fname):
        wodeurl = url_for('download',_external=True,filename=fname)
        return jsonify({"url":wodeurl,"code":1,"filename":fname,"filesize":os.path.getsize(app.config.get('UPLOAD_FOLDER') + "/" +fname)})
