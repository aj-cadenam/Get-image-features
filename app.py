#from flask import Flask, render_template, request
from flask import Flask, request, render_template
from random import sample

#Para subir archivo tipo foto al servidor
from werkzeug.utils import secure_filename 
import os

from common.caracteristicas import get_size, size_kb, format

#Declarando nombre de la aplicación e inicializando
app = Flask(__name__)

#Redireccionando cuando la página no existe
@app.errorhandler(404)
def not_found(error):
    return 'Ruta no encontrada'


def stringAleatorio():
    #Generando string aleatorio
    string_aleatorio = "0123456789abcdefghijklmnopqrstuvwxyz_"
    longitud         = 20
    secuencia        = string_aleatorio.upper()
    resultado_aleatorio  = sample(secuencia, longitud)
    string_aleatorio     = "".join(resultado_aleatorio)
    return string_aleatorio
    
"""La funcion stringAleatorio() se utiliza para dar un nombre de raiz a las imagenes cargadas por el usuario"""
     
#Creando un Decorador
@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')


@app.route('/registrar-archivo', methods=['GET', 'POST'])


def registarArchivo():
        if request.method == 'POST':

            #Script para archivo
            file     = request.files['archivo']
            basepath = os.path.dirname (__file__) #La ruta donde se encuentra el archivo actual
            filename = secure_filename(file.filename) #Nombre original del archivo
            
            #capturando extensión del archivo ejemplo: (.png, .jpg, .pdf ...etc)
            extension           = os.path.splitext(filename)[1]
            nuevoNombreFile     = stringAleatorio() + extension
     
            upload_path = os.path.join (basepath, 'static',nuevoNombreFile) 
            file.save(upload_path)

            #Obtener caracteristicas
            alto, ancho = get_size(upload_path)
            formato=format(upload_path)
            size=size_kb(upload_path)
                       
            return render_template('screen_print.html', nuevoNombreFile =  nuevoNombreFile, img_alto = alto, img_ancho = ancho, formato=formato,size=size )        
        return render_template('index.html') 

"""La funcion registrarArchivo() obtiene la imagen que el usuario carga y posteriomente la guarda en 
la carpeta static para el procesamiento de la misma para obtener sus caracterisitcas """  

if __name__ == '__main__':
    app.run(debug=True, port=5000)