"""
Actividad 1 · Script de login

Navega a https://www.saucedemo.com

Ingresa standard_user / secret_sauce.

Verifica que la URL contenga /inventory.html.

Imprime "Test OK" si pasa.

Reto extra: coloca la validación del título justo después de la redirección.

"""

#Primero el driver
from selenium import webdriver
#Segundo el manager del navegador que voy a usar
from webdriver_manager.chrome import ChromeDriverManager
#Tercero el servicio que recibe el manager y actualiza el driver correspondiente (me ahorra hacerlo manualmente)
from selenium.webdriver.chrome.service import Service

#Como voy a usar el metodo Find By y el metodo Keys, tengo que importarlos acá también
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#creo una variable para los servicios e instalo la version del driver correspondiente 
service = Service(ChromeDriverManager().install())

#creo una variable para el driver
driver = webdriver.Chrome(service=service)



#--------Empiezo a redactar el cuerpo principal del script

try: 
    #Uso el metodo GET para abrir la URL 
    driver.get("https://www.saucedemo.com")
    
    #Localizo el primer campo de login de la pagina usando la variable input_username y el metodo find_element
    input_username = driver.find_element(By.ID , "user-name" )

    #Le ingreso el username que quiero con el metodo send_keys
    input_username.send_keys("standard_user")

    #Localizo el segundo campo de login de la misma forma que antes
    input_password = driver.find_element(By.ID , "password" )

    #Le ingreso el password igual que antes
    input_password.send_keys("secret_sauce")

    #uso el metodo Keys.return para simular el enter dentro del campo password
    input_password.send_keys(Keys.RETURN)

    #Validamos la URL utilizando "assert" 
    #sirve para corroborar si una condición es verdadera, si no lo es, el script se detiene y muestra un error
    assert "/inventory.html" in driver.current_url
    print("Test OK")

    #Valido el título de la página para confirmar que se redirigió correctamente
    titulo = driver.find_element(By.CSS_SELECTOR, "div.header_secondary_container .title").text
    assert titulo == 'Products'
    print('Título de sección OK →', titulo)
    
finally:
    #Cierro el navegador
    driver.quit()






