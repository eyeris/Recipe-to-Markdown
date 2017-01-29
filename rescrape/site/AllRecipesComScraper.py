#!/usr/bin/env python
# encoding: utf-8
"""
AllRecipesComScraper.py

Created by Timothy Hopper on 2013-03-16.
Copyright (c) 2013 __MyCompanyName__. All rights reserved.
"""

from AbstractScraper import RecipeScraper
import json
import os
#from timeit import default_timer as timer


class AllRecipes(RecipeScraper):

    def title(self):
        return self.soup.title.string.encode("ascii", 'ignore').strip().split(" - ")[0].replace('/', ' ').replace('"', ' ').replace('?', ' ').replace('*', ' ')

    def url(self):
        return self.url

    def num_servings(self):
        return self.soup.find("div", {"class": "servings"}).find("span", {"id": "lblYield"}).string.split(" ")[0]

    def prep_time(self):
        return self.get_time("prepHoursSpan") + self.get_time("prepMinsSpan")

    def cook_time(self):
        return self.get_time("cookHoursSpan") + self.get_time("cookMinsSpan")

    def total_time(self):
        return self.get_time("totalHoursSpan") + self.get_time("totalMinsSpan")

    def ingredients(self):
        for s in self.soup.findAll("p", {"itemprop": "ingredients"}):
            yield s.get_text().encode("ascii", "ignore").strip().replace("\n", " ")

    def directions(self):
        for s in self.soup.findAll("span", {"class": "plaincharacterwrap"}):
            yield s.get_text().encode("ascii", "ignore").strip().replace("\n", " ")

    def note(self):
        return ""

    def get_time(self, spanName):
        find = self.soup.find("div", {"id": "divRecipeTimesContainer"}).find("span", {"id": spanName})
        if find.__class__.__name__ != "NoneType":
            return " " + find.get_text().encode("ascii")
        return ""
    def get_ratings(self):
        return self.soup.find("div", {"class": "reviewsWrapper"}).find("p",{"id":"pRatings"}).string.split(" ")[0]
        
    def get_author(self):
        try:
            s=self.soup.find("div", {"class": "author-container"}).find("a").get("href")
            return s.split("/")[-2]
        except AttributeError:
            return "0000000"

    def conc_ingredients(self):
        line={}
        for k,s in enumerate(self.ingredients()):
            line[k]=s
        return line
        
    def conc_directions(self):
        line ={}
        for k,s in enumerate(self.directions()):
            line[k]=s
        return line
    def conc_nutrition(self):
        f={}
        try:
            for i,j in enumerate(self.find("div", "nutrSumWrap").find_all("span")):
                if i==0:
                    f["calories"]=j.string
                if i==1:
                    f["carbohydrates"]=j.string
                if i==2:
                    f["cholesterol"]=j.string
                if i==3:
                    f["fat"]=j.string
                if i==4:
                    f["fiber"]=j.string
                if i==5:
                    f["protein"]=j.string
                if i==6:
                    f["sodium"]=j.string 
            return f
        except  AttributeError:
            f["calories"]=""
            f["carbohydrates"]=""
            f["cholesterol"]=""
            f["fat"]=""
            f["fiber"]=""
            f["protein"]=""
            f["sodium"]=""
            return f
      
    def json_write(self):
        #start = timer()
        s={}
        s["title"]=self.title()
        s["url"]=self.url
        s["time"]=self.total_time()
        s["reviews"]=self.get_ratings()
        s["author_id"]=self.get_author()
        s["ingredients"]=self.conc_ingredients()
        s["directions"]=self.conc_directions()
        s["nutrition"]=self.conc_nutrition()
        #print json.dumps(s)
        directory = os.getcwd()+"\\Recipes3"
        fileName = os.path.join(directory, self.title() + ".json")
        with open(fileName, 'w') as outfile:
            json.dump(s,outfile,sort_keys=True,indent=4)
            print "now writing\t"+self.title()
            #print("\t %s seconds" % (timer() - start))
