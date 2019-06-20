"""
    Para llamar a paquetes de la misma altura
"""
# sys es para utilidad para volver hacia atras en una carpeta 
import sys
sys.path.append('../')
from paquete2.variables import limite
from paquete3.metodos import generar_potencia

for i in range(1, limite+1):
    print(i)
    valor = generar_potencia(i, 2)
    print(valor)
    print("--------------------")
