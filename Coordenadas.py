
import pyautogui, sys


"""El ultimo punto del reto practico: 
Al dar clic sobre algún punto de la imagen visualizada en la 
aplicación Web, debe presentar la siguiente información:
• Coordenas del pixel seleccionado
• Color en formato Hexagesimal (EJ. #62ACB7)
• Color en formato RGB (EJ. 98, 172, 183)

Para esta problematica se expusieron 4 necesidades: 
1.Guardar el evento click mouse sobre la imagen en la pagina web.(No logrado)
2.Obtener coordenadas de dicho evento.(Codigo: #obtener coordenadas)
3.Con las coordenadas entran como parametro a las funcion pixel_color()
para que retorne el color en RGB.
4.Con el return de la funcion pixel_color() se esperaba introducirlo en la 
funcion rgb_to_hex()

"""

"""Obtener coordenadas: Al ejecutar este script podra obtener las coordenadas del 
mouse por pantalla la cual se debe para con la interrupción del teclado, sin embargo
no logre encontrar una solucion para esta problematica desde la solución del backend.
"""

print('Press Ctrl-C to quit.')
try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print('\n')

