from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "You application has been deployed on GKE with version 1.0"

if __name__ == '__main__':
     app.run(host='0.0.0.0',port=8080)

# def test_function(request):
#     return "Hello from Cloud Function!"
