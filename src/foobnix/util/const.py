#-*- coding: utf-8 -*-
'''
Created on 30 авг. 2010

@author: ivan
'''
from foobnix.util.localization import foobnix_localization
import locale
import gtk

foobnix_localization()

SITE_LOCALE="en"
if "ru" in locale.getdefaultlocale()[0]:
    SITE_LOCALE="ru"

ORDER_LINEAR = "ORDER_LINEAR"
ORDER_SHUFFLE = "ORDER_SHUFFLE"
ORDER_RANDOM = "ORDER_RANDOM"

REPEAT_ALL = "REPEAT_ALL"
REPEAT_SINGLE = "REPEAT_SINGLE"
REPEAT_NO = "REPEAT_NO"


ON_CLOSE_CLOSE = "ON_CLOSE_CLOSE"
ON_CLOSE_HIDE = "ON_CLOSE_HIDE"
ON_CLOSE_MINIMIZE = "ON_CLOSE_MINIMIZE"
 
PLAYLIST_PLAIN = "PLAYLIST_PLAIN"
PLAYLIST_TREE = "PLAYLIST_TREE" 

EQUALIZER_LABLES = ["PREAMP", "29", "59", "119", "237", "474", "1K", "2K", "4K", "8K", "15K"]


STATE_STOP = "STOP"
STATE_PLAY = "PLAY"
STATE_PAUSE = "PAUSE"

FTYPE_NOT_UPDATE_INFO_PANEL = "FTYPE_NOT_UPDATE_INFO_PANEL" 

FTYPE_RADIO = "FTYPE_RADIO"
FTYPE_VIDEO = "FTYPE_VIDEO"

DOWNLOAD_STATUS_ALL = _("All")
DOWNLOAD_STATUS_ACTIVE = _("Active")
DOWNLOAD_STATUS_STOP = _("Stop")
DOWNLOAD_STATUS_DOWNLOADING = _("Downloading")
DOWNLOAD_STATUS_COMPLETED = _("Complete")
DOWNLOAD_STATUS_INACTIVE = _("Inactive")

DOWNLOAD_STATUS_LOCK = _("Lock")
DOWNLOAD_STATUS_ERROR = _("Error")

LEFT_PERSPECTIVE_VK = "VK"
LEFT_PERSPECTIVE_INFO = "info"
LEFT_PERSPECTIVE_NAVIGATION = "navigation"
LEFT_PERSPECTIVE_RADIO = "radio"
LEFT_PERSPECTIVE_MY_RADIO = "my radio"
LEFT_PERSPECTIVE_VIRTUAL = "virtual"
LEFT_PERSPECTIVE_LASTFM = "last.fm"

ICON_FOOBNIX = "foobnix.png"

ICON_FOOBNIX_PLAY = "foobnix-play.png"
ICON_FOOBNIX_PAUSE = "foobnix-pause.png"
ICON_FOOBNIX_STOP = "foobnix-stop.png"
ICON_FOOBNIX_RADIO = "foobnix-radio.jpg"
ICON_BLANK_DISK = "foobnix-blank-disc.jpg"
      
BEFORE = gtk.TREE_VIEW_DROP_BEFORE
AFTER = gtk.TREE_VIEW_DROP_AFTER
INTO_OR_BEFORE = gtk.TREE_VIEW_DROP_INTO_OR_BEFORE
INTO_OR_AFTER = gtk.TREE_VIEW_DROP_INTO_OR_AFTER