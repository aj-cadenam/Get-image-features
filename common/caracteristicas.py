from PIL import Image
import sys
import os

#try:
 #   img = Image.open("static/archivos/WNGR_ZAD1OKTMS8P75FE.jpg")

#except:
#    print("No se pudo cargar la imagen")
#    sys.exit(1)

#mg.show()
def get_size(path):
    img = Image.open(path)
    ancho,alto = img.size
    return(ancho,alto)

def format():
    pass

def size_kb():
    #TODO : implement size kb
    pass

#Calcular resolucion de la imagen
#ancho,alto = img.size
#print("ancho:", ancho)
#print("alto:", alto)

#resolucion= ancho * alto
#print("La resolucion de la imagen es :",resolucion, "pixeles" )

#color del PIXEL

#pixels = img.load()
#color=pixels[100,100]
#print(color)

#Tamaño en Kbs del archivo

#tamaño=os.path.getsize('static/archivos/WNGR_ZAD1OKTMS8P75FE.jpg')

#print(tamaño)
#print("Tamaño en Kbs : '%s':" %(tamaño/1000))
#print(type(tamaño))

#Formarto de la imagen ingresada

#Formato de la imagen

# Python program to explain os.path.splitext() method 
    
  
# path
path = 'static/archivos/UDF3GVTWE0LKJXA97ZCR.jpg'
  
# Split the path in 
# root and ext pair
root_ext = os.path.splitext(path)
  
# print root and ext
# of the specified path
 
#print("root part of '% s':" % path, root_ext[0])
#print("ext part of '% s':" % path, root_ext[1], "\n")
print("El formato de la imagen es :", root_ext[1])
  
# path

  
# Split the path in 
# root and ext pair
#root_ext = os.path.splitext(path)
  
# print root and ext
# of the specified path
#print("root part of '% s':" % path, root_ext[0])
#print("ext part of '% s':" % path, root_ext[1])
