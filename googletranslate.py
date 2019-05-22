#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Get translate from Google Translate
author: 'XINZENG ZHANG'
Created on 2018-04-18 17:04:00
USAGE:
python3 googletranslate.py <target language code> <text to be translated>
python googletranslate.py zh-CN 'hello world!'
"""

import requests
import sys
import urllib.parse
import json


def get_url(tl, qry):
    url = 'https://{}/translate_a/single?client=gtx&sl=auto&tl={}&dt=at&dt=bd&dt=ex&' \
          'dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&q={}'.format(http_host, tl, qry)
    return url





def get_translation(querystr):
    result = "{} :\n".format(querystr)
    for query_string in querystr.split("."):
        if len(query_string) > 5000:
            print(' Maximum characters exceeded...')
            return

        base_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0'}
        session = requests.Session()
        session.headers = base_headers
        parse_query = urllib.parse.quote_plus(query_string)
        url = get_url(target_language, parse_query)
        #print(url)
        try:
            
            resp = session.get(url, timeout=3).json()
            #print(resp)
            if len(resp[0])>1:
                if resp[0][1][3]!= None:
                    result += " /{}/".format(resp[0][1][3])
                result += "\t{}".format(resp[0][0][0])           
                if resp[1]:
                    for x in resp[1][0][1]:
                        result += ", {}".format(x)

            elif len(resp[0])==1:
                result += "\t{}".format(resp[0][0][0])
            result += "."
        except requests.exceptions.ReadTimeout:
            print('ReadTimeout...')
    print(result.encode(result_code, 'ignore').decode(result_code))

if __name__ == "__main__":
    http_host = 'translate.googleapis.com'
    target_language = sys.argv[1]
    query_strings = sys.argv[2]
    synonyms_en = False
    definitions_en = True
    examples_en = False
    result_code = 'utf-8'
    alternative_language = 'en'
    get_translation(query_strings)
