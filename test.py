#import rescrape
#s = rescrape.site.AllRecipes("http://allrecipes.com/Recipe/Grilled-Salmon-I/Detail.aspx")

#import urllib2
#from bs4 import BeautifulSoup
#soup = BeautifulSoup(urllib2.urlopen("http://allrecipes.com/Recipes/Main.aspx?vm=l&evt19=1&p34=HR_ListView&Page=2#recipes").read())
from recipesnap import Fwrite
mm=Fwrite("http://allrecipes.com/Recipes/Main.aspx?vm=l&evt19=1&p34=HR_ListView&Page=2#recipes")
mm.getTitles()


