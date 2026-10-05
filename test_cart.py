import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_cart():
    driver = webdriver.Chrome()

    try:
        driver.get("https://www.saucedemo.com/")

        usuario = driver.find_element(By.ID,"user-name")
        password = driver.find_element(By.ID,"password")
        button_login = driver.find_element(By.ID,"login-button")
                
        usuario.send_keys("standard_user")
        password.send_keys("secret_sauce")
        button_login.click()
        
        #Verificacion:
        #Añadir un producto al carrito haciendo clic en el botón correspondiente
        cart = driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket")
        cart.click()
        #Verificar que el contador del carrito se incremente correctamente
        contador_cart = driver.find_element(By.CLASS_NAME,"shopping_cart_badge")
        assert contador_cart.text == "1"

        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

        #Navegar al carrito de compras(Falta esto)
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        driver.get("https://www.saucedemo.com/cart.html")

        nav_cart = driver.find_element(By.CLASS_NAME, "inventory_item_name")
        assert nav_cart.text == "Sauce Labs Fleece Jacket"

    finally:
        driver.quit()