from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import selenium.common.exceptions as exceptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import re
import time

driver = webdriver.Firefox()
wait = WebDriverWait(driver, 10)
TEST_SEARCHES = ["Тестирование", "Эффективное тестирование", "Эффективное тестирование программ"]

# Поиск
def search(text):
    search_line = driver.find_element_by_class_name("gLFyf.gsfi")
    search_line.clear()
    search_line.send_keys(text+Keys.ENTER)
    time.sleep(1.5)

# Смена страницы
def change_page(new_page = 1):
    driver.find_element_by_xpath(".//table[@id=\"nav\"]/tbody/tr/td["+str(new_page+1)+"]/a").click()
    time.sleep(1.5)

# Получение всех ссылок на странице
def get_all_links_on_page(search_text, page = 1):
    search(search_text) 
    if (page > 1):
        change_page(page)
    results = driver.find_elements_by_class_name("r")
    links = []
    for result in results:
        links.append(result.find_element_by_tag_name("a").get_attribute("href"))
    return links

# Получение количества результатов
def get_results_count(search_text):
    search(search_text)
    result_count = driver.find_element_by_id("resultStats")
    results = re.search(r"( {1}\d{1,3})+",result_count.text)
    return results.group(0)

# Выполнение первой части задания
def get_links_count():
    print("Результатов поиска по запросам:")
    print(TEST_SEARCHES[0] + " -" + get_results_count(TEST_SEARCHES[0]))
    print(TEST_SEARCHES[1] + " -" + get_results_count(TEST_SEARCHES[1]))
    print(TEST_SEARCHES[2] + " -" + get_results_count(TEST_SEARCHES[2]))

# Пересечение списков
def intersection(l1, l2):
    intersection = []
    for elem in l1:
        if elem in l2:
            intersection.append(elem)
    return intersection

# Обработка пересечения двух списков с третьим
def get_lists_intersections(first, second, all):
    first_intersection = intersection(first,all)
    second_intersection = intersection(second,all)

    return (first_intersection, second_intersection)
    
# Выполнение второй части задания
def get_links_repeats():
    all_links = get_all_links_on_page(TEST_SEARCHES[2])
    links_on_first_request = []
    links_on_second_request = []
    # Ищем ссылки на трех страницах первого и второго запроса
    for i in range(1,4):
        links_on_first_request.extend(get_all_links_on_page(TEST_SEARCHES[0],i))
        links_on_second_request.extend(get_all_links_on_page(TEST_SEARCHES[1],i))
    # Находим пересечения
    intersections = get_lists_intersections(links_on_first_request,links_on_second_request,all_links)
    # Выводим информацию 
    print("Количество пересечений для \""+TEST_SEARCHES[0]+"\": "+str(len(intersections[0])))
    print("Пересечения \""+TEST_SEARCHES[2]+"\" с \""+TEST_SEARCHES[0] + "\": "+str(intersections[0]))
    print("Количество пересечений для \""+TEST_SEARCHES[1]+"\": "+str(len(intersections[1])))
    print("Пересечения \""+TEST_SEARCHES[2]+"\" с \""+TEST_SEARCHES[1] + "\": "+str(intersections[1]))

        

if __name__ == "__main__":
    driver.get("https://www.google.com")
    get_links_count()
    get_links_repeats()
    driver.close()
    
    