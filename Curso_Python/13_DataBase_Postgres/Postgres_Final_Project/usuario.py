class Usuario:
    def __init__(self, id_usuario=None, username=None, password=None):
        self.id_usuario = id_usuario
        self.username = username
        self.password = password

    def __str__(self):
        return f"ID: {self.id_usuario}, Username: {self.username}, Password: {self.password}"
    
    @property
    def id_usuario(self):
        return self._id_usuario

    @property
    def username(self):
        return self._username

    @property
    def password(self):
        return self._password
    
    @id_usuario.setter
    def id_usuario(self, value):
        self._id_usuario = value

    @username.setter
    def username(self, value):
        self._username = value

    @password.setter
    def password(self, value):
        self._password = value