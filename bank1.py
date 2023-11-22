# from flask import Flask, request, jsonify

# app = Flask(__name__)

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

# @app.route('/debit', methods=['POST'])
# def debit():
#     data = request.get_json()
#     amount = data.get('amount', 0)
#     response, status_code = user_account.debit(amount)
#     return jsonify(response), status_code

# @app.route('/credit', methods=['POST'])
# def credit():
#     data = request.get_json()
#     amount = data.get('amount', 0)
#     response, status_code = user_account.credit(amount)
#     return jsonify(response), status_code

# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask
from flask import request, make_response
import jwt

class BaseException(Exception):
    status = 400
    message = ""

    def __init__(self, status, message) -> None:
        super().__init__()
        self.status = status
        self.message = message

    def __str__(self):
        return str({'status': self.status, 'message': self.message})

class TokenGenerationError(BaseException):
    def __init__(self) -> None:
        super().__init__(500, "Unable to generate the token")

app = Flask(__name__)

@app.route('/api/token/<int:employee_id>', methods=['POST'])
def fetch_token(employee_id):
    log_message = {
        'operation': 'fetch token',
        'status': 'processing'
    }
    app.logger.info(str(log_message))

    payload = {
        'id': employee_id,
        'iss': 'DSCE',
        'sub': 'Employee Microservice Token'
    }

    try:
        token = jwt.encode(payload, key="mysecretkey")
    except:
        log_message['status'] = 'unsuccessful'
        log_message['reason'] = 'Token generation error'
        app.logger.error(str(log_message))
        err = TokenGenerationError()
        return str(err), err.status

    app.logger.info(str(log_message))
    return {'token': token}, 200
