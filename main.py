from flask import Flask, request
from controller.chat import chat_bp
from config import config
from flask_cors import CORS

# template_folder: html模板文件的存放位置
# static_folder: 静态文件存放位置
app = Flask(__name__, template_folder="./templates", static_folder='./templates')
app.register_blueprint(chat_bp, url_prefix='/')
CORS(app, resources=r"/*", supports_credentials=True)


@app.before_request
def before_handler():
    method = request.method
    if method.upper() == 'OPTIONS':
        return "200"


# 解决跨域问题
@app.after_request
def after_handler(resp):
    resp.headers['Access-Control-Allow-Origin'] = "*"
    resp.headers['Access-Control-Allow-Methods'] = "GET,POST,PUT"
    resp.headers['Access-Control-Allow-Headers'] = "*"
    return resp


if __name__ == '__main__':
    app.run('0.0.0.0', config.SERVER_PORT, False)
