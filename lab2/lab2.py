from selenium import webdriver
import time

driver = webdriver.Firefox()
var_site = "https://www.artlebedev.ru/case/"
test_text = "ПроВерОЧНый ТеКст"
links = ["ВЕРХНИЙ РЕГИСТР","нижний регистр","Заглавные Буквы","Первая заглавная","иНВЕРСИЯ рЕГИСТРА"]
assert_lines = {
    "ВЕРХНИЙ РЕГИСТР":test_text.upper(),
    "нижний регистр":test_text.lower(),
    "Заглавные Буквы":test_text.title(),
    "Первая заглавная":test_text.capitalize(),
    "иНВЕРСИЯ рЕГИСТРА":test_text.swapcase()
}

def check_result(line, key):
    print("Проверка по ключу "+key+":")
    assert line == assert_lines[key], "Неправильный вывод"
    print("Правильно")

def start_test():
    driver.find_element_by_id("source").send_keys(test_text)
    for link in links:
        elem = driver.find_element_by_link_text(link)
        elem.click()
        res_text = driver.find_element_by_id("target").get_attribute("value")
        check_result(res_text,link)


if __name__ == "__main__":
    driver.get(var_site)
    start_test()
    time.sleep(10)
    driver.close()