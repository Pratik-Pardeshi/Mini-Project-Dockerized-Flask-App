from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello():
    return "Hello Pratik here,Welcome to My Dockerized Flask App!"
if __name__ == '__main__':
    app.run(host='0.0.0.0')
