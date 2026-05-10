"""
Actividad 3 · Carrito rápido

Haz clic en "Add to cart" del primer producto.

Verifica que el contador del carrito muestre 1.

Navega al carrito y comprueba que el producto añadido está listado.

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
    
    productos = driver.find_element(By.CSS_SELECTOR, "div.inventory_item")
    print("Se encontró al menos un producto")

    producto_nombre = productos.find_element(By.CLASS_NAME, "inventory_item_name").text
    producto_precio = productos.find_element(By.CLASS_NAME, "inventory_item_price").text
    print(f"El primer producto es {producto_nombre} y su precio es {producto_precio}")

    #Voy a identificar el botón "Add to cart" y lo selecciono 
    boton_addtocart = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").send_keys(Keys.RETURN)
    
    #Voy a validar que aparezca "1" en el carrito
    cantidad_carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert cantidad_carrito == "1"
    print(f"El carrito muestra el número {cantidad_carrito}")


finally:
    driver.quit()






