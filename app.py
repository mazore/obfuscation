from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/bundle_v1.js')
def serve_js():
    return send_from_directory('.', 'bundle_v1.js')

if __name__ == "__main__":
    app.run()
