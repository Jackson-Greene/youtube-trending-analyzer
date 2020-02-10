import Scrapper


def getSentenceFromData():

    sentence = "" 

    videos_list = Scrapper.getTrendingData()

    titles_list = getTitlesFromVideos(videos_list)
    tags_list = getTagsFromVideos(videos_list)






    

    return sentence


#from a list of Video objects extract all tags and put them in a list (of strings)#
def getTagsFromVideos(videos_list):
    
    tags_list = []

    for video in videos_list:
        tags = []
        tags = video.getTags()

        for tag in tags:
            tags_list.append(tag)

    return tags_list
####


#from a list of Video objects extract all tags and pvideos_listt (of strings)#
def getTitlesFromVideos(videos_list):
    
    titles_list = []

    for video in videos_list:
        title = video.getTitle()
        titles_list.append(title)

    return titles_list
####

