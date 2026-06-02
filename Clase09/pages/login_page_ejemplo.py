"""
Para comenzar a aplicar el patrón Page Object Model, vamos a crear nuestra primera clase de página: la correspondiente a la pantalla de login. Esta clase vivirá en el archivo pages/login_page.py, siguiendo la convención de mantener una clase por archivo y reflejar en el nombre su propósito funcional.

Este archivo encapsulará toda la lógica asociada a la página de inicio de sesión: desde su URL, pasando por los elementos que la componen, hasta los métodos que permiten interactuar con ella. De esta forma, cualquier cambio futuro en la interfaz de login (por ejemplo, un nuevo ID para el botón de ingreso) podrá manejarse modificando una sola clase, sin afectar directamente los tests.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    URL = "https://www.saucedemo.com/"

    _USER_INPUT = (By.ID, "user-name")
    _PASS_INPUT = (By.ID, "password")
    _LOGIN_BUTTON = (By.ID, "login-button")
    _ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def abrir(self):
        self.driver.get(self.URL)
        return self

    def completar_usuario(self, usuario: str):
        campo = self.wait.until(EC.visibility_of_element_located(self._USER_INPUT))
        campo.clear()
        campo.send_keys(usuario)
        return self

    def completar_clave(self, clave: str):
        campo = self.driver.find_element(*self._PASS_INPUT)
        campo.clear()
        campo.send_keys(clave)
        return self

    def hacer_clic_login(self):
        self.driver.find_element(*self._LOGIN_BUTTON).click()
        return self

    def login_completo(self, usuario, clave):
        self.completar_usuario(usuario)
        self.completar_clave(clave)
        self.hacer_clic_login()
        return self

    def esta_error_visible(self) -> bool:
        try:
            self.wait.until(EC.visibility_of_element_located(self._ERROR_MESSAGE))
            return True
        except:
            return False

    def obtener_mensaje_error(self) -> str:
        if self.esta_error_visible():
            return self.driver.find_element(*self._ERROR_MESSAGE).text
        return ""


"""
¿Por qué cada sección?

URL: centraliza el punto de entrada

Locators: en variables privadas (_MAYÚSCULAS), único lugar a editar si cambian atributos

Constructor: inyecta driver desde el fixture, permitiendo usar cualquier navegador

Acciones de alto nivel: describen "qué" hace el usuario, no "cómo" (olvídate de selectores en tus tests)

Helpers de aserción: pequeños métodos para consultas, pero sin asserts dentro de la clase

"""