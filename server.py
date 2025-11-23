import socket

HOST = '127.0.0.1'
PORT = 6000


def calculate(x, y, opr):
    try:
        a = int(x)
        b = int(y)

        if opr == '+':
            return str(a + b)
        elif opr == '-':
            return str(a - b)
        elif opr == '*':
            return str(a * b)
        elif opr == '/':
            if b == 0:
                return "Error: Division by zero"
            return str(a / b)
        elif opr == '%':
            if b == 0:
                return "Error: Modulo by zero"
            return str(a % b)
        else:
            return "Invalid Operator"
    except:
        return "Invalid Input"


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)

print(f"[SERVER RUNNING] Listening on {HOST}:{PORT}")

while True:
    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")

    data = conn.recv(1024).decode()

    if not data:
        break


    raw_num1, raw_num2, raw_op = data.split(',')

    result = calculate(raw_num1, raw_num2, raw_op)

    conn.send(result.encode())
    conn.close()
