class citas:
    registrar=''
    NumeroAtencion=0
    NombreCliente=''
    fecha=0
    descripcionAtencion=''
    Costo=0

    def __init__(self):
        self.registrar='A-001-A-002-B-022'
        self.NumeroAtencion=0
        self.NombreCliente='S/A'
        self.fecha=0
        self.descripcionAtencion='S/A'
        self.costo=45000
    def setregistrar(self,registrar):
        if registrar[1:5].isalpha() and registrar[5:3].isdigit():
            self.registrar=registrar

    def setNumeroAtencion(self,NumeroAtencion):
        if len (NumeroAtencion) == 1:
            self.NumeroAtencion = NumeroAtencion



    def NombreCliente(self,NombreCliente):
        if len (NombreCliente) >= 8:
            self.NombreCliente = NombreCliente
            return True
        else:
            print("Nombre Incorrecto:")


    def fecha(self,fecha):
        if len(fecha) >= 10:
            self.fecha = fecha

    def descripcionAtencion(self,descripcionAtencion):
        if len (descripcionAtencion) >= 15:
            self.descripcionAtencion = descripcionAtencion

    def costo(self,costo):
        if len (costo) >= 20000:
            self.costo = costo