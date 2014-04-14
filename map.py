#!/usr/bin/python

import json
import os.path
import requests
import urllib

# https://api.guildwars2.com/v1/continents.json
# https://tiles.guildwars2.com/{continent_id}/{floor}/{zoom}/{x}/{y}.jpg
# https://api.guildwars2.com/v1/map_floor.json?continent_id=1&floor=1
# https://api.guildwars2.com/v1/maps.json?map_id=15

continents = None

def get_continents():
   print '+ Getting continents...'

   continents_url = 'https://api.guildwars2.com/v1/continents.json'
   continents_file = 'maps/continents.json'

   if (os.path.isfile(continents_file)):
      print ' * Reading cached continents file...'
      f = open(continents_file)
      continents = json.loads(f.read())
      f.close()
   else:
      print ' * Downloading continents via API...'
      request = requests.get(continents_url)
      continents = json.loads(request.content)
      f = open(continents_file, 'w')
      f.write(request.content)
      f.close()

   return continents

def process_continents():
   print '+ Processing continents...'

   for c in continents['continents']:
      print ' * Processing ' + continents['continents'][c]['name'] + '...'

      for f in continents['continents'][c]['floors']:
         floor_url = 'https://api.guildwars2.com/v1/map_floor.json?continent_id=' + str(c) + '&floor=' + str(f)
         floor_file = 'maps/floors/' + str(c) + '_' + str(f) + '.json'

         if (os.path.isfile(floor_file)):
            print ' * Reading cached floor (' + str(f) + ') file...'
            f = open(floor_file)
            floor = json.loads(f.read())
            f.close()
         else:
            print ' * Downloading floor (' + str(f) + ') via API...'
            request = requests.get(floor_url)
            floor = json.loads(request.content)
            f = open(floor_file, 'w')
            f.write(request.content)
            f.close()

continents = get_continents()
process_continents()
