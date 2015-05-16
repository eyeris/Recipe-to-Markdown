import urllib2
import os
from bs4 import BeautifulSoup
from timeit import default_timer as timer


class Fwrite(object):
    def __init__(self,html):
        self.name=html
        self.soup = BeautifulSoup(urllib2.urlopen(html).read())
        
    def getTitles(self):
        #directory = os.getcwd()
        #fileName = os.path.join(directory, "Allrecipes.com Page:  "+self.name[self.name.find("#")-1] + ".txt")
        #fsock = open(fileName, 'w+')
        import rescrape
        for i in self.soup.findAll("div", {"class": "searchResult hub-list-view"}):
            #fsock.write(i.find("h3", {"class": "resultTitle"}).get_text().encode("ascii", "ignore").strip().replace("\n", " ")+"\n")
            print i.find("h3", {"class": "resultTitle"}).get_text().encode("ascii", "ignore").strip().replace("\n", " "),
            #print i.find("h3", {"class": "resultTitle"}).find("a",href=True)["href"]
            s = rescrape.site.AllRecipes(i.find("h3", {"class": "resultTitle"}).find("a",href=True)["href"])
            start = timer()
            s.write(True)
            print("\t--- %s seconds ---" % (timer() - start))
            #print i.find("ul", {"class": "searchReviews"}).find("a").get_text().encode("ascii", "ignore").strip().replace("\n", " ")
            #fsock.write(i.find("h3", {"class": "resultTitle"}).find("a",href=True)["href"]+"\n")
            #fsock.write(i.find("ul", {"class": "searchReviews"}).find("a").get_text().encode("ascii", "ignore").strip().replace("\n", " ")+"\n")
            #fsock.write("\n")
            #fsock.close()
            #
            

        
        