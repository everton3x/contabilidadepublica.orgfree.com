#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Everton da Rosa'
SITENAME = 'Contabilidade Pública'
SITESUBTITLE = 'Ideias e reflexões sobre Contabilidade Pública'
SITEURL = 'https://everton3x.github.io/contabilidadepublica'
GITHUB_URL = 'https://github.com/everton3x/contabilidadepublica'

PATH = 'content'
OUTPUT_PATH = 'docs/'
PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['posts']
STATIC_PATHS = ['images', 'files']

TIMEZONE = 'America/Sao_Paulo'
DEFAULT_DATE_FORMAT = '%d/%m/%Y'

DEFAULT_LANG = 'pt'

GOOGLE_ANALYTICS = 'UA-81908417-1'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'))

# Social widget
SOCIAL = (('Facebook', 'https://facebook.com/everton3x'),
          ('Medium', 'https://medium.com/everton3x'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME = 'pelican-clean-blog'

# pelican-clean-blog config https://github.com/gilsondev/pelican-clean-blog
FACEBOOK_URL = 'http://facebook.com/everton3x'
