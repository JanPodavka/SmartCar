from flask import Flask, request

app = Flask(__name__)


# Define a route to receive control commands
@app.route('/control', methods=['POST'])
def control_car():
    command = request.form.get('command')
    print("Received command:", command)

    return 'OK', 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
