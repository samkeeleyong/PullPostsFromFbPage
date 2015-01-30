__author__ = 'sam-ong'

import json
import requests
import ast
from constants import *
from string import Template


request_url= Template("$FACEBOOK_URL/$PAGE_ID/posts?" +
         "fields=message&" +
         "type=status&" +
         "limit=$POSTS_LIMIT&" +
         "access_token=$ACCESS_TOKEN").substitute(REQUEST_OPTIONS)


# @param request_url:string
#        URL to send an HTTP POST (e.g. graph.facebook.com/blah/blah)
# @return {}:json
#         Returned data from the HTTP POST
def request_posts(request_url):
    response = requests.get(request_url)
    return response.json()


# Main Script Logic
# TODO fails when there are no more posts, while condition to be changed
counter = 1
while True:
    data = request_posts(request_url)

    # write to file
    with open("confessions/confession-" + str(counter)+".json","w") as outfile:
        json.dump(data, outfile)

    # get link to the next page
    link = data["paging"]["next"]
    print "Done on page ", counter
    counter += 1