"""
1- Abrir la página de login.

2- Completar usuario y contraseña:

    Usuario: standard_user

    Contraseña: secret_sauce

3- Hacer clic en el botón de login.

4- Validar que el login fue exitoso:

    Que la URL contenga /inventory.html

    Que el título sea Swag Labs o que aparezca la palabra Products

5- Agregar el primer producto al carrito.

6- Esperar explícitamente a que aparezca el badge del carrito (.shopping_cart_badge) y confirmar que dice 1.

7- (Opcional pero recomendado): ingresar al carrito y verificar que el producto añadido esté en la lista.

8- Mostrar Test OK en consola si todo se completó con éxito.
"""

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

#driver.implicitly_wait(10)

try:
    #1- Abrir la página de login.
    driver.get("https://www.saucedemo.com")

    #2- Completar usuario y contraseña:
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")

    #3- Hacer clic en el botón de login.
    driver.find_element(By.ID, "login-button").click()

    #4- Validar que el login fue exitoso:
    assert "/inventory.html" in driver.current_url
    print("La URL contiene 'Inventory'")

    titulo_pag = driver.find_element(By.CSS_SELECTOR, ".app_logo").text
    print(f"El título de la página es {titulo_pag}")

    titulo_seccion = driver.find_element(By.CSS_SELECTOR, ".title[data-test='title']").text
    print(f"El título de la sección es {titulo_seccion}")

    #5- Agregar el primer producto al carrito.
    add_backpack = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

    #6- Esperar explícitamente a que aparezca el badge del carrito (.shopping_cart_badge) y confirmar que dice 1.

    #Version SIN espera explícita
    """
    cantidad_carrito = (driver.find_element(By.CLASS_NAME, "shopping_cart_badge")).text
    assert cantidad_carrito == "1"
    print (f"La cantidad en el carrito es {cantidad_carrito}")
    """

    #Version CON espera explícita (Requiere importar funciones en el encabezado)
    wait = WebDriverWait(driver, 5)

    badge = wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'shopping_cart_badge')))

    #7- (Opcional pero recomendado): ingresar al carrito y verificar que el producto añadido esté en la lista.
    carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    producto_carrito = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    assert producto_carrito == "Sauce Labs Backpack"
    print(f"El producto que se encuentra en el carrito es {producto_carrito}")

    #8- Mostrar Test OK en consola si todo se completó con éxito.
    print("Test OK")

except Exception as e:
    print(f"Test falló: {e}")

finally:
    driver.quit()













