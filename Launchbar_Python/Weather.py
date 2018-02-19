#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# LaunchBar Action Script
#
__author__ = 'BorisMirage'
# --- coding:utf-8 ---

import requests

newWeatherArlington = requests.get('http://api.wunderground.com/api/34705bc0869c57ed/conditions/q/22202.json').json()
newWeatherDC = requests.get('http://api.wunderground.com/api/34705bc0869c57ed/conditions/q/20052.json').json()
print 'Arlington: Weather - ' + str(newWeatherArlington['current_observation']['weather']) + ', Temperature - ' + str(newWeatherArlington['current_observation']['dewpoint_c']) + 'C'
print 'DC: Weather - ' + str(newWeatherDC['current_observation']['weather']) + ', Temperature - ' + str(newWeatherDC['current_observation']['dewpoint_c'])

