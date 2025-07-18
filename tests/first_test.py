from selenium import webdriver

def test_page_title():
    browser = webdriver.Chrome()  # ¡Sin ruta hardcodeada!
    browser.get('https://github.com')
    title_element = browser.find_element(By.ID, 'hero-section-brand-heading')
    assert "Build and ship software" in title_element.text
    browser.quit()