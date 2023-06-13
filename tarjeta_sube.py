class Sube:
    def __init__(self):
        self.saldo = 0
        self.grupo_beneficiario = None
        self.estado = ACTIVADO
    
    def obtener_precio_ticket(self):
        if self.grupo_beneficiario == PRIMARIO:
            return 35
        else:
            return PRECIO_TICKET
    
    def pagar_pasaje(self):
        if self.estado == DESACTIVADO: #verificacion de estado de la tarjeta
            raise UsuarioDesactivadoException("Tarjeta desactivada")
        
        if self.saldo < self.obtener_precio_ticket(): #verificacion del saldo de la tarjeta
            raise NoHaySaldoException("No hay saldo suficiente")
        
        self.saldo -= self.obtener_precio_ticket() #si el saldo y el estado esta bien, resta el precio del ticket al saldo de la tarjeta
    
    def cambiar_estado(self, nuevo_estado):
        if nuevo_estado not in [ACTIVADO, DESACTIVADO]: #si nuevo_estado no es ACTIVADO o DESACTIVADO, devuelve una excepcion
            raise EstadoNoExistenteException("Pendiente...") 
        
        self.estado = nuevo_estado #si está en ACTIVADO O DESACTIVADO 


class NoHaySaldoException(Exception):
    pass


class UsuarioDesactivadoException(Exception):
    pass


class EstadoNoExistenteException(Exception):
    pass


# Constantes
PRIMARIO = "primario"
PRECIO_TICKET = 70
ACTIVADO = "activado"
DESACTIVADO = "desactivado"
