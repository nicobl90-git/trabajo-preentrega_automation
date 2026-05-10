# Inicialización
#Importamos las librerías necesarias y creamos una instancia de Chrome WebDriver.

from selenium import webdriver  #Importamos la librería que permite controlar el navegador
import time  #Para hacer pausas visibles (solo demo)

driver = webdriver.Chrome()  #Creamos la instancia del driver → abre una ventana de Chrome vacía

try:
    #Navegación
    #Abrimos la URL de Sauce Demo con el método get().
    driver.get('https://www.saucedemo.com')  #Navegamos a la URL de Sauce Demo (pantalla de login)
    
    #Validación
    #Verificamos el título de la página para confirmar la carga correcta.
    print('Título:', driver.title)  #Leemos el título de la pestaña → debería salir "Swaq Labs"
    assert driver.title == 'Swag Labs'  #Validamos que el título sea el esperado (asegura que cargó bien)
    
    time.sleep(2)  #Pausa de 2 s para que lo veas (luego la quitaremos)
finally:
    #Finalización
    #Cerramos el navegador con quit() para liberar recursos.
    driver.quit()  #Cierre limpio: mata la sesión y la ventana 

#Ejecutar desde la terminal con python3 Clase07/primer_script.py (tengo que especificar la carpeta porque este archivo no esta directamente dentro de Automation QA)
