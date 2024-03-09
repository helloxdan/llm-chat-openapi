import os
import dotenv

dotenv.load_dotenv()
# 项目启动的端口
SERVER_PORT = os.getenv("SERVER_PORT")
# ChatGPT的api key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# 前端请求的host
HOST = os.getenv("HOST")
