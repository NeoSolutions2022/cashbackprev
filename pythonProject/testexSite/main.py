from time import sleep

import undetected_chromedriver as uc

driver = uc.Chrome()
driver.get("https://www.nowsecure.nl")

sleep(5)

input("aa")

driver.quit()
