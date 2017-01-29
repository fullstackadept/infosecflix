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

# thumbnail config
THUMBS = {
    'blackhatusa' : 'https://pbs.twimg.com/profile_images/730168530440609792/EgTOmf8I_400x400.jpg',
    'bsides' : 'https://i.imgur.com/ABoCVMD.jpg',
    'circlecitycon' : 'https://pbs.twimg.com/profile_images/378800000397493274/efb9db3e911e52f08dc7ca7beb6ef405_400x400.jpeg',
    'converge' : 'https://www.convergeconference.org/wp-content/uploads/2016/10/converge_logo_home-Copy.png',
    'defcon' : 'https://pbs.twimg.com/profile_images/794271957818580992/QJ06URkq_400x400.jpg',
    'derbycon' : 'https://pbs.twimg.com/profile_images/1100903441/derbyconlogo-Twitter_400x400.jpg',
    'grrcon' : 'http://grrcon.com/wp-content/themes/grrcon/images/logo.png',
    'hope' : 'https://i.imgur.com/qd4DWHi.png',
    'schmoocon' : 'https://pbs.twimg.com/profile_images/357342497/Shmoo_Eyes_400x400.jpg',
    'showmecon' : 'https://pbs.twimg.com/profile_images/789200425962450945/_I_Q0wy5_400x400.jpg',
    'securewv' : 'https://pbs.twimg.com/profile_images/737851153036283904/Bh6iVwvD_400x400.jpg'
}

#FANART="https://i.ytimg.com/vi/oFN1N5r5BOA/maxresdefault.jpg"
FANART="https://i.imgur.com/qv3RMak.jpg"

