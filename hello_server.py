from flask import Flask
app = Flask(__name__)

@app.route("/<personName>")
def hello(personName):
    return "Hello " + personName

if __name__ == "__main__":
    app.run()