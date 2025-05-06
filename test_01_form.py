from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def test_form_validation():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    # Заполняем поля формы
    driver.find_element(By.NAME, "first-name").send_keys("Иван")
    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")

    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    wait.until(lambda d: "alert-danger" in d.find_element(By.ID, "zip-code").get_attribute("class"))
    assert "alert-danger" in driver.find_element(By.ID, "zip-code").get_attribute("class")


    fields = [
        "first-name", "last-name", "address", "e-mail",
        "phone", "city", "country", "job-position", "company"
    ]
    for field in fields:
        field_status = driver.find_element(By.ID, field)
        assert "alert-success" in field_status.get_attribute("class")

    driver.quit()


test_form_validation()
