from selenium import webdriver
#utilizo el driver para despues guardarlo en una variable
#esta variable tendra todo lo que tenga webdriver para comunicarse con el navegador

from webdriver_manager.chrome import ChromeDriverManager
#Traigo el driver para el navegador que quiero trabajar

from selenium.webdriver.chrome.service import Service
#Este servicio recibe el chrome driver manager y me instala la version correcta segun mi navegador

#Otros from
#from selenium.webdriver.common.by import By #para localizar los elementos
#from selenium.webdriver.common.keys import Keys #para usar el enter
#from selenium.webdriver.support.ui import WebDriverWait #para generar esperas explicitas


#puedo crear tambien condiciones esperadas para despues utilizarlas en el codigo. Por ejemplo:
# from selenium.webdriver.support import expected_conditions as EC

#creo una variable para los servicios
service = Service(ChromeDriverManager().install())
#esto me instala la version correcta del driver para mi navegador y me evita hacerlo manualmente cuando se actualiza el navegador

#voy a crear una variable para darle los poderes y que reciba los servicios
driver = webdriver.Chrome(service=service)

#CON ESTO YA PUEDO CONTROLAR EL NAVEGADOR


#driver.implicitly_wait(10) #ejecuta a encontrar todo lo que esta abajo. Si lo encuentra antes de los 10 segundos, sigue con el siguiente.

#wait = WebDriverWait(driver, 10) #creo una variable para generar esperas explicitas. El primer parametro es el driver y el segundo es el tiempo de espera

#voy a usar el metodo GET para abrir una URL
driver.get("https://www.google.com")
#puedo usar el comando "python (nombre del archivo).py" para ejecutar el codigo y se va a abrir el navegador con la pagina de google

#voy a locarlizar el campo busqueda de Google
input_google = driver.find_element(By.NAME, "q") #puedo hacerlo por name, id, class, etc.

#puedo usar input_google = wait.until() para generar espera
#tambien puedo crearle una condicion desde el header y pasarle otro metodo. Por ejemplo:
# input_google = wait.until(
#     EC.presence_of_element_located((By.NAME, "q"))   siendo el EC (Expected conditions) definido en el encabezado

#para pasar un string como valor, necesito usar el metodo send_keys
input_google.send_keys("Selenium")

#uso el metodo Keys.return para simular el enter y hacer la busqueda
input_google.send_keys(Keys.RETURN)

driver.quit() #cierra sesion y consume menos recursos

#-----------------------------

#Puedo poner todo dentro de un try/except y ponerle un finally para cerrar el navegador

"""
try: 
    input_google = wait.until(
        EC.presence_of_element_located((By.NAME, "q"))
    )
    input_google.send_keys("Selenium")
    input_google.send_keys(Keys.RETURN)
except Exception as e:
    print(f"Ocurrio un error: {e}")

finally:
    driver.quit()

"""

#ESTO SE EJECUTO CON SELENIUM PERO TAMBIEN DEBEMOS PROBARLO CON PYTEST PARA VER SI FUNCIONA CORRECTAMENTE Y SI SE INTEGRA BIEN CON EL FRAMEWORK DE PRUEBAS.

#-----------------------------

#Luego de crear los archivos conftest y test_, tomando parte de los encabezados anteriores, puedo cambiar la estructura del codigo para que se adapte a pytest. Para eso, voy a crear una funcion y dentro de esa funcion voy a poner el codigo que tengo hasta ahora. Ademas, voy a usar el fixture que cree en el archivo conftest.py para usar el driver.
#Por eso aparece mucho el chrome_driver. Proviene de los otros archivos

"""
def test_google_search(chrome_driver):
    wait = WebDriverWait(chrome_driver, 10)
    chrome_driver.get("https://www.google.com")

    try:
    input_google = wait.until(
        EC.presence_of_element_located((By.NAME, "q"))
    )
    input_google.send_keys("Selenium")
    input_google.send_keys(Keys.RETURN)
    except Exception as e:
        print(f"Ocurrio un error: {e}") 
"""