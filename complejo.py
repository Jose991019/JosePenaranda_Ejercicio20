import numpy as np

class Complejo():
    def __init__(self,real,imag):
        self.real = real
        self.imaginario = imag
        self.norma = np.sqrt(self.real**2 + self.imaginario**2)
    def conjugado(self):
        self.imaginario = -self.imaginario
    def calcula_norma(self):
        self.norma = np.sqrt(self.real**2 + self.imaginario**2)
    def pow(self,n):
        resultado = Complejo(self.real,self.imaginario)
        for i in range(n-1):
            resultado = Complejo(self.real*resultado.real - self.imaginario*resultado.imaginario,self.imaginario*resultado.real + self.real*resultado.imaginario)
        return(resultado)