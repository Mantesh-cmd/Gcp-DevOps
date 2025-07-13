from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Your application has been deploye with version 3.0"

if __name__ == '__main__':
     app.run(host='0.0.0.0',port=8080)

# def test_function(request):
#     return "Hello from Cloud Function!"
