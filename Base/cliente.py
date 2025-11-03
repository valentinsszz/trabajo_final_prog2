class Cliente:                 #lo mismo, nose si hacia falta poner los tipos de datoss
    
    # Constructor
    
    def __init__(self, numeroId, nombres, apellidos, email):
        self.__numeroId = numeroId
        self.__nombres = nombres
        self.__apellidos = apellidos
        self.__email = email

    
    # Comandos (setters)
    
    def establecerNumeroId(self, numeroId):
        self.__numeroId = numeroId

    def establecerNombres(self, nombres):
        self.__nombres = nombres

    def establecerApellidos(self, apellidos):
        self.__apellidos = apellidos

    def establecerEmail(self, email):
        self.__email = email

    # Consultas
    
    def obtenerNumeroId(self):
        return self.__numeroId

    def obtenerNombres(self):
        return self.__nombres

    def obtenerApellidos(self):
        return self.__apellidos

    def obtenerEmail(self):
        return self.__email
    
    def __eq__(self, otro):
        if not isinstance(otro, Cliente):
            return False
        return self.obtenerNumeroId == otro.obtenerNumeroId()
    
    def __str__(self):
        # Devuelve una cadena legible con los datos del cliente es mas legible que usar return "Cliente: " + self.__nombres + " " + self.__apellidos + " - ID: " + str(self.__numeroId) + " - Email: " + self.__email
        return f"Cliente: {self.__nombres} {self.__apellidos} - ID: {self.__numeroId} - Email: {self.__email}"