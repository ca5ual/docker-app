from flask import Flask, request
import datetime
import os

app = Flask(__name__)

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

@app.route("/")
def home():
  return "Backend is running", 200

@app.route("/log", methods=["POST"])
def log():
  content = request.get_json()
  with open(f"{LOG_DIR}/log.txt", "a") as f:
    f.write(f"{datetime.datetime.now()}: {content}\n")
  return {"status": "logged"}, 200

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000)
