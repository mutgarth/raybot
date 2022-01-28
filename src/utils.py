from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def get_web_content(url):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://valorinveste.globo.com/cotacoes/")
    content = driver.page_source
    return content



