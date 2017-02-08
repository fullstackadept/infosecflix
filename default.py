# -*- coding: utf-8 -*-
#------------------------------------------------------------
# InfosecFlix by fullstackadept
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon and talesfromthecrypt by coldkeys
#
# Author: fullstackadept
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

# Get the plugin url in plugin:// notation.
__url__ = sys.argv[0]

addonID = 'plugin.video.infosecflix'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

FANART=os.path.join(os.path.dirname(__file__), 'fanart.jpg')

# Main conference/playlist config
PLAYLISTS = {
    'Black Hat USA': [{
        'title' : 'Black Hat USA 2016',
        'id' : 'PLH15HpR5qRsXm0-rMacuWBxWcB2fmsmEw'
        },
        {
        'title' : 'Black Hat USA 2015',
        'id' : 'PLH15HpR5qRsXF78lrpWP2JKpPJs_AFnD7'
        },
        {
        'title' : 'Black Hat USA 2014',
        'id' : 'PLH15HpR5qRsUBgeytB_T4xnKzr4Iv3upj'
        },
        {
        'title' : 'Black Hat USA 2013',
        'id' : 'PLH15HpR5qRsUtTv7IQKftKGOcRLGtwuoF'
    }],
    'BSides': [{
        'title' : 'Bsides Augusta 2016',
        'id' : 'PLNhlcxQZJSm_4V8VDudQyBFp8b91rBHTj'
        },
        {
        'title' : 'Bsides Detroit 2016',
        'id' : 'PLNhlcxQZJSm-AtNWUBV2eI_zNDGHRrbhk'
        },
        {
        'title' : 'Bsides Nashville 2016',
        'id' : 'PLNhlcxQZJSm8OerdQZyQAdi7GG1ufgRaw'
        },
        {
        'title' : 'Bsides Knoxville 2016',
        'id' : 'PLNhlcxQZJSm_AgX2w6eHs3EIeaErUlm-5'
        },
        {
        'title' : 'Bsides SF 2016',
        'id' : 'PLNhlcxQZJSm_vceoN_dHHm44mpT_UbaWF'
        },
        {
        'title' : 'Bsides LV 2015',
        'id' : 'PLNhlcxQZJSm_wpMC42BKPCknT-JhnZGos'
        },
        {
        'title' : 'Bsides Tampa 2015',
        'id' : 'PLNhlcxQZJSm_by2u3gZUlcPPU0IQtvRTS'
    }],
    'CircleCityCon': [{
        'title' : 'CircleCityCon 2016',
        'id' : 'PLNhlcxQZJSm_fAztb-LmQapZiEM08cV-6'
        },
        {
        'title' : 'CircleCityCon 2015',
        'id' : 'PLNhlcxQZJSm9TV35bUYvhjUpdAR8iPT5R'
        },
        {
        'title' : 'CircleCityCon 2014',
        'id' : 'PLNhlcxQZJSm8AQVCGin_go3JgJe4dVgPR'
    }],
    'ConVerge': [{
        'title' : 'ConVerge 2016',
        'id' : 'PLNhlcxQZJSm9HnVtDwMQ_JN1bCTuOedMh'
    }],
    'DEF CON': [{
        'title' : 'DEF CON 24 (2016)',
        'id' : 'PL9fPq3eQfaaAvXV3hJc4yHuNxoviVckoE'
        },
        {
        'title' : 'DEF CON 23 (2015)',
        'id' : 'PL9fPq3eQfaaBuHqVvDzPoWxznYYmyx5UX'
        },
        {
        'title' : 'DEF CON 22 (2014)',
        'id' : 'PL9fPq3eQfaaBCdjbKFYjosh1s1EkaYdsQ'
        },
        {
        'title' : 'DEF CON 21 (2013)',
        'id' : 'PL9fPq3eQfaaBD_8E9PJ8yyiTL0JhynlGK'
        },
        {
        'title' : 'DEF CON 20 (2012)',
        'id' : 'PL9fPq3eQfaaDcbIEMSzdL5yuzh_m6BB-E'
        },
        {
        'title' : 'DEF CON 19 (2011)',
        'id' : 'PL9fPq3eQfaaBoESMifnn5w4S487vrmGR6'
        },
        {
        'title' : 'DEF CON 18 (2010)',
        'id' : 'PL9fPq3eQfaaC26TgwyDg2Db-m5E7jRRbj'
        },
        {
        'title' : 'DEF CON 17 (2009)',
        'id' : 'PL9fPq3eQfaaDjnjDsjgmtASOWg8a8neEE'
        },
        {
        'title' : 'DEF CON 16 (2008)',
        'id' : 'PL9fPq3eQfaaBY3OjTaGyaBzgc80sOFkG8'
        },
        {
        'title' : 'DEF CON 15 (2007)',
        'id' : 'PL9fPq3eQfaaCji1aEQBUrIpPQf9-HazLL'
        },
        {
        'title' : 'DEF CON 14 (2006)',
        'id' : 'PL9fPq3eQfaaAxDI0xo83ZFzDAZgXO3Yhy'
        },
        {
        'title' : 'DEF CON 13 (2005)',
        'id' : 'PL9fPq3eQfaaBwvKmscgwI2B-S981fgVrH'
        },
        {
        'title' : 'DEF CON 12 (2004)',
        'id' : 'PL9fPq3eQfaaAU98_NKiJ-7simP1s-O2zs'
        },
        {
        'title' : 'DEF CON 11 (2003)',
        'id' : 'PL9fPq3eQfaaAlKSZpQad9gwnASyhJ33Zi'
        },
        {
        'title' : 'DEF CON 10 (2002)',
        'id' : 'PL9fPq3eQfaaChpuiKkNQ0uwmYdpPoI65z'
        },
        {
        'title' : 'DEF CON 9 (2002)',
        'id' : 'PL9fPq3eQfaaCzGwJQmga1SRJUedjp2t5c'
        },
        {
        'title' : 'DEF CON 8 (2001)',
        'id' : 'PL9fPq3eQfaaCotE0QrvM2eTmm-59Gvt9Z'
        },
        {
        'title' : 'DEF CON 7 (2000)',
        'id' : 'PL9fPq3eQfaaBxFm9YU4aafXz75peLDXhX'
    }],
    'DerbyCon': [{
        'title' : 'DerbyCon 6.0 (2016)',
        'id' : 'PLNhlcxQZJSm9T78xh_QYYiqkTjIt4jYgm'
        },
        {
        'title' : 'DerbyCon 5.0 (2015)',
        'id' : 'PLNhlcxQZJSm8cr3iBN27VZ4Rm11Erbae-'
        },
        {
        'title' : 'DerbyCon 4.0 (2014)',
        'id' : 'PLNhlcxQZJSm8o9c_2_iDDTV6tCPdMp5dg'
        },
        {
        'title' : 'DerbyCon 3.0 (2013)',
        'id' : 'PLNhlcxQZJSm-Wo3Kpvn8oIm_rD5PwlmHX'
        },
        {
        'title' : 'DerbyCon 2.0 (2012)',
        'id' : 'PLNhlcxQZJSm97hLg2WXjW1qTytN-pbDtv'
        },
        {
        'title' : 'DerbyCon 1.0 (2011)',
        'id' : 'PL2ABA97A5B8AA1005'
    }],
    'GrrCon': [{
        'title' : 'GrrCon 2016',
        'id' : 'PLNhlcxQZJSm88_x7IQKSFzhtp9ileHB72'
        },
        {
        'title' : 'GrrCon 2015',
        'id' : 'PLNhlcxQZJSm-lvGvO_MQ6x08wdwLdh4YJ'
    }],
    'HOPE': [{
        'title' : 'The Eleventh HOPE (2016)',
        'id' : 'PLcajvRZA8E099SG5JGAaS56NMHPTbuHIV'
        },
        {
        'title' : 'HOPE X (2014)',
        'id' : 'PLcajvRZA8E0-UUHhjOBQuYADBypOPFt-a'
        },
        {
        'title' : 'HOPE Number Nine (2012)',
        'id' : 'PLcajvRZA8E09m2Z8r7CUDYcI3908SNkHU'
        },
        {
        'title' : 'The Next HOPE (2010)',
        'id' : 'PLcajvRZA8E0-OrQXj7nPbmfEpKVu7VvYs'
        },
        {
        'title' : 'The Last HOPE (2008)',
        'id' : 'PLcajvRZA8E0_8luB1SAMjMW5AZ_Uc1nTG'
        },
        {
        'title' : 'HOPE Number Six (2006)',
        'id' : 'PLcajvRZA8E08sBBGcHVz32idpxDNXn7nF'
        },
        {
        'title' : 'The Fifth HOPE (2004)',
        'id' : 'PLcajvRZA8E084v1rTdZYTKiEDoHAP5IPx'
        },
        {
        'title' : 'H2K2 (2002)',
        'id' : 'PLcajvRZA8E09HG98twwOf9rfYF6-FHORZ'
        },
        {
        'title' : 'H2K (2000)',
        'id' : 'PLcajvRZA8E09S7VRCK3XRzIRx9zNKGv5e'
        },
        {
        'title' : 'Beyond HOPE (1997)',
        'id' : 'PLcajvRZA8E0-4HW1K66VGge3JcUdAEJj5'
        },
        {
        'title' : 'Hackers On Planet Earth (1994)',
        'id' : 'PLcajvRZA8E0_ckfjqU1irYzOwbsYa2AjC'
    }],
    'SchmooCon': [{
        'title' : 'SchmooCon 2016',
        'id' : 'PLJgHiyD1pZg70X3X3zjmdmZg3u0eqDFJ4'
        },
        {
        'title' : 'SchmooCon 2015',
        'id' : 'PLStO1VqVBvmHyVc71QLOCBKugWQyyM7WE'
    }],
    'SecureWV': [{
        'title' : 'SecureWV/Hack3rcon 2016',
        'id' : 'PLNhlcxQZJSm-wLsEAL9FIXAhC3WY1YvrW'
    }],
    'ShowMeCon': [{
        'title' : 'ShowMeCon 2016',
        'id' : 'PLNhlcxQZJSm9NT-zQ9jHdYRhtGOASAYT7'
        },
        {
        'title' : 'ShowMeCon 2015',
        'id' : 'PLNhlcxQZJSm9zsNKfwujM4JgEk1wOc44m'
    }]
}

