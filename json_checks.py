#verify if a library import is needed? does check exist?
import json

def is_json(myjson):
    with open(myjson) as file:
        try:
            json_object = json.load(file)
        except ValueError, e:
            return False

    return True

def jsondiff(json1,json2):

    #Check if files are jsons, if not return 1
    if not is_json(json1):
        print 'First file provided is not a json'
        return 1
    if not is_json(json2):
        print 'Second file provided is not a json'
        return 1

    with open(json1,'r') as f:
        json_1 = json.load(f)
    with open(json2,'r') as f:
        json_2 = json.load(f)

    #Match jsons keys and values
    json1_keys = json_1.keys()
    json2_keys = json_2.keys()

    if len(json1_keys) > len(json2_keys):
        print 'First json file has more keys than the second file'

    elif len(json1_keys) < len(json2_keys):
        print 'Second json file has more keys than the first file'
    else:
        print "Same amount of keys between the jsons"

    print "Matching keys and values:"
    for key1,key2 in json1_keys, json2_keys:
        if key1==key2
            if key1 != key2 or value1 != value2:
                print key1 + ':' + '' + value1 + ', ' + key2 + ':' + '' + value2