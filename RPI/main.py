from flask import Flask, request

app = Flask(__name__)


@app.route('/connect', methods=['POST']) #POST method for confirm connection between RPi and app
def control_car():
    command = request.form.get('command')
    print("Received command:", command)

    return 'Úspěšně navázáno spojení', 200 


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
