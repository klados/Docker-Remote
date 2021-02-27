from .. import Base
import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import Integer, Column, String, Enum, DateTime


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    password = Column(String(120), nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    role = Column(Enum('user', 'admin', 'superAdmin'), default='user', nullable=False)
    created_at = Column(DateTime(), default=datetime.datetime.utcnow)

    def setPassword(self, password):
        self.password = generate_password_hash(password)

    def getPassword(self, password):
        return check_password_hash(self.password, password)

    # def __repr__(self):
    #     return '<New user %r>' % self.username
