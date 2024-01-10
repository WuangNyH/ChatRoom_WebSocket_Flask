from http import HTTPStatus

from sqlalchemy.testing.pickleable import User

from models.users import Users
from core.Database import SessionLocal
from utils.Password import hashPassword, verifyPassword, checkPassword


class UsersService:
    def __init__(self):
        self.db = SessionLocal()

    def registerUser(self, request):
        try:
            newUser = Users(**request)
            checkPassword(newUser.password)
            newUser.password = hashPassword(newUser.password)
            self.db.add(newUser)
            self.db.commit()
            return newUser
        finally:
            self.db.close()

    def getUsersByUsername(self, username):
        try:
            user = self.db.query(Users).filter_by(username=username).first()
            return user
        finally:
            self.db.close()

    def loginUser(self, request):
        try:
            user = self.getUsersByUsername(request.get('username'))

            if not user:
                raise ValueError("Username does not exist!!!")

            if not verifyPassword(user.password, request.get('password')):
                raise ValueError("Wrong password!!!")

            return user
        finally:
            self.db.close()
