from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return ('Flask is running in my computer! Yaay!')

if __name__ == '__main__':
    app.run(debug=True)
