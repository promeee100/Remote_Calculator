from flask import Flask, render_template, request, jsonify
import socket

app = Flask(__name__)

def send_to_server(a, b, op):
    HOST = "127.0.0.1"
    PORT = 6000

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    message = f"{a},{b},{op}"
    client_socket.send(message.encode())

    result = client_socket.recv(1024).decode()
    client_socket.close()

    return result

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.json
    a = data["num1"]
    b = data["num2"]
    op = data["op"]

    result = send_to_server(a, b, op)

    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)
