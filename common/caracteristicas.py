from PIL import Image
import sys
import os

def get_size(path):
    img = Image.open(path)
    ancho,alto = img.size
    return(ancho,alto)

def format(path):
    root_ext = os.path.splitext(path)
    return( root_ext[1])
    

def size_kb(path):
    tamaño = os.path.getsize(path)
    return( (tamaño/1000 ))
    

