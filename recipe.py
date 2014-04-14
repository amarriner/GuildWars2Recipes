#!/usr/bin/python

import json
import os.path
import requests
import urllib

#https://api.guildwars2.com/v1/recipes.json
#https://api.guildwars2.com/v1/recipe_details.json?recipe_id=1275
#http://wiki.guildwars2.com/wiki/API:1/items
#https://api.guildwars2.com/v1/item_details.json?item_id=28445
#https://render.guildwars2.com/file/{signature}/{file_id}.{format}

all = dict()

def get_item(item_id):
   print '   + Getting item id ' + item_id + '...'
   item_url = 'https://api.guildwars2.com/v1/item_details.json?item_id=' + item_id
   item_file = 'items/' + item_id + '.json'

   if (os.path.isfile(item_file)):
      print '     - Reading cached item...'
      f = open(item_file)
      item = json.loads(f.read())
      f.close()
   else:
      print '     - Downloading item via API...'
      request = requests.get(item_url)
      item = json.loads(request.content)
      f = open(item_file, 'w')
      f.write(request.content)
      f.close()

   image_file = 'items/' + item_id + '.png'
   image_url = 'https://render.guildwars2.com/file/' + item['icon_file_signature'] + '/' + item['icon_file_id'] + '.png'
   if (not os.path.isfile(image_file)):
      print '     - Downloading missing item image...'
      urllib.urlretrieve(image_url, image_file)

   return item

def get_recipe(recipe_id):
   print '+ Getting recipe ' + recipe_id + '...'
   recipe_url = 'https://api.guildwars2.com/v1/recipe_details.json?recipe_id=' + recipe_id
   recipe_file = 'recipes/' + recipe_id + '.json'

   if (os.path.isfile(recipe_file)):
      print ' * Reading cached recipe...'
      f = open(recipe_file)
      recipe = json.loads(f.read())
      f.close()
   else:
      print ' * Downloading recipe via API...'
      request = requests.get(recipe_url)
      recipe = json.loads(request.content)
      f = open(recipe_file, 'w')
      f.write(request.content)
      f.close()

   print ' * Processing output item...'
   item = get_item(recipe['output_item_id'])
   if (recipe_id not in all):
      all[item['name']] = []

   all[item['name']].append(recipe_id)

   #print ' * Processing ingredients...'
   #for i in recipe['ingredients']:
   #   get_item(i['item_id'])

   return recipe

r = open('recipes.json')
recipes = json.loads(r.read())
r.close()

print len(recipes['recipes'])
for r in recipes['recipes']:
   get_recipe(str(r))

f = open('items.json', 'w')
f.write(json.dumps(all))
f.close()

