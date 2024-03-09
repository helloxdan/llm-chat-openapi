from flask import Blueprint, render_template, request
from service import chat
from config import config

chat_bp = Blueprint('chat', __name__)


@chat_bp.get("/")
def get_index():
    title = "聊天机器人"
    context = {
        "title": title,
        "host": config.HOST,
        "port": config.SERVER_PORT
    }
    return render_template("index.html", context=context)


# 接收聊天内容
@chat_bp.post("/dialog")
def send_chat():
    return chat.send_chat(request.json)
