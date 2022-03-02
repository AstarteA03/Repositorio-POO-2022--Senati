class Animales:
    pass
    def __init__(self,Nombre,Años,Color):
        self.Nombre= Nombre
        self.Años= Años
        self.Color= Color
    def description(self):
        return '{}Es un animal tiene {} años \nsu pelaje es de color {} \n'.format(self.Nombre,self.Años,self.Color)
    def comentario(self):
        return '{} Gracias por su Visita'.format(self.Nombre)
    
instructor= Animales('Misha',2,'Castaño')
print(instructor.description())
print(instructor.comentario())
