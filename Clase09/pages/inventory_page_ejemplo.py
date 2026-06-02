"""
Una vez que el usuario accede exitosamente a la aplicación, es redirigido a la página de inventario, donde puede ver los productos disponibles y realizar acciones como agregarlos al carrito o cerrar sesión. Esta pantalla también debe encapsularse en una clase, que llamaremos InventoryPage, ubicada en el archivo pages/inventory_page.py.

Esta clase tiene como objetivo abstraer todas las interacciones posibles en esa vista: desde obtener información visible (como el título o los productos), hasta realizar acciones (como agregar productos o navegar al carrito). Siguiendo el enfoque del Page Object Model, centralizamos los selectores y exponemos métodos expresivos que describen las acciones del usuario sin acoplar al test con la lógica interna de la interfaz.

"""


from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:
    _TITLE = (By.CLASS_NAME, "title")
    _PRODUCTS = (By.CLASS_NAME, "inventory_item")
    _ADD_BUTTONS = (By.CSS_SELECTOR, "button[data-test*='add-to-cart']")
    _CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    _CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    _MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    _LOGOUT_LINK = (By.ID, "logout_sidebar_link")
    def __init__(self, driver):
            self.driver = driver
            self.wait = WebDriverWait(driver, 10)
    def obtener_titulo(self):
            """Obtiene el título de la página de inventario."""
            return self.driver.find_element(*self._TITLE).text
        
    def obtener_productos(self):
            """Obtiene la lista de productos disponibles."""
            return self.driver.find_elements(*self._PRODUCTS)
        
    def agregar_primer_producto(self):
            """Añade el primer producto disponible al carrito."""
            primer_boton = self.driver.find_elements(*self._ADD_BUTTONS)[0]
            primer_boton.click()
            return self
        
    def obtener_contador_carrito(self):
        """Obtiene el número de productos en el carrito."""
    
        try:
            badge = self.driver.find_element(*self._CART_BADGE)
            return int(badge.text)
        except:
            return 0
        
    def ir_al_carrito(self):
        """Navega a la página del carrito."""
        self.driver.find_element(*self._CART_LINK).click()
    
        # Importación lazy para evitar dependencias circulares
        
        from pages.cart_page import CartPage
        return CartPage(self.driver)
            
        def hacer_logout(self):
                """Cierra la sesión del usuario."""
                self.driver.find_element(*self._MENU_BUTTON).click()
        
        logout_link = self.wait.until(
        EC.element_to_be_clickable(self._LOGOUT_LINK)
        )
        logout_link.click()
        from pages.login_page import LoginPage
        return LoginPage(self.driver)