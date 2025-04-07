from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "deneme1234 aaa bbb"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
