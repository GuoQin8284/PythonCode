import time

from driver.driver import SetupDriver

driver = SetupDriver().setupDriver()

driver.start_activity("com.wandoujia.phoenix2","com.pp.assistant.activity.PPMainActivity")
time.sleep(5)

print(driver.current_package)
print(driver.current_activity)
driver.background_app(5)
print(driver.current_package)
print(driver.current_activity)

print(driver)
driver.close_app()
print(driver)

driver,quit()

print(driver)