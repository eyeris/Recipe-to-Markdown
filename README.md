rescrape
========

Rescrape is a Python tool for scraping online recipes into [Markdown](http://daringfireball.net/projects/markdown/).
Becaue the files are Markdown, they can be opened in any text editor or word processor, easily emailed, and easily modified.
Because Markdown is simple a text file, you'll be able to open your recipes as easily 50 years from now as you can today.

Rescrape provides an abstract scraping class that can be implemented for any website. So far, I implemented scrapers for

* [AllRecipes.com](http://www.allrecipes.com)
* [Food.com](http://www.food.com)
* [The Pioneer Woman](http://www.thepioneerwoman.com)

Please write other scrapers and issue pull requests!

The abstract class is called RecipeScraper and is in site/AbstractScraper.py.

A site scraper is easily created:

```python
import rescrape
s = rescrape.site.AllRecipes("http://allrecipes.com/Recipe/Grilled-Salmon-I/Detail.aspx")
```

To print the recipe in Markdown form to standard out, just called:

```python
s.write()
```

You can also use the write function to create a text file:

```python
s.write(True, "~/Recipes/")
```

For the [grilled salmon](http://allrecipes.com/Recipe/Grilled-Salmon-I/Detail.aspx) recipe, you'll get this:

```
Grilled Salmon I Recipe

http://allrecipes.com/Recipe/Grilled-Salmon-I/Detail.aspx

* Servings: 6
* Prep Time:  15 mins
* Cook Time:  16 mins
* Total Time:  2 hrs 31 mins

Ingredients:

* 1 1/2 pounds salmon fillets
* lemon pepper to taste
* garlic powder to taste
* salt to taste
* 1/3 cup soy sauce
* 1/3 cup brown sugar
* 1/3 cup water
* 1/4 cup vegetable oil

Directions:

1. Season salmon fillets with lemon pepper, garlic powder, and salt.
2. In a small bowl, stir together soy sauce, brown sugar, water, and vegetable oil until sugar is dissolved. Place fish in a large resealable plastic bag with the soy sauce mixture, seal, and turn to coat. Refrigerate for at least 2 hours.
3. Preheat grill for medium heat.
4. Lightly oil grill grate. Place salmon on the preheated grill, and discard marinade. Cook salmon for 6 to 8 minutes per side, or until the fish flakes easily with a fork.
```


Rendered in Markdown, you get:

> Grilled Salmon I Recipe
>
> http://allrecipes.com/Recipe/Grilled-Salmon-I/Detail.aspx
>
> * Servings: 6
> * Prep Time:  15 mins
> * Cook Time:  16 mins
> * Total Time:  2 hrs 31 mins
>
> Ingredients:
>
> * 1 1/2 pounds salmon fillets
> * lemon pepper to taste
> * garlic powder to taste
> * salt to taste
> * 1/3 cup soy sauce
> * 1/3 cup brown sugar
> * 1/3 cup water
> * 1/4 cup vegetable oil
>
> Directions:
>
> 1. Season salmon fillets with lemon pepper, garlic powder, and salt.
> 2. In a small bowl, stir together soy sauce, brown sugar, water, and vegetable oil until sugar is dissolved. Place fish in a large resealable plastic bag with the soy sauce mixture, seal, and turn to coat. Refrigerate for at least 2 hours.
> 3. Preheat grill for medium heat.
> 4. Lightly oil grill grate. Place salmon on the preheated grill, and discard marinade. Cook salmon for 6 to 8 minutes per side, or until the fish flakes easily with a fork.

With the new improvements to the Allrecipes.com script. Following Additonal details can also be scraped and saved in JSON format. 

* Ratings
* Author (Author ID)
* Nutirients

Output the recipe as a JSON format file using ```s.json_write()``` method.

When using ```.json_write()``` method, ingredients, directions and nutriens information are also written isside a sub JSON document.


```json
{
   "nutrition":{
      "fiber":"5.7",
      "sodium":"960",
      "carbohydrates":"45",
      "calories":"559",
      "fat":"31.7",
      "cholesterol":"44",
      "protein":"22.5"
   },
   "ingredients":{
      "0":"2 1/2 cups all-purpose flour",
      "1":"1/2 teaspoon salt",
      "2":"1 cup chilled solid vegetable shortening",
      "3":"6 tablespoons ice water, or as needed",
      "4":"3 cups cubed cooked turkey",
      "5":"1/2 small onion, chopped",
      "6":"1 (10.75 ounce) can cream of potato soup",
      "7":"1 (10.75 ounce) can cream of chicken soup",
      "8":"1/2 (10.75 ounce) can water",
      "9":"2 (15 ounce) cans mixed vegetables, drained",
      "10":"salt and pepper to taste"
   },
   "url":"http://allrecipes.com/recipe/grandmas-leftover-turkey-pot-pie/detail.aspx",
   "title":"Grandma's Leftover Turkey Pot Pie Recipe",
   "reviews":"22",
   "time":" 1 hr 45 mins",
   "directions":{
      "0":"Whisk together the flour and 1/2 teaspoon of salt in a bowl..,
      "1":"Preheat oven to 375 degrees F (190 degrees C)...",
      "2":"In a saucepan, mix together the turkey, onion, cream of potato soup..,
      "3":"Cut the dough in almost equal halves. 
      "4":"Bake in the preheated oven until the crust is golden brown, about 45 minutes..."
   },
   "author_id":"1969657"
}
```

# Data Set and update on the code

I have modified the code to support fetchig more information from allrecipes.com and save using JSON format. JSON format is flexible and this can be easily exported to NoSQL database like MongoDB. However, shortafter, alrecipes.com changed their website layout so that the code woudnt work. Therefore, I am releasing the raw data set. This is 26 790 recipes. Actual number of reviews may be different than the number in the recipe as I have collected data in 2015. 

The URL is still working. Nutrient information is per serving. Please refer to the URL for units of measurements for the nutrients. Most of the times, following units of measurements are used

* Fiber (g)
* Fat (g)
* Carbohydrates (g)
* Protein (g)
* Sodium (mg)
* Cholestrol (mg)

# Publications 

This dataset is downloaded for my thesis and some publications related to this work can be mentioned as follows (but they use different dataset). Since this is unprocessed raw dataset, NLP and ML based reserch canuse this. 

I. Nirmal, A. Caldera, and R. D. Bandara, “Optimization Framework for Flavour and Nutrition Balanced Recipe: A Data Driven Approach,” 2018 5th IEEE Uttar Pradesh Section International Conference on Electrical, Electronics and Computer Engineering (UPCON), 2018.


