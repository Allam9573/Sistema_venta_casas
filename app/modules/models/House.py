class House():
    def __init__(self, direccion, propietario, precio, url_foto):
        self.direccion = direccion
        self.propietario = propietario
        self.precio = precio
        self.url_foto = url_foto

    def get_direccion(self):
        return self.direccion

    def get_propietario(self):
        return self.propietario

    def get_precio(self):
        return self.precio

    def get_foto(self):
        return self.url_foto
