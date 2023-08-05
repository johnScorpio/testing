# models.py
class Role:
    def __init__(self, name):
        self.name = name

class User:
    def __init__(self, username, password, active=True, roles=['user']):
        self.username = username
        self.password = password
        self.active = active
        self.roles = roles

