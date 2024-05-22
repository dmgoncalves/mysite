from flask import Flask


app = Flask(__name__)

def get_public_ip():
    response = requests.get("https://api.ipify.org")
    return response

@app.route('/')
def hello_world():  # put application's code here
    return 'hello'

if __name__ == '__main__':

    app.run()
