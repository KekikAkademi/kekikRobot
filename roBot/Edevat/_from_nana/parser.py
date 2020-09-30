# https://github.com/pokurt/Nana-Remix

import html
import re

def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    return re.sub(cleanr, '', raw_html)

def escape_markdown(text):
    """Helper function to escape telegram markup symbols."""
    escape_chars = r'\*_`\['
    return re.sub(r'([%s])' % escape_chars, r'\\\1', text)

def mention_html(user_id, name):
    return u'<a href="tg://user?id={}">{}</a>'.format(user_id, html.escape(name))

def mention_markdown(user_id, name):
    return u'[{}](tg://user?id={})'.format(escape_markdown(name), user_id)