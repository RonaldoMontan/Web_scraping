from selenium import webdriver

navegador = webdriver.Chrome()

navegador.get('https://www.youtube.com/')

elemento = navegador.find_element_by_tag_name('input')


print(elemento)