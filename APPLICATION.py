from flask import Flask
app = Flask(__name__)

@app.route("/try")
def hello():
    return "Hello World!"

@app.route("/main")
def goodbye():
    return "Hello not World!"	
	
if __name__ == "__main__":
    app.run()

	
	
