from conftest import *


driver = webdriver.Edge()
driver.get('https://pro.guap.ru')
xpath('//a[text()="Кабинет"]/parent::li').click()
xpath('//input[@id="username"]').send_keys('camat2004@yandex.ru')
xpath('//input[@id="password"]').send_keys('11021982')
xpath('//input[@name="login"]').click()
driver.get('https://lms.guap.ru/login/index.php')
xpath('//img[@class="eta-login"]').click()
time.sleep(10)




