__author__ = 'sam-ong'
import glob

FACEBOOK_URL = "https://graph.facebook.com"
NDMU_CONFESSIONS_PAGE_ID = "395931383856469"
ACCESS_TOKEN = "PUT YOUR ACCESS TOKEN HERE"

REQUEST_OPTIONS = {
    "FACEBOOK_URL": FACEBOOK_URL,
    "PAGE_ID": NDMU_CONFESSIONS_PAGE_ID,
    "ACCESS_TOKEN": ACCESS_TOKEN,
    "POSTS_LIMIT": 100
}

# Keyword searcher constants

NUM_CONFESSIONS = len(glob.glob1("confessions", "*.json"))
SEARCH_KEYWORDS = ["sam keeley ong",
                   "samuel",
                   "sam-liker"]