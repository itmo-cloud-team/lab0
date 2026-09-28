from flask import Flask
import json
import sys

import db
from routers import api

app = Flask(__name__)
config = None

app.register_blueprint(api.router)

def get_html(page_name):
    with open(f'pages/{page_name}.html') as file:
        return file.read()

@app.route('/')
def index():
    return get_html('index')

if __name__ == '__main__':
    config_file_path = ''
    for arg in sys.argv:
        if arg.startswith('--config'):
            config_file_path = arg.split('=')[1]
            break
    if not config_file_path:
        print('Bad usage. Missing --config key.')
        exit(1)

    with open(config_file_path, 'r') as file:
        config = json.load(file)

    result = db.connect(
        config['db_username'],
        config['db_password'],
        config['db_host'],
        config['db_port'],
        config['db_name']
    )
    if not result:
        exit(1)

    app.run(host=config['host'], port=config['port'])
