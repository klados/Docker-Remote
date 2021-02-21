from application.models.user import User


class UserResource:
    def __init__(self, db):
        self.db = db

    def checkIfEmailExists(self, email: str) -> bool:
        return self.db.session.query(User.email).filter_by(email=email).scalar()

    def checkIfUsernameExists(self, username: str) -> bool:
        return self.db.session.query(User).filter_by(username=username).scalar()

    def createNewUser(self, data: dict) -> bool:
        """ insert user to users table """
        try:
            newUser = User(username=data['username'], email=data['email'])
            newUser.setPassword(data['password'])
            self.db.session.add(newUser)
            self.db.session.commit()
            return True
        except Exception:
            return False

    def getUserByEmail(self, email: str) -> User:
        return self.db.session.query(User).filter_by(email=email).first()
        #._asdict()

