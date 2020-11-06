import feedparser

URL = ("http://rss.hankyung.com/new/news_main.xml", "http://rss.hankyung.com/new/news_economy.xml")


def crawl_rss(url_address):
    d = feedparser.parse(url_address)
    print(type(d))
    print(d.feed["title"])
    print(type(d.entries))
    print('~' * 80)
    for news in d.entries:
        print("title :", news.title)
        print("link :", news.link)
        print("description :", news.description)
        print('*' * 80)


def main():
    for url_address in URL:
        crawl_rss(url_address)
        print('_' * 80)


if __name__ == "__main__":
    main()
