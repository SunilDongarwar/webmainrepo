from flask import Flask
app = Flask(__name__)
@app.route("/")
def helloworld():
    return "Hello World! Lets Start Contributing Myapp, will it work ???"
if __name__ == "__main__":
    app.run()
