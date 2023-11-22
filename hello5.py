# 9-nov-2023

from flask import Flask, request, make_response
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

if __name__ == "__main__":
    app.run(debug=True)


@app.route('/api/token/verify/<int:employee_id>', methods=['POST'])
def verify_token(employee_id):
    log_message = {
        'operation': 'verify token',
        'status': 'processing'
    }
    app.logger.info(str(log_message))

    data = request.json

    try:
        payload = jwt.decode(data['token'], algorithms = ['HS256'],
                              key="mysecretkey")
    # except:
    #     log_message['status'] = 'unsuccessful'
    #     log_message['reason'] = 'Token verification error'
    #     app.logger.error(str(log_message))
    #     err = TokenVerificationError()
    #     return str(err), err.status

    # app.logger.info(str(log_message))
    # return {'token': payload}, 200

        if (employee_id == payload['id']):
                log_message['status'] = 'verified'

                app.logger.info(str(log_message))

                return {'token': payload}, 200
        else:
            log_message['status'] = 'not verified'
            log_message['status'] = 'unsuccessful'
            log_message['reason'] = 'Token decode error'
            app.logger.error(str(log_message))
            err = TokenGenerationError()
            return str(err), err.status
        
     
    except:
        log_message['status'] = 'unsuccessful'
        log_message['reason'] = 'Token decode error'
        app.logger.error(str(log_message))
        err = TokenGenerationError()
        return str(err),err.status