from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return "Hola Mundo - Desarrollado por Maxwell Aybar | DevOps CI/CD"

@app.route("/api/status")
def status():
    return jsonify({"status": "active", "service": "DevOps-API"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
