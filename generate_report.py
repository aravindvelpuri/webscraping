# from scrape_sakshi import scrape_sakshi
# from scrape_eenadu import scrape_eenadu
# import pandas as pd
# from datetime import datetime

# def generate_combined_report():
#     sakshi_news = [{'title': x['title'], 'url': x['url'], 'source': 'Sakshi'} for x in scrape_sakshi()]
#     eenadu_news = [{'title': x['title'], 'url': x['url'], 'source': 'Eenadu'} for x in scrape_eenadu()]

#     all_news = sakshi_news + eenadu_news
#     df = pd.DataFrame(all_news)

#     df.drop_duplicates(subset=['title'], inplace=True)  # or use ['url']
#     df.sort_values(by='title', inplace=True)

#     filename = f"andhra_news_report_{datetime.now().strftime('%Y-%m-%d')}.csv"
#     df.to_csv(filename, index=False)
#     print(f"✅ Combined news report saved: {filename}")

# from scrape_sakshi import scrape_sakshi
# from scrape_eenadu import scrape_eenadu
# from utils.classify import classify_severity
# import pandas as pd
# from datetime import datetime

# def generate_combined_report():
#     sakshi_news = [{'title': x['title'], 'url': x['url'], 'source': 'Sakshi'} for x in scrape_sakshi()]
#     eenadu_news = [{'title': x['title'], 'url': x['url'], 'source': 'Eenadu'} for x in scrape_eenadu()]
#     all_news = sakshi_news + eenadu_news

#     # Classify severity
#     for article in all_news:
#         article["severity"] = classify_severity(article["title"])

#     df = pd.DataFrame(all_news)
#     df.drop_duplicates(subset=['title'], inplace=True)
#     df.sort_values(by='severity', inplace=True)

#     filename = f"andhra_news_report_{datetime.now().strftime('%Y-%m-%d')}.csv"
#     df.to_csv(filename, index=False)
#     print(f"✅ Combined news report saved: {filename}")
#     return df

from scrape_sakshi import scrape_sakshi
from scrape_eenadu import scrape_eenadu
from utils.classify import classify_severity
from utils.report_writer import generate_word_report
import pandas as pd
from datetime import datetime

SEEN_FILE = 'seen_titles.txt'

def load_seen_titles():
    try:
        with open(SEEN_FILE, 'r', encoding='utf-8') as f:
            return set(line.strip() for line in f)
    except FileNotFoundError:
        return set()

def save_seen_titles(titles):
    with open(SEEN_FILE, 'a', encoding='utf-8') as f:
        for title in titles:
            f.write(f"{title}\n")

def generate_combined_report():
    sakshi_news = [{'title': x['title'], 'url': x['url'], 'source': 'Sakshi'} for x in scrape_sakshi()]
    eenadu_news = [{'title': x['title'], 'url': x['url'], 'source': 'Eenadu'} for x in scrape_eenadu()]
    all_news = sakshi_news + eenadu_news

    seen_titles = load_seen_titles()
    new_news = [n for n in all_news if n['title'] not in seen_titles]

    for article in new_news:
        article['severity'] = classify_severity(article['title'])

    df = pd.DataFrame(new_news)
    if df.empty:
        print("⚠️ No new articles to process.")
        return None, None

    df.drop_duplicates(subset=['title'], inplace=True)
    df.sort_values(by='severity', inplace=True)

    save_seen_titles(df['title'].tolist())
    word_file = generate_word_report(df)
    print(f"✅ Word report saved: {word_file}")
    return df, word_file
