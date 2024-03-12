import json
from flask import Flask, jsonify, request
from response_custom import response_error, response_success

app = Flask(__name__)

employees = [{'id': 1, 'name': 'Ashley'}, {'id': 2, 'name': 'mike'}]
nextEmployeeId = 4


@app.route('/employees', methods=['GET'])
def get_employees():
    data = response_success(200, employees)
    return data


def get_employee(id):
    return next((e for e in employees if e['id'] == id), None)


@app.route('/employees/<int:id>', methods=['GET'])
def get_employee_by_id(id: int):
    print("id : ", id)
    employee = get_employee(id)
    print("em : ", employee)
    if employee is None:
        dataErr = response_error(404, 'Employee does not exist')
        return dataErr
        # return jsonify({'error': 'Employee does not exist'}), 404
    return response_success(200, employee)


def employee_is_valid(employee):
    for key in employee.keys():
        if key != 'name':
            return False
    return True


@app.route('/employees', methods=['POST'])
def create_employee():
    global nextEmployeeId
    employee = json.loads(request.data)  # ini nerima ketika raw
    # request.form -> untuk form
    # request.
    if not employee_is_valid(employee):
        return jsonify({'error': "Invalid employee properties"}), 400

    employee['id'] = nextEmployeeId
    nextEmployeeId += 1
    employees.append(employee)
    return response_success(201, employee)
    # return '', 201, {'location': f'/employees/{employee["id"]}'}


@app.route("/employees/<int:id>", methods=['PUT'])
def update_employee(id: int):
    get = request.get_json()
    print("yeya : ", get['data'])
    employee = get_employee(id)
    if employee is None:
        return jsonify({'error': 'Employee does not exist.'}), 404

    updated_employee = json.loads(request.form)  # ambil data dari request
    if not employee_is_valid(updated_employee):
        return jsonify({'error': 'Invalid employee properties'}), 400

    employee.update(updated_employee)

    return jsonify(employee)


@app.route('/employees/<int:id>', methods=['DELETE'])
def delete_employee(id: int):
    global employees
    employee = get_employee(id)
    if employee is None:
        return response_error(404, 'Employee does not exist')

    employees = [e for e in employees if e['id'] != id]
    return response_success(201, employee, msg="delete")


@app.route('/file', methods=['POST'])
def get_file():
    file = request.files['file']
    print("file : ", file.filename)
    txt = request.form['text']
    print("text : ", txt)
    return jsonify({"code": 200, "message": "sukses upload"}), 200


if __name__ == '__main__':
    app.run(port=5000, debug=True)
