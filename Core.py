import random
import base64
# import platform as holysystem
from urllib.request import urlopen as apiloader
from urllib.parse import quote_plus as urlgen
from json import loads as jsongen
from requests import get as urldecode

class WilloteamBase:
    serverlog = 724268787360202839
    server = 724268787360202836
    guildowner = 479642404216111124

class emoticon:
    error = 729527143100317707
    success = 723714370462416966

def jsonapi(url):
    return urldecode(url).json()

def api(url):
    return jsongen(apiloader(url).read())

class Config:
    prefix = 'g!'

class Version:
    version = '0.67' 
    changelog = 'BFD updates, added `g!vote`, added `g!httpcat` and modified `g!about`'

def urlify(word): 
  return urlgen(word).replace('+', '%20')

def gitify(word):
  return urlgen(word).replace('-')
