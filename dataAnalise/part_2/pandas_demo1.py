#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
"""
 @Time    : 2021/3/19 9:16
 @Author  : panrhenry
 @Email   : panrhenry@163.com
"""

import pandas as pd
from lxml.html import parse
from urllib.request import urlopen

parsed = parse(urlopen('http://finance.yahoo.com/q/op?s=AAPL+Options'))

doc = parsed.getroot()

print("doc: %s" % doc)

# links = doc.findall('.//a')
#
# print(links[15:20])

# ----1
urls = [lnk.get('href') for lnk in doc.findall('.//a')]

# print(urls[-10:])

# --- 2
tables = doc.findall('.//table')
calls = tables[0:1]
puts = tables[1:1]

print('calls : %s ' % calls)

rows = calls.findll('.//tr')

print(rows)


# def _unpack(row, kind='td'):
#     etls = row.findall('.//%s' % kind)
#     return [val.text_content() for val in etls]
#
# print(_unpack(rows[0],kind='th'))
