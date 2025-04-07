from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "deneme1234 fffaada bbbdd"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)




# Uygulamayı Docker ile çalıştırmak için terminalde sırasıyla şu komutları çalıştır:
# docker build -t flask-deneme .
# docker run -d -p 5050:80 --name flask-test flask-deneme