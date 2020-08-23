from flask import Flask, request
from cat_detector import cat_detector_bp
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

app.register_blueprint(cat_detector_bp, url_prefix='/cat')

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/detector/cats/', methods=['GET', 'POST'])
def cats():
    if request.method == 'POST':
        name = request.form['imageName']
        file = request.files['image']
        return name
    else:
        return 'Hello'


if __name__ == '__main__':
    app.run()
