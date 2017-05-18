#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import cchardet as chardet

with open('countriesToCities.json') as data_file:    
    data = json.load(data_file)

counter = 0

for country in data:
  for city in data[country]:
    charset = chardet.detect(str(city.encode('utf-8')))
    if charset['encoding'] != 'ASCII':
      print(city)
      counter += 1

print("Temos " + str(counter) + " cidades com falha")
