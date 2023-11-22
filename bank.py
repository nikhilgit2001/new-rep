# class bank:
#       def __init__(self, name, acc_num, bal):
#             self.name = name
#             self.acc_num = acc_num
#             self.bal = bal

#       def debit(self, amount):
#             if(amount > self.bal):
#                   print("Amount cannot be deducted")

#             else:
#                   bal = self.bal - amount
#             return bal

#       def credit(self, amount):
#             if(amount <= 0):
#                   print("Invalid amount")

#             else:
#                   bal = self.bal + amount
#             return bal

# print(bank("nikhi", 12000, 10000).credit(2000))
            
# # class Bank:
# #     def __init__(self, name, acc_num, bal):
# #         self.name = name
# #         self.acc_num = acc_num
# #         self.bal = bal

# #     def debit(self, amount):
# #         if amount > self.bal:
# #             print("Amount cannot be deducted")
# #         else:
# #             self.bal -= amount
# #         return self.bal

# #     def credit(self, amount):
# #         if amount <= 0:
# #             print("Invalid amount")
# #         else:
# #             self.bal += amount
# #         return self.bal

# # # Taking user input
# # user_name = input("Enter your name: ")
# # account_number = input("Enter your account number: ")
# # initial_balance = float(input("Enter your initial balance: "))

# # # Creating a Bank object
# # user_account = Bank(user_name, account_number, initial_balance)

# # # Asking user for the operation
# # operation = input("Choose operation (debit/credit): ").lower()

# # # Performing the chosen operation
# # if operation == "debit":
# #     debit_amount = float(input("Enter the amount to be debited: "))
# #     new_balance = user_account.debit(debit_amount)
# #     print(f"Final balance after debit: {new_balance}")
# # elif operation == "credit":
# #     credit_amount = float(input("Enter the amount to be credited: "))
# #     new_balance = user_account.credit(credit_amount)
# #     print(f"Final balance after credit: {new_balance}")
# # else:
# #     print("Invalid operation. Please choose debit or credit.")

# from flask import Flask, request, jsonify
# from flask_httpauth import HTTPBasicAuth

# app = Flask(__name__)
# auth = HTTPBasicAuth()

# # Dummy user credentials for authentication
# users = {
#     "username": "password",
# }

# class Bank:
#     def __init__(self, name, acc_num, bal):
#         self.name = name
#         self.acc_num = acc_num
#         self.bal = bal

#     def debit(self, amount):
#         if amount > self.bal:
#             return "Amount cannot be deducted", 400
#         else:
#             self.bal -= amount
#             return {"message": "Debit successful", "new_balance": self.bal}, 200

#     def credit(self, amount):
#         if amount <= 0:
#             return "Invalid amount", 400
#         else:
#             self.bal += amount
#             return {"message": "Credit successful", "new_balance": self.bal}, 200

# # Creating a Bank object
# user_account = Bank("John Doe", "123456789", 1000.0)

# @auth.verify_password
# def verify_password(username, password):
#     return users.get(username) == password

# @app.route('/debit', methods=['POST'])
# @auth.login_required
# def debit():
#     data = request.get_json()
#     amount = data.get('amount')

#     # Validate the amount
#     if not isinstance(amount, (int, float)):
#         return "Invalid amount format", 400

#     response, status_code = user_account.debit(amount)
#     return jsonify(response), status_code

# @app.route('/credit', methods=['POST'])
# @auth.login_required
# def credit():
#     data = request.get_json()
#     amount = data.get('amount')

#     # Validate the amount
#     if not isinstance(amount, (int, float)):
#         return "Invalid amount format", 400

#     response, status_code = user_account.credit(amount)
#     return jsonify(response), status_code

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, request, jsonify

app = Flask(__name__)

class Bank:
    def __init__(self, name, acc_num, bal):
        self.name = name
        self.acc_num = acc_num
        self.bal = bal

    def debit(self, amount):
        if amount > self.bal:
            return "Amount cannot be deducted", 400
        else:
            self.bal -= amount
            return {"message": "Debit successful", "new_balance": self.bal}, 200

    def credit(self, amount):
        if amount <= 0:
            return "Invalid amount", 400
        else:
            self.bal += amount
            return {"message": "Credit successful", "new_balance": self.bal}, 200

# Creating a Bank object
user_account = Bank("John Doe", "123456789", 1000.0)

@app.route('/debit', methods=['POST'])
def debit():
    data = request.get_json()
    amount = data.get('amount', 0)
    response, status_code = user_account.debit(amount)
    return jsonify(response), status_code

@app.route('/credit', methods=['POST'])
def credit():
    data = request.get_json()
    amount = data.get('amount', 0)
    response, status_code = user_account.credit(amount)
    return jsonify(response), status_code

if __name__ == '__main__':
    app.run(debug=True)
