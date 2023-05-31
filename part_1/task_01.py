import re


def domain_name(url):
    result = re.search(r'(https?://|www.)([\w-]+)', url)
    return result[0].replace('www', ''). \
        replace('http:', ''). \
        replace('https:', ''). \
        replace('.', ''). \
        replace('/', '')


if __name__ == "__main__":
    assert domain_name("http://google.com") == "google"
    assert domain_name("http://google.co.jp") == "google"
    assert domain_name("www.xakep.ru") == "xakep"
    assert domain_name("https://youtube.com") == "youtube"
