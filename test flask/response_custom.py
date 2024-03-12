from flask import jsonify


def response_success(status: int, data, *, msg: str):
    message = "Success"
    if message is not None:
        message = message + ' ' + str(msg)
    else:
        if status == 201:
            message = message + ' ' + 'create'
    data = ({'code': status, 'message': message, 'data': data})
    return jsonify(data), status


def response_error(status: int, message: str):
    data = ({'code': status, 'message': message, 'data': 'null'})
    return jsonify(data), status
