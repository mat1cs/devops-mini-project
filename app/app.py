from flask import Flask, jsonify, request
from config import Config
from database import Database

config = Config()
db = Database(config)

db.connect()
db.create_table()

app = Flask(__name__)

@app.route("/")
def get_messages():
    messages = db.get_messages()
    return jsonify(messages)

@app.route("/add", methods=["POST"])
def add_message():
    data = request.get_json()
    content = data.get("content")
    db.insert_message(content)
    return {"status": "success"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=config.app_port)