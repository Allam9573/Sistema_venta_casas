class User():
    def __init__ (self, nombre, correo, usuario, contrasenia):
        self.__nombre = nombre
        self.__correo = correo
        self.__usuario = usuario
        self.__contrasenia = contrasenia

    def get_nombre(self):
        return self.__nombre

    def get_correo(self):
        return self.__correo

    def get_usuario(self):
        return self.__usuario

    def get_contrasenia(self):
        return self.__contrasenia
