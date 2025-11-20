from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Docker!"

if __name__ == "__main__":
    # listen on all interfaces so Docker can forward the port
    app.run(host="0.0.0.0", port=5000)