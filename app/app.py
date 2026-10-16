import os
import subprocess

from flask import Flask, request

app = Flask(__name__)

@app.get("/")
def home():
    return {"message": "DevSecOps lab is running"}

@app.get("/search")
def search():
    query = request.args.get("q", "")
    return {"query": query}

@app.get("/health")
def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", "5000")),
        debug=False,
    )
