from flask import jsonify
from flask_cors import CORS

from app import create_app

app = create_app()
CORS(app)
# Error Handlers


@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({
        "name": "Error 500 - Internal Server Error",
        "msg": error
    })


@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "name": "Error 404 - Not Found",
        "msg": error
    })


@app.route('/')
def index():
    return {"Message": "Welcome to Erco test"}


if __name__ == "__main__":
    app.run(debug=False)
