import os 
from flask import Flask, send_from_directory
app = Flask(__name__, static_folder='web-app') 

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def web_app(path):
	result = None 
	if path != "" and os.path.exists(app.static_folder + '/' + path):
		result = send_from_directory(app.static_folder , path)
	else:
		result = send_from_directory(app.static_folder , 'index.html')
	return result

if __name__ == "__main__": 
	app.run(host ='0.0.0.0', port = 5001, debug = True) 
