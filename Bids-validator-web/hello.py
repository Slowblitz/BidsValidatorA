
from flask import Flask, jsonify, render_template, request
app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/_getData')
def get_names():
	try :
		 phrase='liste des paths donnes :'
		 a = request.args.get('a')

		 return jsonify(result=phrase +a )
	except Exception,e:
    	 return (str(e))


if __name__ == "__main__":
    app.run()

