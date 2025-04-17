from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

latest_data = {'a': None, 'b': None, 'c': None, 'd': None}

@app.route('/send_data', methods=['POST'])
def receive_data():
    data = request.json
    latest_data['a'] = data.get('a')
    latest_data['b'] = data.get('b')
    latest_data['c'] = data.get('c')
    latest_data['d'] = data.get('d')
    return jsonify({'message': '데이터 수신 완료', 'received': latest_data})

@app.route('/get_data', methods=['GET'])
def get_data():
    return jsonify(latest_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
