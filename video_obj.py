class Video:
    title = ""
    desc = ""
    hyperlink = ""
    tags = []
	
    def __init__(self, title, desc, hyperlink, tags):
	    self._title = title
	    self._desc = desc
	    self._hyperlink = hyperlink
	    self._tags = tags
	
    def creatVideo(title, desc, hyperlink, tags):
	    video = Video(title, desc, hyperlink, tags)
	    return video

    #Getters
    def getTitle(self):
	    return self._title

    def getDesc(self):
	    return self._desc
	
    def getHyperlink(self):
	    return self._hyperlink

    def getTags(self):
	    return self._tags
		
    #Setters
    def setTitle(self, value):
	    self._title = value
	
    def setDesc(self, value):
	    self._desc = value

    def setHyperLink(self, value):
	    self._hyperlink = value
	
    def setTags(self, value):
	    self.tags = value

    def __str__(self):
	    return "Title: " + self._title + "\nDescription: " + self._desc + "\nHyperlink: " + self._hyperlink + "\nTags: " + self._tags
