import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def test_example_domain(driver):
    driver.get('https://github.com')
    title_element = driver.find_element(By.ID, 'hero-section-brand-heading')
    assert title_element.text == 'Build and ship software on a single, collaborative platform', \
        f"Texto encontrado: {title_element.text}"