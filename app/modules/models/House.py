class House():
    def __init__(self, direccion, propietario, precio, url_foto):
        self.__direccion = direccion
        self.__propietario = propietario
        self.__precio = precio
        self.__url_foto = url_foto

    def get_direccion(self):
        return self.__direccion

    def get_propietario(self):
        return self.__propietario

    def get_precio(self):
        return self.__precio

    def get_foto(self):
        return self.__url_foto
