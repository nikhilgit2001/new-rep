from flask import Flask, request, make_response, jsonify

app = Flask(__name__)

class Employee:
    def __init__(self, name, id, address):
        self.name = name
        self.id = id
        self.address = address

employees = {
    1: Employee("Prashanth", 1, "Bengaluru"),
    2: Employee("Shiva", 2, "Bengaluru"),
    3: Employee("Phaneendra", 3, "Mysore"),
    4: Employee("Pranav", 4, "Mysore"),
}


count = 4

class EmployeeManager:
    @app.route("/api/employee/", methods=["POST"])
    def create_employee():
        global count
        employee = request.json
        count += 1
        employee['id'] = count
        employees[count] = Employee(employee['name'], count, employee['address'])
        return jsonify(employee)

    @app.route("/api/employee/<int:employee_id>", methods=["PUT"])
    def alter_employee_data(employee_id):
        employee = request.json
        employee_obj = employees.get(employee_id)

        if employee_obj is None:
            return make_response("Employee not found", 404)

        employee_obj.name = employee.get('name', employee_obj.name)
        employee_obj.address = employee.get('address', employee_obj.address)
        return jsonify(employee_obj.__dict__)

    @app.route("/api/employee/<int:employee_id>", methods=["GET"])
    def get_employee_information(employee_id):
        employee = employees.get(employee_id)
        if employee is None:
            return make_response("Employee not found", 404)
        return jsonify(employee.__dict__)

    @app.route("/api/employee/<int:employee_id>", methods=["DELETE"])
    def remove_employee_data(employee_id):
        employee = employees.get(employee_id)
        if employee is None:
            return make_response("Employee not found", 404)
        del employees[employee_id]
        return make_response("", 200)

if __name__ == "__main__":
    app.run(debug=True)
