import feedparser


def read_address():
    address_list = list()
    with open("ohmynews_rss.txt", 'r', encoding='utf-8') as file:
        all_lines = file.readlines()
        for line in all_lines:
            title = line.split("|")[0].strip()
            link = line.split("|")[1].strip()
            # print(title, link)
            addr_dict = {"title": title, "link": link}
            address_list.append(addr_dict)
    return address_list


def crawl_rss(url_address):
    d = feedparser.parse(url_address)
    print(d.feed["title"])
    for news in d.entries:
        print("title :", news.title)
        print("link :", news.link)
        print("description :", news.description)
        print('*' * 80)


def main():
    address = read_address()
    for addr in address:
        print("=" * 80)
        print(addr["title"])
        print("=" * 80)
        crawl_rss(addr["link"])
        print("=" * 80)


if __name__ == "__main__":
    main()
