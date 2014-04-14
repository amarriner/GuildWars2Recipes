Idea is to have a web app to peruse Guild Wars 2 recipes. Fleshed out soon.

[In progress demo](http://bulletriddenlich.com/gw2/)

* recipe.py - the main use for this is to cache all of the recipe and item detail results on disk as well as all of the 
item images. The resulting items folder is 96mb, and the recipes folder is 33mb. The cache takes about an hour to 
complete. Subsequent runs of the script merely check to make sure the item/recipe has been cached. It's other utility is 
to build other JSON files from the API results. For example, in order to search all the recipes by output item, one could 
build a file with all the names of the output items associated with recipe ids. 

* index.html - right now this is just a playground for messing with the cached results of the python script using jquery
