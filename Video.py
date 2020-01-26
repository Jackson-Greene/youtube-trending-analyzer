class Video:

    title = ""
    desc = ""
    tags = []
	

    def __init__(self, title, desc, tags):
	    self._title = title
	    self._desc = desc
	    self._tags = tags


    #Getters
    def getTitle(self):
	    return self._title


    def getDesc(self):
	    return self._desc


    def getTags(self):
	    return self._tags
		

	#Setters
    def setTitle(self, value):
	    self._title = value
	

    def setDesc(self, value):
	    self._desc = value
	

    def setTags(self, value):
	    self.tags = value


    def __str__(self):
        return "title: {}\ndescription: {}\ntags: {}".format(str(self._title), str(self._desc), str(self._tags))