def name_as_key(name):
    return name.lower().replace(" ", "")

def load_thumbnail(name):
    filename = name_as_key(name)
    return os.path.join(os.path.dirname(__file__), 'resources', 'logos', filename + '.jpg')

def get_main_menu():
    return PLAYLISTS.keys()

def get_sub_menu(name):
    return PLAYLISTS[name]

def main_menu():
    for name in get_main_menu():
        # Create a URL for the plugin recursive callback.
        # Example: plugin://plugin.video.example/?action=listing&category=SchmooCon
        plugintools.add_item(
            title=name,
            url='{0}?action=listing&category={1}'.format(__url__, name),
            thumbnail=load_thumbnail(name),
            fanart=FANART,
            folder=True )

def sub_menu(name):
    for item in get_sub_menu(name):
        plugintools.add_item(
            title=item['title'],
            url='plugin://plugin.video.youtube/playlist/' + item['id'] + '/',
            thumbnail=load_thumbnail(name),
            fanart=FANART,
            folder=True )

# Entry point
def run():
    # Get params
    params = plugintools.get_params()

    plugintools.log("[plugin.video.infosecflix] run "+repr(params))

    if params.get("action") is None:
        main_menu()
    else:
        sub_menu(params.get("category"))

    plugintools.close_item_list()

run()
