from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Mahantesh how are you?!,this application is running on version V1.0"

if __name__ == '__main__':
     app.run(host='0.0.0.0',port=8080)
