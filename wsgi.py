from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Terceito teste de deploy . . . </br> aa"

if __name__ == "__main__":
    application.run()
