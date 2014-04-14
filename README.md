Idea is to have a web app to peruse Guild Wars 2 recipes. Fleshed out soon. Expanded to mess with map stuff.

[In progress demo](http://bulletriddenlich.com/gw2/)

[In progress map demo](http://bulletriddenlich.com/gw2/map.html)

* recipe.py - the main use for this is to cache all of the recipe and item detail results on disk as well as all of the 
item images. The resulting items folder is 96mb, and the recipes folder is 33mb. The cache takes about an hour to 
complete. Subsequent runs of the script merely check to make sure the item/recipe has been cached. Its other utility is 
to build other JSON files from the API results. For example, in order to search all the recipes by output item, one could 
build a file with all the names of the output items associated with recipe ids. 

* map.py - works similarly to recipe.py in that it's for caching map JSON files

* index.html - right now this is just a playground for messing with the cached results of the python script using jquery
