#Clase mayor o clase papá
class Animal:
    pass
    def __init__(self,nombre,tipo)
        self.nombre=nombre
        self.tipo=tipo
    
    #metodos
    def descripcion(self)
        return '{}este animal es {}'.format(self.nombre,self.tipo)

#clase hijo o subclase
class perro(Animal):
    def sonido (self.tipoSonido):
        return'{}se trabajo es {}'.format(self.sonido,self.TipoSonido)
class Gato(Animal):
    def sonido(self.tipo.Sonido):
        return '{} su trabajo es {}'.format(self.nombre,self.TipoSonido)
    
#Objetos

newAnimal = Perro('Firulais','Labrador')
print(newAnimal.descripcion())
print(newAnimal.comportamiento('Ladra'))

otroAnimal = Gato('Mina','Sibeariano')
print(newAnimal.descripcion())
print(newAnimal.comportamiento('Maulla'))


animalito= Perro('Rex','Sabueso')
print(newAnimal.descripcion())
print(newAnimal.comportamiento('Ladra'))