# Main conference/playlist config
PLAYLISTS = {
    'Black Hat USA': [{
        'title' : 'Black Hat USA 2016',
        'id' : 'PLH15HpR5qRsXm0-rMacuWBxWcB2fmsmEw',
        'thumbnail' : THUMBS['blackhatusa']
        },
        {
        'title' : 'Black Hat USA 2015',
        'id' : 'PLH15HpR5qRsXF78lrpWP2JKpPJs_AFnD7',
        'thumbnail' : THUMBS['blackhatusa']
        },
        {
        'title' : 'Black Hat USA 2014',
        'id' : 'PLH15HpR5qRsUBgeytB_T4xnKzr4Iv3upj',
        'thumbnail' : THUMBS['blackhatusa']
        },
        {
        'title' : 'Black Hat USA 2013',
        'id' : 'PLH15HpR5qRsUtTv7IQKftKGOcRLGtwuoF',
        'thumbnail' : THUMBS['blackhatusa']
    }],
    'BSides': [{
        'title' : 'Bsides Augusta 2016',
        'id' : 'PLNhlcxQZJSm_4V8VDudQyBFp8b91rBHTj',
        'thumbnail' : THUMBS['bsides']
        },
        {
        'title' : 'Bsides Detroit 2016',
        'id' : 'PLNhlcxQZJSm-AtNWUBV2eI_zNDGHRrbhk',
        'thumbnail' : THUMBS['bsides']
        },
        {
        'title' : 'Bsides Nashville 2016',
        'id' : 'PLNhlcxQZJSm8OerdQZyQAdi7GG1ufgRaw',
        'thumbnail' : THUMBS['bsides']
        },
        {
        'title' : 'Bsides Knoxville 2016',
        'id' : 'PLNhlcxQZJSm_AgX2w6eHs3EIeaErUlm-5',
        'thumbnail' : THUMBS['bsides']
        },
        {
        'title' : 'Bsides SF 2016',
        'id' : 'PLNhlcxQZJSm_vceoN_dHHm44mpT_UbaWF',
        'thumbnail' : THUMBS['bsides']
        },
        {
        'title' : 'Bsides LV 2015',
        'id' : 'PLNhlcxQZJSm_wpMC42BKPCknT-JhnZGos',
        'thumbnail' : THUMBS['bsides']
        },
        {
        'title' : 'Bsides Tampa 2015',
        'id' : 'PLNhlcxQZJSm_by2u3gZUlcPPU0IQtvRTS',
        'thumbnail' : THUMBS['bsides']
    }],
    'CircleCityCon': [{
        'title' : 'CircleCityCon 2016',
        'id' : 'PLNhlcxQZJSm_fAztb-LmQapZiEM08cV-6',
        'thumbnail' : THUMBS['circlecitycon']
        },
        {
        'title' : 'CircleCityCon 2015',
        'id' : 'PLNhlcxQZJSm9TV35bUYvhjUpdAR8iPT5R',
        'thumbnail' : THUMBS['circlecitycon']
        },
        {
        'title' : 'CircleCityCon 2014',
        'id' : 'PLNhlcxQZJSm8AQVCGin_go3JgJe4dVgPR',
        'thumbnail' : THUMBS['circlecitycon']
    }],
    'ConVerge': [{
        'title' : 'ConVerge 2016',
        'id' : 'PLNhlcxQZJSm9HnVtDwMQ_JN1bCTuOedMh',
        'thumbnail' : THUMBS['converge']
    }],
    'DEF CON': [{
        'title' : 'DEF CON 24 (2016)',
        'id' : 'PL9fPq3eQfaaAvXV3hJc4yHuNxoviVckoE',
        'thumbnail' : THUMBS['defcon']
        },
        {
        'title' : 'DEF CON 23 (2015)',
        'id' : 'PL9fPq3eQfaaBuHqVvDzPoWxznYYmyx5UX',
        'thumbnail' : THUMBS['defcon']
        },
        {
        'title' : 'DEF CON 22 (2014)',
        'id' : 'PL9fPq3eQfaaBCdjbKFYjosh1s1EkaYdsQ',
        'thumbnail' : THUMBS['defcon']
        },
        {
        'title' : 'DEF CON 21 (2013)',
        'id' : 'PL9fPq3eQfaaBD_8E9PJ8yyiTL0JhynlGK',
        'thumbnail' : THUMBS['defcon']
        },
        {
        'title' : 'DEF CON 20 (2012)',
        'id' : 'PL9fPq3eQfaaDcbIEMSzdL5yuzh_m6BB-E',
        'thumbnail' : THUMBS['defcon']
        },
        {
        'title' : 'DEF CON 19 (2011)',
        'id' : 'PL9fPq3eQfaaBoESMifnn5w4S487vrmGR6',
        'thumbnail' : THUMBS['defcon']
        },
        {
        'title' : 'DEF CON 18 (2010)',
        'id' : 'PL9fPq3eQfaaC26TgwyDg2Db-m5E7jRRbj',
        'thumbnail' : THUMBS['defcon']
        },
        {
        'title' : 'DEF CON 17 (2009)',
        'id' : 'PL9fPq3eQfaaDjnjDsjgmtASOWg8a8neEE',
        'thumbnail' : THUMBS['defcon']
        },
        {
        'title' : 'DEF CON 16 (2008)',
        'id' : 'PL9fPq3eQfaaBY3OjTaGyaBzgc80sOFkG8',
        'thumbnail' : THUMBS['defcon']
        },
        {
        'title' : 'DEF CON 15 (2007)',
        'id' : 'PL9fPq3eQfaaCji1aEQBUrIpPQf9-HazLL',
        'thumbnail' : THUMBS['defcon']
        },
        {
        'title' : 'DEF CON 14 (2006)',
        'id' : 'PL9fPq3eQfaaAxDI0xo83ZFzDAZgXO3Yhy',
        'thumbnail' : THUMBS['defcon']
        },
        {
        'title' : 'DEF CON 13 (2005)',
        'id' : 'PL9fPq3eQfaaBwvKmscgwI2B-S981fgVrH',
        'thumbnail' : THUMBS['defcon']
        },
        {
        'title' : 'DEF CON 12 (2004)',
        'id' : 'PL9fPq3eQfaaAU98_NKiJ-7simP1s-O2zs',
        'thumbnail' : THUMBS['defcon']
        },
        {
        'title' : 'DEF CON 11 (2003)',
        'id' : 'PL9fPq3eQfaaAlKSZpQad9gwnASyhJ33Zi',
        'thumbnail' : THUMBS['defcon']
        },
        {
        'title' : 'DEF CON 10 (2002)',
        'id' : 'PL9fPq3eQfaaChpuiKkNQ0uwmYdpPoI65z',
        'thumbnail' : THUMBS['defcon']
        },
        {
        'title' : 'DEF CON 9 (2002)',
        'id' : 'PL9fPq3eQfaaCzGwJQmga1SRJUedjp2t5c',
        'thumbnail' : THUMBS['defcon']
        },
        {
        'title' : 'DEF CON 8 (2001)',
        'id' : 'PL9fPq3eQfaaCotE0QrvM2eTmm-59Gvt9Z',
        'thumbnail' : THUMBS['defcon']
        },
        {
        'title' : 'DEF CON 7 (2000)',
        'id' : 'PL9fPq3eQfaaBxFm9YU4aafXz75peLDXhX',
        'thumbnail' : THUMBS['defcon']
    }],
    'DerbyCon': [{
        'title' : 'DerbyCon 6.0 (2016)',
        'id' : 'PLNhlcxQZJSm9T78xh_QYYiqkTjIt4jYgm',
        'thumbnail' : THUMBS['derbycon']
        },
        {
        'title' : 'DerbyCon 5.0 (2015)',
        'id' : 'PLNhlcxQZJSm8cr3iBN27VZ4Rm11Erbae-',
        'thumbnail' : THUMBS['derbycon']
        },
        {
        'title' : 'DerbyCon 4.0 (2014)',
        'id' : 'PLNhlcxQZJSm8o9c_2_iDDTV6tCPdMp5dg',
        'thumbnail' : THUMBS['derbycon']
        },
        {
        'title' : 'DerbyCon 3.0 (2013)',
        'id' : 'PLNhlcxQZJSm-Wo3Kpvn8oIm_rD5PwlmHX',
        'thumbnail' : THUMBS['derbycon']
        },
        {
        'title' : 'DerbyCon 2.0 (2012)',
        'id' : 'PLNhlcxQZJSm97hLg2WXjW1qTytN-pbDtv',
        'thumbnail' : THUMBS['derbycon']
        },
        {
        'title' : 'DerbyCon 1.0 (2011)',
        'id' : 'PL2ABA97A5B8AA1005',
        'thumbnail' : THUMBS['derbycon']
    }],
    'GrrCon': [{
        'title' : 'GrrCon 2016',
        'id' : 'PLNhlcxQZJSm88_x7IQKSFzhtp9ileHB72',
        'thumbnail' : THUMBS['grrcon']
        },
        {
        'title' : 'GrrCon 2015',
        'id' : 'PLNhlcxQZJSm-lvGvO_MQ6x08wdwLdh4YJ',
        'thumbnail' : THUMBS['grrcon']
    }],
    'HOPE': [{
        'title' : 'The Eleventh HOPE (2016)',
        'id' : 'PLcajvRZA8E099SG5JGAaS56NMHPTbuHIV',
        'thumbnail' : THUMBS['hope']
        },
        {
        'title' : 'HOPE X (2014)',
        'id' : 'PLcajvRZA8E0-UUHhjOBQuYADBypOPFt-a',
        'thumbnail' : THUMBS['hope']
        },
        {
        'title' : 'HOPE Number Nine (2012)',
        'id' : 'PLcajvRZA8E09m2Z8r7CUDYcI3908SNkHU',
        'thumbnail' : THUMBS['hope']
        },
        {
        'title' : 'The Next HOPE (2010)',
        'id' : 'PLcajvRZA8E0-OrQXj7nPbmfEpKVu7VvYs',
        'thumbnail' : THUMBS['hope']
        },
        {
        'title' : 'The Last HOPE (2008)',
        'id' : 'PLcajvRZA8E0_8luB1SAMjMW5AZ_Uc1nTG',
        'thumbnail' : THUMBS['hope']
        },
        {
        'title' : 'HOPE Number Six (2006)',
        'id' : 'PLcajvRZA8E08sBBGcHVz32idpxDNXn7nF',
        'thumbnail' : THUMBS['hope']
        },
        {
        'title' : 'The Fifth HOPE (2004)',
        'id' : 'PLcajvRZA8E084v1rTdZYTKiEDoHAP5IPx',
        'thumbnail' : THUMBS['hope']
        },
        {
        'title' : 'H2K2 (2002)',
        'id' : 'PLcajvRZA8E09HG98twwOf9rfYF6-FHORZ',
        'thumbnail' : THUMBS['hope']
        },
        {
        'title' : 'H2K (2000)',
        'id' : 'PLcajvRZA8E09S7VRCK3XRzIRx9zNKGv5e',
        'thumbnail' : THUMBS['hope']
        },
        {
        'title' : 'Beyond HOPE (1997)',
        'id' : 'PLcajvRZA8E0-4HW1K66VGge3JcUdAEJj5',
        'thumbnail' : THUMBS['hope']
        },
        {
        'title' : 'Hackers On Planet Earth (1994)',
        'id' : 'PLcajvRZA8E0_ckfjqU1irYzOwbsYa2AjC',
        'thumbnail' : THUMBS['hope']
    }],
    'SchmooCon': [{
        'title' : 'SchmooCon 2016',
        'id' : 'PLJgHiyD1pZg70X3X3zjmdmZg3u0eqDFJ4',
        'thumbnail' : THUMBS['schmoocon']
        },
        {
        'title' : 'SchmooCon 2015',
        'id' : 'PLStO1VqVBvmHyVc71QLOCBKugWQyyM7WE',
        'thumbnail' : THUMBS['schmoocon']
    }],
    'SecureWV': [{
        'title' : 'SecureWV/Hack3rcon 2016',
        'id' : 'PLNhlcxQZJSm-wLsEAL9FIXAhC3WY1YvrW',
        'thumbnail' : THUMBS['securewv']
    }],
    'ShowMeCon': [{
        'title' : 'ShowMeCon 2016',
        'id' : 'PLNhlcxQZJSm9NT-zQ9jHdYRhtGOASAYT7',
        'thumbnail' : THUMBS['showmecon']
        },
        {
        'title' : 'ShowMeCon 2015',
        'id' : 'PLNhlcxQZJSm9zsNKfwujM4JgEk1wOc44m',
        'thumbnail' : THUMBS['showmecon']
    }]
}

def get_main_menu():
    return PLAYLISTS.keys()

def get_sub_menu(name):
    return PLAYLISTS[name]

def main_menu():
    for name in get_main_menu():
        # Create a URL for the plugin recursive callback.
        # Example: plugin://plugin.video.example/?action=listing&category=SchmooCon
        url = '{0}?action=listing&category={1}'.format(__url__, name)
        thumbnail = THUMBS[name.lower().replace(" ", "")]
        plugintools.add_item(
            title=name,
            url=url,
            thumbnail=thumbnail,
            fanart=FANART,
            folder=True )

def sub_menu(name):
    for item in get_sub_menu(name):
        plugintools.add_item(
            title=item['title'],
            url="plugin://plugin.video.youtube/playlist/" + item['id'] + "/",
            thumbnail=item['thumbnail'],
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
