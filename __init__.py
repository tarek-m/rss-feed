from bottle import *
import feedparser
import tkinter


@route('/')
def index():
    return static_file("index.html", root="")
@route('/rss' , method="GET")
def rss():
    NewsFeed = feedparser.parse("http://www.fifa.com/rss/index.xml")
    articles=[]
    for i in range(1,30):
        article={'title': NewsFeed["entries"][i]["title"],'link':NewsFeed["entries"][i]["link"]}
        articles.append(article)
    return json_dumps(articles)

@route('/<filename:re:.*\.css>')
def stylesheet(filename):
    return static_file(filename, root='')


def main():
    run(host='localhost', port=7002)

if __name__ == '__main__':
    main()