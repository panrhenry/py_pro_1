#!/usr/bin/python3.6
#-*- coding: utf-8 -*-
"""
 @Time    : 2021/4/6 9:36
 @Author  : panrhenry
 @Email   : panrhenry@163.com
"""

import pandas as pd

import requests
import json

url = 'http://search.twitter.com/search.json?q=python%20pandas'

resp = requests.get(url)

data = json.loads(resp.text)

print(data.keys)


