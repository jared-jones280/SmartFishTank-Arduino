import os
import socket
import threading
import pickle
import atexit
import json
from flask import Flask, jsonify, request, render_template, flash, request, redirect, url_for, send_from_directory
from flask_cors import CORS
from werkzeug.utils import secure_filename


app = Flask(__name__)
CORS(app)

fish_data = {}

def tank_handler(conn, addr):
    print('\t\tGot a tank!')
    
    while True:
        global fish_data
        fish_data = json.loads(conn.recv(2**14).decode('utf-8'))
        # print('Got Data: ')
        # print(fish_data)

def server():
    print('Looking for fish tank...')
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.bind((socket.gethostname(), 8001))
    serversocket.listen(5)

    while True:
        (clientsocket, address) = serversocket.accept()
        
        data = clientsocket.recv(10240).decode('utf-8')
        print('New connection: ')
        print(data)
        
        try:
            data = json.loads(data)
        except socket.error:
            clientsocket.sendall('Unknown connection'.encode('utf-8'))
            clientsocket.close()
            continue
        except json.decoder.JSONDecodeError:
            pass
        
        if 'device' in data and data['device'] == 'smart-fish-tank':
            to_send = {'accept' : True}
            clientsocket.sendall(json.dumps(to_send).encode())
            threading.Thread(target=tank_handler, args=(clientsocket, address,), daemon=True).start()
        
        print(data)     # ! Does this print the results after a connection is already established?
        # ct = client_thread(clientsocket)
        # ct.run()
        
def exit_handler():
    print('Closing')

def allowable_static_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ['html', 'js', 'css', 'ico']

@app.route('/api', methods=['GET'])
def api():
    return jsonify(fish_data)

@app.route('/', methods=['GET'])
def index():
    return send_from_directory('./', '462web.html')

@app.route('/<path:path>', methods=['GET'])
def static_page(path):
    path = secure_filename(path)

    if allowable_static_file(path) and os.path.exists('./{}'.format(path)):
        return send_from_directory('./', path)
    else:
        return handler404()

def handler404():
    return '<h1>404 Error</h1>'

if __name__ in '__main__':
    atexit.register(exit_handler)
    threading.Thread(target=server, daemon=True).start()
    print('Starting server')
    app.run(host='0.0.0.0', port=8000)
    # main()