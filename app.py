 
from flask import Flask

app = Flask(__name__)
@app.route("/")
def index():
    return "Hello World  第2次更改"
if __name__=="__mian__":
    app.run()

 
