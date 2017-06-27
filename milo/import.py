#!/usr/bin/env python

#!/usr/bin/env python
import json
    
text = """{
	"_index": 0,
	"_members": [{
		"name": "pro",
		"type": "object",
		"indexes": [0]
	}, {
		"name": "impt",
		"type": "object",
		"indexes": [0]
	}],
	"pro": [{
		"_index": 0,
		"_members": [{
			"name": "pra",
			"type": "object",
			"indexes": [1, 2]
		}, {
			"name": "insp",
			"type": "object",
			"indexes": [1, 2]
		}],
		"pra": [{
			"_index": 1,
			"_members": [{
				"name": "facil",
				"type": "object",
				"indexes": [0]
			}],
			"facil": [{
				"_index": 0,
				"_members": [{
					"name": "addr",
					"type": "object",
					"indexes": [0]
				}, {
					"name": "name",
					"type": "field"
				}],
				"addr": [{
					"_index": 0,
					"_members": [{
					   "name": "name",
					   "type": "field"
                  }, {
                  "name": "line1",
						"type": "field"
					}, {
						"name": "line2",
						"type": "field"
					}, {
						"name": "state",
						"type": "field"
					}, {
						"name": "zip",
						"type": "field"
					}],
					"line1": null,
					"line2": null,
					"state": null,
					"zip": null
				}]
			}]
		}, {
			"_index": 2,
			"_members": [{
				"name": "facil",
				"type": "object",
				"indexes": [0]
			}],
			"facil": [{
				"_index": 0,
				"_members": [{
					"name": "addr",
					"type": "object",
					"indexes": [0]
				}, {
					"name": "name",
					"type": "field"
				}],
				"addr": [{
					"_index": 0,
					"_members": [{
						"name": "line1",
						"type": "field"
					}, {
						"name": "line2",
						"type": "field"
					}, {
						"name": "state",
						"type": "field"
					}, {
						"name": "zip",
						"type": "field"
					}],
					"line1": null,
					"line2": null,
					"state": null,
					"zip": null
				}]
			}]
		}],
		"insp": [{
			"_index": 1,
			"_members": [{
				"name": "type_code",
				"type": "field"
			}, {
				"name": "value",
				"type": "field"
			}],
			"type_code": null,
			"value": null
		}, {
			"_index": 2,
			"_members": [{
				"name": "type_code",
				"type": "field"
			}, {
				"name": "value",
				"type": "field"
			}],
			"type_code": null,
			"value": null
		}]
	}],
	"impt": [{
		"_index": 0,
		"_members": [{
			"name": "id",
			"type": "field"
		}, {
			"name": "date",
			"type": "field"
		}],
		"id": null,
		"date": null
	}]
}"""

#text = """{
#    "_index": 0,
#	"_members": [{
#		"name": "pro",
#		"type": "object",
#		"indexes": [1, 2]
#	}],
#    "pro": [{
#		"_index": 1,
#		"_members": [{
#			"name": "first_name",
#			"type": "field"
#		}, {
#			"name": "last_name",
#			"type": "field"
#		}],
#		"first_name": null,
#		"last_name": null
#	}, {
#		"_index": 2,
#		"_members": [{
#			"name": "first_name",
#			"type": "field"
#		}, {
#			"name": "last_name",
#			"type": "field"
#		}],
#		"first_name": null,
#		"last_name": null
#	}]
#}"""

def imptMembers(pName, pObject, pLevel):
    print("%s%s(%d)" % (" " * (pLevel * 3), pName, pObject["_index"]))
    for member in pObject["_members"]:
        mName = member["name"]
        mType = member["type"]

        print "%sname=%s" % (" " * ((pLevel + 1) * 3), mName), "type=%s" % mType
        if mType == "object":
            for oNext in pObject[mName]:
                imptMembers(mName, oNext, pLevel + 1)         

class ImptDict(object):
    
    def __init__(self, pName, pObject):
        self._name = pName
        self._index = pObject["_index"]
        self._members = pObject["_members"]
        self._memberNames = []
        self._instances = {}
        self._fields = {}
        print("-> %s(%d) CLEAR" % (pName, self._index))
        # self.members = _members

        for mDef in self._members:
            mName = mDef["name"]
            self._memberNames.append(mName)
            m = None

            if mDef["type"] == "object":

                for dInstance in pObject[mName]:
                    print("ImptDict(%s)" % mName)
                    m = ImptDict(mName, dInstance)                   
                    self._instances[mName, m._index] = m
            else:
                self._fields[mName] = None

            print("-> %s(%d).%s" % (pName, self._index, mName))
        pass



class ImptJson(ImptDict):
    def __init__(self, pName, pText):
        super(ImptJson, self).__init__(pName, json.loads(pText))


dImpt = json.loads(text)
imptMembers("root", dImpt, 0)
#impt = ImptDict("root", dImpt)
impt = ImptJson("root", text)

print impt._instances["pro", 0]._instances
pass 
