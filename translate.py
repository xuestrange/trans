import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import os


def request(word):
    ua = UserAgent().random
    header = {"User-Agent": ua}
    url = f"https://dict.youdao.com/w/eng/{word}/#keyfrom=dict2.index"

    response = requests.get(url, header)

    if response.status_code == 200:
        return response.text
    else:
        return "request error"


def parse(html):
    soup = BeautifulSoup(html, features="lxml")
    try:

        eng_pronouce = soup.find('span', {'class': 'phonetic'}).string
        trans_container = soup.find('div', {'class': 'trans-container'})
        meaning = []
        for li in trans_container.findChildren("li", recursive=True):
            meaning.append(li.text)

        meaning = ''.join(str(item)+"\n" for item in meaning)
    except AttributeError:
        eng_pronouce = "None"
        meaning = "No meanings"
    return eng_pronouce, meaning


def is_word(string):
    if ' ' in string:
        return False
    else:
        return True


def trans_sentence(sentence):
    trans = os.popen(f"trans -b en:zh \"{sentence}\" ").read()
    return trans


def translate():
    clipboard = os.popen("xclip -o").read().strip()
    if is_word(clipboard):
        content = request(clipboard)
        trans_list = parse(content)
        return is_word(clipboard), clipboard, trans_list
    else:
        clipboard = clipboard.replace("\n ", " ")
        clipboard = clipboard.replace("-\n", "")
        clipboard = clipboard.replace("\n", " ")

        return is_word(clipboard), clipboard, trans_sentence(clipboard)


if __name__ == '__main__':
    result = translate()
    print(result)
