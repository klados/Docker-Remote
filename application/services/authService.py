from application.resources.userResource import UserResource
from werkzeug.security import check_password_hash


class AuthService:

    def __init__(self, db):
        self.userResource = UserResource(db)
        self.db = db

    def loginService(self, data):
        user = self.userResource.getUserByEmail(data['email'])
        print(user, data['password'])
        if user:
            if user.getPassword(data['password']):
                return {'status': 'success', 'username': user.username, 'role': user.role}
        return {'status': 'error', 'msg': 'Wrong credentials'}

    def registerService(self, data):
        errors = []
        # check if email already exists
        ans = self.userResource.checkIfEmailExists(data['email'])
        if ans:
            errors.append({'status': 'error', 'field': 'email', 'msg': 'Email already exists.'})

        # check if username already exists
        ans = self.userResource.checkIfUsernameExists(data['username'])
        if ans:
            errors.append({'status': 'error', 'field': 'username',
                           'msg': 'Username already in use. Please choose something else.'})

        if len(errors) != 0:
            return errors

        # add to database
        if self.userResource.createNewUser(data):
            return []
        return [{'status': 'error', 'msg': 'Unknown error, user did not created'}]
