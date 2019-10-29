from flask import Flask
app = Flask(__name__, static_folder='./Web')

@app.route("/")
def index():
    return app.send_static_file("Index.html")

@app.route("/pathtest")
def pathtest():
    return "path test successful"

if __name__ == "__main__":
    app.run()