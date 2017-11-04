from flask import Flask, jsonify, request
from printAddress import *

app = Flask(__name__)
languages = [{'name':'JS'}, {'name':'Ruby'}]

@app.route('/address', methods=['POST'])
def getAddress():
	address=request.json['path']
	print (address)
	
	return jsonify({'message':'It works!'})

@app.route('/lang', methods=['GET'])
def getLang():
	return jsonify({'languages': languages })

@app.route('/lang/<name>', methods=['GET'])
def getLanguage(name):
	lang = [language for language in languages if language['name']==name]
	return jsonify({'language': lang})

@app.route('/lang', methods=['POST'])
def addLanguage():
	address=request.json['name']
	print (address)
	return jsonify({'languages':languages})
	

if __name__ == '__main__':
	app.run()
