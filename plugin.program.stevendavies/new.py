import xbmc, xbmcaddon, xbmcgui, xbmcplugin,os,base64,sys,xbmcvfs
import shutil
import urllib2,urllib
import re
import extract
import downloader
import time
import plugintools
import MySQLdb
from addon.common.addon import Addon
from addon.common.net import Net

USER_AGENT = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
ADDON_ID = 'plugin.program.chameleonbuilds'
BASEURL = 'http://wizard.chameleonbuilds.com'
ADDON = xbmcaddon.Addon(id=ADDON_ID)
HOME = ADDON.getAddonInfo('path')
VERSION = "0.0.1"
PATH = "Chameleon Builds"
FANART = xbmc.translatePath(os.path.join('special://home/addons/' + ADDON_ID , 'fanart.jpg'))
ICON = xbmc.translatePath(os.path.join('special://home/addons/' + ADDON_ID, 'icon.png'))
ART = xbmc.translatePath(os.path.join('special://home/addons/' + ADDON_ID + '/resources/art/'))
zip        =  ADDON.getSetting('zip')
dialog     =  xbmcgui.Dialog()
dp         =  xbmcgui.DialogProgress()


