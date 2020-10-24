import os
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def fib():
	prox = 1
   	ant = 0
   	res = "0, "
   	for i in range(50):
		tmp = prox
		prox = prox + ant
		ant = tmp
		if i < 49:
			res += str(prox) + ", "
		else:
			res += str(prox) + "."
   	return res

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)