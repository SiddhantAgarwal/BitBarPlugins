#!/usr/local/bin/python3
import concurrent.futures
import requests
import time
import feedparser
import re

urls = [
    ('http://feeds.reuters.com/reuters/INtopNews', 'Top'),
    ('http://feeds.reuters.com/reuters/INsportsNews', 'Sports'),
    ('http://feeds.reuters.com/reuters/INtechnologyNews', 'Tech'),
    ('https://news.ycombinator.com/rss', 'HackerNews')
]

def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext

def parse_feed(entry):
    parsed_feed = feedparser.parse(entry[0])
    return parsed_feed, entry[1]

def parse_reuter(parsed_feed):
    for entry in data.entries:
        print(entry.title.strip() + '|color=#FCF6F0')
        print(cleanhtml(entry.summary).strip() + '|color=#77B2A1 size=10 href={}'.format(entry.link.strip()))

def parse_hackernews(parse_feed):
    for entry in data.entries:
        print(entry.title.strip() + '|color=#FCF6F0 href={}'.format(entry.link.strip()))

print(':newspaper::small_red_triangle_down:')
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    future_to_url = {executor.submit(parse_feed, url_tuple): url_tuple for url_tuple in urls}
    for future in concurrent.futures.as_completed(future_to_url):
        try:
            data, title = future.result()
            print('---')
            print(title)
            if title == 'HackerNews':
                parse_hackernews(data)
            else:
                parse_reuter(data)    
        except Exception as exc:
            data = str(type(exc))