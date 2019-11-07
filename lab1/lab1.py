from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
sites = []
openedsites = []
driver = webdriver.Firefox()
def init():
    with open("sites.txt","r") as f:
        for line in f.readlines():
            sites.append(line)

def open_and_focus_new_tab():
    driver.execute_script("window.open()")
    driver.switch_to.window(driver.window_handles[len(openedsites)])

def random_open():
    count = len(sites)
    for i in range(0,count):
        open = random.choice(sites)
        driver.get(open)
        openedsites.append(open)
        sites.remove(open)
        open_and_focus_new_tab()
    driver.close()
    print("All tabs were opened!")
    time.sleep(5)

def close_everything():
    print("Closing tabs")
    temp_list = openedsites.copy()
    temp_list.reverse()
    for site in temp_list:
        # Закрываем все вкладки в обратном порядке
        driver.switch_to.window(driver.window_handles[openedsites.index(site)])
        openedsites.remove(site)
        driver.close()
        time.sleep(1)
    print("All closed")

if __name__ == "__main__":
    init()
    random_open()
    close_everything()