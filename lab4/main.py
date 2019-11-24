from selenium import webdriver

driver = webdriver.Firefox()
BLOG_URL = "https://sprungmarker.de/"
TAG_CLOUD = []
posts = []
def read_tag_cloud():
    tag_cloud_links = driver.find_elements_by_class_name("tag-cloud-link")
    for link in tag_cloud_links:
        TAG_CLOUD.append(link.text.lower())

def find_all_posts():
    links = driver.find_elements_by_xpath("//h3[@class=\"entry-title\"]/a")
    for link in links:
        posts.append(link.get_attribute("href"))

def check_tags_in_cloud(post):
    print("Проверка тэгов для "+post)
    driver.get(post)
    post_tags = []
    for tag in driver.find_elements_by_xpath("//span[@class=\"cat-links\"]/a"):
        post_tags.append(tag.text.lower())
    print("Тэги поста: "+ str(post_tags))
    for tag in post_tags:
        if tag in TAG_CLOUD:
            print("Тэг "+tag+" есть в облаке тэгов")
        else:
            print("Тэга "+tag+" нет в облаке тэгов")
    

if __name__ == "__main__":
    driver.get(BLOG_URL)
    read_tag_cloud()
    print("Облако тэгов на сайте "+BLOG_URL+": "+str(TAG_CLOUD))
    find_all_posts()
    for post in posts:
        check_tags_in_cloud(post)
    driver.close()
