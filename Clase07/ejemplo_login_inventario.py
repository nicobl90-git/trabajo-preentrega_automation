from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
options = Options()
options.add_argument('--start-maximized') # Opcional: ventana grande
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(5) # Espera implícita profesional
try:
    # 1) Login
    driver.get('https://www.saucedemo.com')
    driver.find_element(By.ID, 'user-name').send_keys('standard_user')
    driver.find_element(By.ID, 'password').send_keys('secret_sauce')
    driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()

    # 2) Validar que estamos en inventario
    assert '/inventory.html' in driver.current_url

    # 3) Verificar título de sección
    titulo = driver.find_element(By.CSS_SELECTOR,
    'div.header_secondary_container .title').text
    assert titulo == 'Products'
    print('Título de sección OK →', titulo)

    # 4) Contar productos visibles
    productos = driver.find_elements(By.CLASS_NAME, 'inventory_item')
    print(f'Se encontraron {len(productos)} productos.')

    # 5) Añadir el primer producto al carrito
    productos[0].find_element(By.TAG_NAME, 'button').click()

    # 6) Confirmar que el badge del carrito muestra 1
    badge = driver.find_element(By.CLASS_NAME,
    'shopping_cart_badge').text
    assert badge == '1'
    print('Carrito OK →', badge)
finally:
 driver.quit()

"""
¿Qué hace cada bloque?

Configuración

    Todo lo referente a ventana y tiempos de espera.

    Inicializa el navegador Chrome

    Maximiza la ventana

    Establece espera implícita de 5 segundos

Login

    Rellena usuario y contraseña usando IDs y CSS.

    Abre la URL de SauceDemo

    Localiza campos por ID

    Envía credenciales con send_keys()

Verificaciones

    Comprueba el estado de la aplicación tras acciones.

    Confirma URL del inventario

    Verifica título "Products"

    Cuenta productos visibles

Interacciones

    Realiza acciones y valida resultados.

    Añade primer producto al carrito

    Comprueba que el contador muestra "1"

    Imprime confirmaciones en consola




"""