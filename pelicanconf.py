#AUTHOR = 'Vic'
SITENAME = 'Vic Simeone'
#SITESUBTITLE = ''
SITEURL = ''

PATH = "source"
# ARTICLES_PATH is relave to PATH
ARTICLE_PATHS = ["articles"]

# TIMEZONE = 'US/Eastern'

DEFAULT_LANG = 'en'
DEFAULT_CATEGORY = 'bloggity blog'
USE_FOLDER_AS_CATEGORY = False

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Python.org", "https://www.python.org/"),
)

# Social widget
SOCIAL = (
    ("GitHub", "https://github.com/oSquat"),
    ("LinkedIn", "https://www.linkedin.com/in/vicsimeone")
)
# adds a "fork me" banner
#GITHUB_URL = "http://github.com/oSquat/"

DEFAULT_PAGINATION = 10

PAGE_ORDER_BY='date'
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = True

SUMMARY_MAX_PARAGRAHS = 0

MENUITEMS=[('home', '/')]

# There aren't multiple authors so we don't want a page for authors
AUTHOR_SAVE_AS = ''
CATEGORY_SAVE_AS = ''

THEME = './themes/skeleton'

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'markdown.extensions.toc': {},
        'markdown.extensions.def_list': {},
    },
    'output_format': 'html5'
}
