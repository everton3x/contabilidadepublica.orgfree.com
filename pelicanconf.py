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
DEFAULT_DATE = 'fs'


DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True
USE_FOLDER_AS_CATEGORY = False

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Everton da Rosa', 'https://everton3x.github.io/'),
		('Hello World', 'https://everton3x.github.io/helloworld/'),
        ('Contabilidade Pública', 'https://everton3x.github.io/contabilidadpublica'),
        ('Fórum sobre Contabilidade Pública', 'http://www.contabeis.com.br/forum/foruns/8/contabilidade-publica/')
)

# Social widget
SOCIAL = (('Facebook', 'https://facebook.com/everton3x'),
			('Twitter', 'https://twitter.com/everton3x'),
          ('Medium', 'https://medium.com/everton3x'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

MENUITEMS = (('Início', 'index.html'),
	('Categorias', 'categories.html'),
	('Tags', 'tags.html'),
	('Autores', 'authors.html'),
	('Arquivos', 'archives.html')
)

# attila
THEME = 'attila'
HEADER_COVER = 'static/pexels-photo-169657-1.jpeg'
#HEADER_COLOR = 'black'
AUTHORS_BIO = {
  "everton da rosa": {
    "name": "Everton da Rosa",
    "cover": "https://pt.gravatar.com/userimage/2318180/0a175cf735e882a8c81d12d05952842c.png",
    "image": "https://pt.gravatar.com/userimage/2318180/0a175cf735e882a8c81d12d05952842c.png",
    "website": "https://everton3x.github.io",
    "location": "Três de Maio - Rio Grande do Sul - Brasil",
    "bio": "Contador Público Municipal e apaixonado por programação."
  }
}
