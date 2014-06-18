# -*- coding: utf-8 -*-

import urllib2, gzip, xbmcaddon, xbmcgui
from StringIO import StringIO

ADDON            = xbmcaddon.Addon('weather.wunderground')
ADDONNAME        = ADDON.getAddonInfo('name')
LANGUAGE         = ADDON.getLocalizedString
WAIK             = ADDON.getSetting('WAIK')
WUNDERGROUND_URL = 'http://api.wunderground.com/api/%s/%s/%s/q/%s.%s'

def wundergroundapi(features, settings, query, fmt):
    try:
        key = WAIK
    except:
        dialog = xbmcgui.Dialog()
        ok = dialog.ok(ADDONNAME, LANGUAGE(32522).encode('utf-8', 'ignore'))
        data = ''
        return data
    url = WUNDERGROUND_URL % (key, features, settings, query, fmt)
    try:
        req = urllib2.Request(url)
        req.add_header('Accept-encoding', 'gzip')
        response = urllib2.urlopen(req)
        if response.info().get('Content-Encoding') == 'gzip':
            buf = StringIO(response.read())
            compr = gzip.GzipFile(fileobj=buf)
            data = compr.read()
        else:
            data = response.read()
        response.close()
    except:
        data = ''
    return data