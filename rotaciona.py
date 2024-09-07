# INCOMPLETO -> ERRADO


entrada = input().split(' ')
vezes = int(entrada[0])
angulo = int(entrada[1])
from math import cos,sin,radians
matriz = [
    cos(angulo),-(sin(angulo)),
    sin(angulo),cos(angulo)
    ]
entrada = input().split(' ')
# entrada = [
#  20  
#  50
#      ]
retornar = [f'{((matriz[0]*radians(int(entrada[0]))+matriz[1]*radians(int(entrada[1]))))*180/3.14:.2f}',f'{(matriz[2]*radians(int(entrada[0]))+matriz[3]*radians(int(entrada[1])))*180/3.14:.2f}']
print(*retornar)