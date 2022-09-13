from flask import Flask
from flask import request
from flask_cors import CORS
import pymongo

from markupsafe import escape

app = Flask(__name__)


CORS(app, support_credentials=True)

@app.route("/")
def hello_world():
    return "<p>Hello, Ba Adil!</p>"


o = open("myfile.txt", "w")
o.write("ahmed")
o.close()


@app.route("/send", methods = ['GET', 'POST'])
def hello():
    if(request.method == 'POST'):
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["Mywebsite"]
        mycol = mydb["Mywebsite"]
        mydict = request.json
        x = mycol.insert_one(mydict)
    return "True"