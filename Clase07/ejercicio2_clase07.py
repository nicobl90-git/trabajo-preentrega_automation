"""
Actividad 2 · Explora el inventario

Tras el login, valida que el título (div.header_secondary_container .title) sea "Products".

Confirma que aparece al menos un div.inventory_item.

Muestra en consola el nombre y precio del primer producto.

"""

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try: 
    driver.get("https://www.saucedemo.com")
    input_username = driver.find_element(By.ID , "user-name" )
    input_username.send_keys("standard_user")
    input_password = driver.find_element(By.ID , "password" )
    input_password.send_keys("secret_sauce")
    input_password.send_keys(Keys.RETURN)

    assert "/inventory.html" in driver.current_url
    print("Test OK")

    titulo = driver.find_element(By.CSS_SELECTOR, "div.header_secondary_container .title").text
    assert titulo == 'Products'
    print('Título de sección OK →', titulo)
    
    #Voy a validar que encuentre al menos un div.inventory_item
    productos = driver.find_element(By.CSS_SELECTOR, "div.inventory_item")
    print("Se encontró al menos un producto")

    #Voy a tomar su nombre y precio a partir de findelement y su clase correspondiente
    producto_nombre = productos.find_element(By.CLASS_NAME, "inventory_item_name").text
    producto_precio = productos.find_element(By.CLASS_NAME, "inventory_item_price").text
    print(f"El primer producto es {producto_nombre} y su precio es {producto_precio}")

finally:
    driver.quit()






