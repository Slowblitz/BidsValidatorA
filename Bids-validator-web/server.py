
from flask import Flask, jsonify, render_template, request
import os
import logging
import ast
app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/_getData')
def get_names():
	try :
		 phrase='liste des paths donnes :'
		 a = request.args.get('a')
		 testarray = ast.literal_eval(a)
		 return jsonify(result=phrase + a)
	except Exception,e:
    	 return (str(e))


@app.route('/end_stu_live_session',methods=["GET", "POST"])
def end_stu_live_session():
    if request.method == 'POST':
        data = request.json
       
        return jsonify(data)
    return render_template("home.html")

if __name__ == "__main__":
    app.run()

