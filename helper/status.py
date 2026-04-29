from flask import Flask
import platform

app = Flask(__name__)

@app.route('/status')
def status():
    return {
        "service": "Helper-Service",
        "system": platform.system(),
        "version": "1.0.0",
        "container_info": "Running on Python 3.9-slim"
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)