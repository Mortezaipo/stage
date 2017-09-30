import tornado.web
from settings import Settings
from db import db
from memcached import Memcached
import lib


def authenticate(email: str, password: str) -> bool:
    password = lib.generate_password(password)
    admin = db.select("SELECT * FROM users WHERE email=%s AND password=%s LIMIT 1", (email, password), True)
    if admin:
        return True
    return False


def register(email: str, password: str) -> int:
    password = lib.generate_password(password)
    if db.select("SELECT user_id FROM users WHERE email=%s AND password=%s", (email, password), True):
        return 3
    action = db.insert("INSERT INTO users (email, password) VALUES (%s, %s)", (email, password))
    if action:
        return 1
    return 2


def validate_user(key: str) -> bool:
    pass


class AuthHandler(tornado.web.RequestHandler):
    """Authentication handler class."""

    def get(self):
        self.render("auth/login.html")

    def post(self):
        email = self.get_argument("email")
        password = self.get_argument("password")
        if authenticate(email, password):
            self.write("auth success")
        else:
            self.write("auth faild")


class RegisterHandler(tornado.web.RequestHandler):

    def get(self):
        self.render("auth/register.html")

    def post(self):
        email = self.get_argument("email")
        password = self.get_argument("password")

        action = register(email, password)
        if action == 3:
            self.write("already exists!")
        elif action == 1:
            self.write("registered!")
        elif action == 2:
            self.write("failed!")
