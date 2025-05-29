# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# import time
# import csv
# from datetime import datetime

# def scrape_sakshi():
#     url = "https://www.sakshi.com/tags/andhra-pradesh"
#     print(f"🌐 Fetching: {url}")

#     options = Options()
#     options.add_argument("--headless")
#     options.add_argument("--disable-gpu")
#     options.add_argument("--no-sandbox")

#     driver = webdriver.Chrome(options=options)
#     driver.get(url)
#     time.sleep(5)

#     # Save full HTML for inspection
#     with open("sakshi_debug.html", "w", encoding="utf-8") as f:
#         f.write(driver.page_source)

#     # Use BeautifulSoup for flexible parsing
#     from bs4 import BeautifulSoup
#     soup = BeautifulSoup(driver.page_source, "html.parser")
#     driver.quit()

#     articles = []
#     print("🔍 Previewing Sakshi articles:")

#     for article in soup.select("a.title"):
#         title = article.get_text(strip=True)
#         link = article.get("href")
#         if title and link:
#             if not link.startswith("http"):
#                 link = "https://www.sakshi.com" + link
#             print(f"- {title}")
#             articles.append({
#                 "title": title,
#                 "url": link
#             })

#     print(f"✅ Sakshi: {len(articles)} articles found")
#     return articles

# def save_articles_to_csv(articles, filename):
#     with open(filename, mode='a', newline='', encoding='utf-8') as file:
#         writer = csv.writer(file)
#         for article in articles:
#             writer.writerow([datetime.now().date(), "Sakshi", article["title"], article["url"]])

# if __name__ == "__main__":
#     articles = scrape_sakshi()
#     if articles:
#         filename = f"andhra_news_report_{datetime.now().date()}.csv"
#         save_articles_to_csv(articles, filename)
#         print(f"✅ Saved to {filename}")
#     else:
#         print("⚠️ No articles to save.")

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup

def scrape_sakshi():
    url = "https://www.sakshi.com/tags/andhra-pradesh"
    print(f"🌐 Fetching: {url}")

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(options=options)
    driver.get(url)
    time.sleep(5)

    soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()

    articles = []
    print("🔍 Previewing Sakshi articles:")

    for article in soup.select("a.title"):
        title = article.get_text(strip=True)
        link = article.get("href")
        if title and link:
            if not link.startswith("http"):
                link = "https://www.sakshi.com" + link
            print(f"- {title}")
            articles.append({"title": title, "url": link})

    print(f"✅ Sakshi: {len(articles)} articles found")
    return articles
