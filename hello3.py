from flask import Flask

app = Flask(__name__)

employees = {
    1: "Prashanth",
    2: "Shiva",
    3: "Phani",
    4: "Pranav"
}

@app.route("/<employeeName>", methods=["GET"])
def hello_employee(employeeName):
    return "<p>Hello, {}!</p>".format(employeeName)

@app.route("/<int:employee_id>", methods=["GET"])
def hello_employee_var(employee_id):
    return "<p>Hello, {}!</p>".format(employees.get(employee_id, "Person Not Present"))

from flask import Flask
# from flask import request, make_response
# app = Flask(__name__)

# class Employee:
#     name = ''
#     id = ''
#     address = ''
#     def __init__(self, name, id, address):
#         self.name = name
#         self.id = id
#         self.address = address
#     def __str__(self):
#         return str({
#         "id": self.id,
#         "name": self.name,
#         "address": self.address
#         })
    
# employees = {
# 1: Employee("Prashanth", 1, "Bengaluru"),
# 2: Employee("Shiva", 2, "Bengaluru"),
# 3: Employee("Phaneendra", 3, "Mysore"),
# 4: Employee("Pranav", 4, "Mysore"),
# }
# count = 4

# @app.route("/api/employee/", methods=["POST"])
# def create_employee():
#     global count
#     employee = request.json
#     count += 1
#     employee['id'] = count
#     employees[count] = Employee(employee['name'], count, employee['address'])
#     return employee

# @app.route("/api/employee/<int:employee_id>", methods=["PUT"])
# def alter_employee_data(employee_id):
#     employee = request.json
#     employees[employee_id].name = employee.get('name', employees[employee_id].name)
#     employees[employee_id].address = employee.get('address', employees[employee_id].address)
#     return str(employees[employee_id])

# @app.route("/api/employee/<int:employee_id>", methods=["GET"])
# def get_employee_information(employee_id):
#     return str(employees[employee_id])

# @app.route("/api/employee/<int:employee_id>", methods=["DELETE"])
# def remove_employee_data(employee_id):
#     del employees[employee_id]
#     return make_response(""), 200
# app.run()
