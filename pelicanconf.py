AUTHOR = 'Malik'
SITENAME = 'malikblog'
SITEURL = 'https://malikblogsite.netlify.app/'
SITETITLE = 'Abdulmalik Ibikunle'
SITESUBTITLE = 'DevOps Engineer'

PATH = "content"

TIMEZONE = 'Europe/Rome'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


# Social widget
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/abdulmalik-ibikunle-8a6894177/'),
          ('github', 'https://github.com/malikhq'),
          ("twitter", "https://x.com/malik0x"))


# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
# theme
THEME = "themes/Flex"

# Menu items
MAIN_MENU = True

MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),
             ('Portfolio', '/portfolio.html'),)
             


FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"


STATIC_PATHS = ['images', 'files']
PYGMENTS_STYLE = 'monokai'

DEFAULT_PAGINATION = 10

LINK_PAGINATION = True

SIDE_CATEGORY = True

SIDE_TAG_CLOUD = True

RECENT_PAGES = True

DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True
