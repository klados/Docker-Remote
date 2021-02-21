from .. import db
import datetime
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    role = db.Column(db.Enum('user', 'admin', 'superAdmin'), default='user', nullable=False)
    created_at = db.Column(db.DateTime(), default=datetime.datetime.utcnow)

    def setPassword(self, password):
        self.password = generate_password_hash(password)

    def getPassword(self, password):
        return check_password_hash(self.password, password)

    # def __repr__(self):
    #     return '<New user %r>' % self.username
