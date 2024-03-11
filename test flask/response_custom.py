from flask import jsonify


def response_success(status: int, data):
    data = ({'code': status, 'message': 'success', 'data': data})
    return jsonify(data), status


def response_error(status: int, message: str):
    data = ({'code': status, 'message': message, 'data': 'null'})
    return jsonify(data), status
