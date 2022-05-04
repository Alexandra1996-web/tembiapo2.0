# python -m flask run 'codigo para hacer funcionar en la terminal' 
from crypt import methods
from flask import Flask, render_template, url_for, request # Importamos las librerias a ser usadas
import requests
from codigo_feliz import *

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

@app.route("/empresas", methods=['GET', 'POST']) 
def ver_empresas():
    print(request.data)
    keyword = request.form['consulta']
    temp = busqueda(keyword)
    dash_dep = temp[0]
    print(dash_dep)
    dash_cont = temp[1]
    dash2_dep = temp[2]
    dash2_cont = temp[3]  
    return render_template('index.html', dash_dep = dash_dep, dash_cont = dash_cont, dash2_dep = dash2_dep, dash2_cont = dash2_cont)

@app.route("/puestos", methods=["GET", "POST"]) 
def ver_puesto(): 
    print(request.data)
    return render_template('puestos.html', puestos = empresas[0]["puestos"], empresa = empresas[0]["nombre"])

@app.route("/cuestionario") # Llamamos al metodo route y le pasamos el argumento de la url o slug que queremos que vaya
def cuestionario(): # Creamos la funcion inicio
    return render_template('cuestionario.html') 

if __name__ == "__main__":
    app.run(debug=True)