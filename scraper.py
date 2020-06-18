import urllib, os, requests, datetime, subprocess



import pprint

#pip install feedparser
import feedparser

#stockexchange
from nsetools import Nse



#place your CLIENT ID and CLIENT SECRET below

class News:
    def Nigerian_News(self):
        newsfeed=feedparser.parse("http://feeds.feedburner.com")
        print("Today's News: ")
        for i in range(20):
            entry=newsfeed.entries[i]
            print(entry.title)
            print(entry.summary)
            print("---------News Link----------")
            print(entry.link)
            print("#########################################################")
            print("---------------------------------------------------------")


class Medium:
    def medium_programming(self):
        feed=feed.feedparser("https://medium.com/feed/tag/programming")

        print("Programming Today: ")
        for i in range(10):
            entry=feed.entries[i]
            print(entry.title)
            print("URL "+entry.link)
            print("############################################################")
            print("------------------------------------------------------------")

    def medium_python(self):
        feed_python=feedparser.parse("https://medium.com/feed/tag/python")
        print("Python Today: ")
        for i in range(5):
            entry=feed_python.entries[i]
            print(entry.title)
            print("URL: "+entry.link)
            print("############################################################")
            print("------------------------------------------------------------")

    def medium_developer(self):
        feed_developer=feedparser.parse("https://medium.com/feed/tag/developer")
        print("Developer News Today: ")
        for i in range(5):
            entry=feed_developer.entries[i]
            print(entry.title)
            print("URL: "+entry.link)
            print("#############################################################")
            print("-------------------------------------------------------------")



class StockExchange:
    def nse_stock(self):
        nse=Nse()
        print("TOP GAINERS OF YESTERDAY")
        pprint.pprint(nse.get_top_gainers())
        print("##################################################################")
        print("TOP LOSERS OF YESTERDAY")
        pprint.pprint(nse.get_top_losers())
        print("#############################################################")
        print("-------------------------------------------------------------")
        


#objects instantialization
News_object=News()
Medium_object=Medium()
StockExchange_object=StockExchange()



if __name__=="__main__":
    #Function call of each class
    Medium_object.medium_python()
    Medium_object.medium_developer()
    Medium_object.medium_programming()
    StockExchange_object.nse_stock()