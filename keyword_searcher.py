__author__ = 'sam-ong'

import ast
import re
import glob
from constants import *


# @oaram message:string
# @desc Add Results to the text file
def add_result_match(message):
    with open("keyword searcher results.txt", "a") as results_file:
        results_file.write(message)
        results_file.write("\n<------------------------- NEXT MATCH ---------------------->\n")




# Main Script Logic
# STILL NOT WORKING... DONT KNOW WHY
for i in range(1, NUM_CONFESSIONS):

    filename = "confession-" + str(i)+".json"

    for keyword in SEARCH_KEYWORDS:
        print "File name:", filename
        with open("confessions/"+filename, "r") as infile:
            data = ast.literal_eval(infile.read())
            for entry in data["data"]:
                try:
                    message = entry["message"].lower()
                except KeyError:
                    print "Exception occurred, dict:", entry

                match_list = re.findall(keyword, message)

                if len(match_list) > 0:
                    add_result_match(message)
                    print message
                    print "Found a match"

    print "---------Next File--------"