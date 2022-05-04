from locale import locale_encoding_alias
from operator import indexOf, itemgetter
from re import X
import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

'''Aca empiezan las funciones'''
#limpia una lista de elementos repetidos
def limpiar_lista_repetida (lista):
    resultado = []
    for valor in lista:
        if valor not in resultado:
            resultado.append(valor)
    return resultado

#cuenta el numero de coincidencias en una lista y devuelve otra lista con el resultado
def contador_lista (lista_llena):
    n = 0
    n2 = 0

    lista_limpia = limpiar_lista_repetida(lista_llena) # [encar, asu, encar, asu, mandioca]
    resultado2 = [0 for x in range(len(lista_limpia))]                                      #[2, 2, 1]
    for i, val in enumerate(lista_limpia):
        for index, value in enumerate(lista_llena):
            if lista_limpia[i] == lista_llena[index]:
                resultado2[i] += 1
    return resultado2


def busqueda(keyword):
    dash_dep_titulo = []
    dash_dep_subtitulo = []
    dash_dep_locacion = []
    #Aca metemos la keyword para hacer la busqueda
    ''' keyword = input("Ingresar busqueda: ")'''
    # URL para Scrapping de una tabla de datos
    URL = "https://es.linkedin.com/jobs/search?keywords=" + keyword + "&location=Paraguay&geoId=104065273&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0"

    options = Options()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    website = driver.get(URL)
    time.sleep(2)

    #Cabezera numero de trabajos
    n_trabajos = int(driver.find_element_by_css_selector('h1>span').get_attribute('innerText'))
    print(f"Numero de empleos: {n_trabajos}")

    #Loop para hacer scroll
    i = 0
    while i <= int(n_trabajos/25)+1: 
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        i = i + 1
        try:
            driver.find_element_by_xpath('/html/body/main/div/section/button').click()
            time.sleep(2)
        except:
            pass
            time.sleep(2)



    #Aca asignamos los valores de las ofertas de trabajo de html a unas variables para utilizar mas adelante
    lista_trabajos = driver.find_element_by_class_name("jobs-search__results-list") #Guardar todo el apartado de lista de trabajo
    trabajos = lista_trabajos.find_elements_by_tag_name("li") #Encontrar en lista_trabajos todos los elementos que tengan un tag <li>
    titulos = lista_trabajos.find_elements_by_class_name("base-search-card__title") #Encontrar titulos por su clase y guardar.
    subtitulos = lista_trabajos.find_elements_by_class_name("base-search-card__subtitle") #Encontrar la empresa que ofrece el empleo por su clase 
    subtitulo = [x.text for x in subtitulos] 
    locaciones = lista_trabajos.find_elements_by_class_name("job-search-card__location")
    locacion = [x.text.split(", ") for x in locaciones]

    #Determinamos en que posicion se encuentra el departamento y asignamos a nuevas listas que podemos utilizar para el dashboard
    for i, var in enumerate(trabajos):
        if len(locacion[i]) == 3:
            dash_dep_titulo.append(titulos[i])
            dash_dep_subtitulo.append(subtitulo[i])
            dash_dep_locacion.append(locacion[i][1])
        elif len(locacion[i]) == 2:
            dash_dep_titulo.append(titulos[i])
            dash_dep_subtitulo.append(subtitulo[i])
            dash_dep_locacion.append(locacion[i][0])
            ## Chau Paraguay
        '''elif len(locacion[i]) == 1:
            dash_dep_titulo.append(titulos[i])
            dash_dep_subtitulo.append(subtitulos[i])
            dash_dep_locacion.append(locacion[i][0])'''

    #Para enviar ya al dashboard
    #Lista Limpia departamentos
    dash_dep = limpiar_lista_repetida(dash_dep_locacion)
    #Contador de empletos por departamento
    dash_cont = contador_lista(dash_dep_locacion)

    #Para enviar ya al dashboard
    #Lista Limpia empleo
    dash2_dep = limpiar_lista_repetida(subtitulo)
    #Contador de empletos por departamento
    dash2_cont = contador_lista(subtitulo)

    lista_feliz = [dash_dep, dash_cont, dash2_dep, dash2_cont]
    return lista_feliz
#Impresion completa de la lista
'''for i in range(len(trabajos)):
    print(f"N: {i}")
    print(f"Titulos: {titulos[i].text}")
    print(f"Subtitulos: {subtitulos[i].text}")
    print(f"Locaciones: {locacion[i]}")

    print(f"------------------------------------------------------------")'''

'''# Impresion solo con departamentos
for i in range(len(dash_dep_titulo)):
    print(f"N: {i}")
    print(f"Titulos: {dash_dep_titulo[i].text}")
    print(f"Subtitulos: {dash_dep_subtitulo[i]}")
    print(f"Locaciones: {dash_dep_locacion[i]}")

    print(f"------------------------------------------------------------")'''


'''#Print no mas pa ver que onda.
print(dash_dep)
print(dash_cont)'''

'''print("--------------------------------------------------")

dash2_sub = limpiar_lista_repetida(dash_dep_subtitulo)
dash2_cont = contador_lista(dash_dep_subtitulo)

print(dash2_sub)
print(dash2_cont)

print("--------------------------------------------------")'''



