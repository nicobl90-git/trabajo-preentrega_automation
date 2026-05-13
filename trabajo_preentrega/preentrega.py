from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

wait = WebDriverWait(driver, 5)

try:
    #Navegar a la página de login de saucedemo.com
    driver.get("https://www.saucedemo.com")

    #Ingresar credenciales válidas (usuario: "standard_user", contraseña: "secret_sauce")
    input_username = driver.find_element(By.ID, "user-name").send_keys("standard_user")
    input_password = driver.find_element(By.ID, "password").send_keys("secret_sauce")

    #Validar login exitoso verificando que se haya redirigido a la página de inventario
    #Login automatizado con espera explícita y validación de /inventory.html y “Products/Swag Labs”.
    login_button = driver.find_element(By.ID, "login-button").click()
    assert "/inventory.html" in driver.current_url
    print ("La URL contiene 'Inventory'")

    #Verificar que el título de la página de inventario sea correcto
    titulo_pagina = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".app_logo"))).text
    titulo_seccion = driver.find_element(By.CSS_SELECTOR, ".title[data-test='title']").text
    print(f"El título de la página es {titulo_pagina} y la sección es {titulo_seccion}")

    #Comprobar que existan productos visibles en la página (al menos verificar la presencia de uno)
    producto_nombre = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    producto_precio = driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[1]/div[2]/div[2]/div").text
    print(f"Se encontró el siguiente producto: {producto_nombre} y su precio es {producto_precio}")

    #Validar que elementos importantes de la interfaz estén presentes (menú, filtros, etc.)
    assert wait.until(EC.visibility_of_element_located((By.ID, "react-burger-menu-btn")))
    print("Se encontró el menú sandwich")
    assert wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "select_container")))
    print("Se encontró el filtro para los productos")
    assert wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_container")))
    print("Se encontró el botón del carrito")

    #Añadir un producto al carrito haciendo clic en el botón correspondiente
    agregar_producto = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

    #Verificar que el contador del carrito se incremente correctamente
    cantidad_carrito = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))).text

    #Comprobar que el producto añadido aparezca correctamente en el carrito
    assert cantidad_carrito == "1"
    print(f"El carrito muestra el número {cantidad_carrito}")

    #Verifica ítem en carrito.
    carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_container").click()
    producto_carrito = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item_name"))).text
    assert producto_carrito == "Sauce Labs Backpack"
    print(f"El producto que se encuentra en el carrito es {producto_carrito}")

except Exception as e:
    print(f"Test falló: {e}")

finally:    
    driver.quit()


