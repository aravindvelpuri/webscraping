from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def scrape_eenadu():
    url = "https://www.eenadu.net/andhra-pradesh"
    print(f"🌐 Fetching: {url}")

    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(options=options)
    driver.get(url)
    time.sleep(5)

    articles = []
    elements = driver.find_elements(By.CSS_SELECTOR, "aside.thumb-content-more.showmoredivs")

    print("🔍 Previewing Eenadu articles:")
    for el in elements:
        try:
            title = el.find_element(By.CSS_SELECTOR, "h3.article-title-rgt").text.strip()
            link = el.find_element(By.TAG_NAME, "a").get_attribute("href")
            if title and link:
                print(f"- {title}")
                articles.append({"title": title, "url": link})
        except Exception:
            continue

    driver.quit()
    print(f"✅ Eenadu: {len(articles)} articles found")
    return articles
