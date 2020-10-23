# Eve Travers

import json

# Takes a json object as an argument and 
# returns a list of dicts corralating to the input
# sorted such that child nodes appear after their parents.
def sortCategoriesForInsert(inputJson):

    jsonDict = json.load(inputJson)

    outputJson = []
    # Search for all json data that are roots
    for data in jsonDict:
        if data["parent_id"] == None:
            # Add data and all of its children to outputJson
            outputJson.extend(addJson(data, jsonDict))

    return outputJson


# Helper function that returns the json data of the given entry
# and all of its children
def addJson(toAdd, inputJson):
    output = [toAdd]

    currentId = toAdd["id"]

    # Loop through all json data searching for children of toAdd
    # Recursivly call addJson for each of its children
    for data in inputJson:
        if data["parent_id"] == currentId:
            output.extend(addJson(data, inputJson))

    return output
