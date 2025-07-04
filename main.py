from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Mahantesh how are you?!,your  application is running successfully now"

if __name__ == '__main__':
     app.run(host='0.0.0.0',port=8080)

# def test_function(request):
#     return "Hello from Cloud Function!"
