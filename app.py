# python -m flask run 'codigo para hacer funcionar en la terminal' 
from flask import Flask, render_template, url_for, request # Importamos las librerias a ser usadas
import requests

empresas = [
{
    "nombre": "empresa1", 
    "puestos" : [
        {"nombre": "Arquitecto"},
        {"nombre" : "Ingeniero"}
    ],  
},
{
    "nombre": "empresa2", 
    "puestos" : [
        {"nombre": "Psicologo"},
        {"nombre" : "Disenhador"}
    ],  
},
]

app = Flask(__name__) # Creamos el objeto app

@app.route("/") # Llamamos al metodo route y le pasamos el argumento de la url o slug que queremos que vaya
def inicio(): # Creamos la funcion inicio
    return render_template('index.html') # Retornamos la renderizacion de un doc html (mostrar en pantalla)

@app.route("/empresas", methods=["GET", "POST"]) 
def ver_empresas(): 
    print(request.data)
    return render_template('empresas.html', empresas = empresas)

@app.route("/puestos", methods=["GET", "POST"]) 
def ver_puestos(): 
    print(request.data)
    return render_template('puestos.html', puestos = empresas[0]["puestos"], empresa = empresas[0]["nombre"])

if __name__ == "__main__":
    app.run(debug=True)