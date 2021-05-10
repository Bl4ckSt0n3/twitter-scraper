from flask import Flask, render_template, jsonify


# please retype your path
import sys  
sys.path.append("/home/ubuntu/Documents/documents/twitter_scraper/t_api/algorithm") 

from alg import file_op, search_by_expression
search_by_expression() # run out only 1 time


data = file_op()
app = Flask(__name__, template_folder='templates')

@app.route('/index')
def index():
	jsondata = data
	return jsonify(jsondata)

"""
@app.route('/index')
def index():

	return render_template("index.html", data=data.tweets())
	
"""
