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

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
# theme
THEME = "themes/Flex"

# Menu items
MENUITEMS = (
    ("About", "/pages/about.html"),
    ("Portfolio", "/pages/portfolio.html"),
    ("Blog", "/category/blog.html"),
)


STATIC_PATHS = ['images', 'files']
PYGMENTS_STYLE = 'monokai'