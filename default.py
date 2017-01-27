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

addonID = 'plugin.video.infosecflix'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

# menu / playlist config
def infosec_list():
    thumbnails = {
        'converge' : 'https://www.convergeconference.org/wp-content/uploads/2016/10/converge_logo_home-Copy.png',
        'schmoocon' : 'https://pbs.twimg.com/profile_images/357342497/Shmoo_Eyes_400x400.jpg',
        'derbycon' : 'https://pbs.twimg.com/profile_images/1100903441/derbyconlogo-Twitter_400x400.jpg',
        'grrcon' : 'http://grrcon.com/wp-content/themes/grrcon/images/logo.png',
        'blackhat' : 'https://pbs.twimg.com/profile_images/730168530440609792/EgTOmf8I_400x400.jpg',
        'defcon' : 'https://pbs.twimg.com/profile_images/794271957818580992/QJ06URkq_400x400.jpg',
        'showmecon' : 'https://pbs.twimg.com/profile_images/789200425962450945/_I_Q0wy5_400x400.jpg',
        'circlecitycon' : 'https://pbs.twimg.com/profile_images/378800000397493274/efb9db3e911e52f08dc7ca7beb6ef405_400x400.jpeg',
        'securewv' : 'https://pbs.twimg.com/profile_images/737851153036283904/Bh6iVwvD_400x400.jpg',
        'bsides' : 'https://i.imgur.com/ABoCVMD.jpg'
    }

    menu = [
        {
            'title' : 'ConVerge 2016',
            'id' : 'PLNhlcxQZJSm9HnVtDwMQ_JN1bCTuOedMh',
            'thumbnail' : thumbnails['converge']
        },
        {
            'title' : 'SecureWV/Hack3rcon 2016',
            'id' : 'PLNhlcxQZJSm-wLsEAL9FIXAhC3WY1YvrW',
            'thumbnail' : thumbnails['securewv']
        },
        {
            'title' : 'SchmooCon 2016',
            'id' : 'PLJgHiyD1pZg70X3X3zjmdmZg3u0eqDFJ4',
            'thumbnail' : thumbnails['schmoocon']
        },
        {
            'title' : 'SchmooCon 2015',
            'id' : 'PLStO1VqVBvmHyVc71QLOCBKugWQyyM7WE',
            'thumbnail' : thumbnails['schmoocon']
        },
        {
            'title' : 'DerbyCon 6.0 (2016)',
            'id' : 'PLNhlcxQZJSm9T78xh_QYYiqkTjIt4jYgm',
            'thumbnail' : thumbnails['derbycon']
        },
        {
            'title' : 'DerbyCon 5.0 (2015)',
            'id' : 'PLNhlcxQZJSm8cr3iBN27VZ4Rm11Erbae-',
            'thumbnail' : thumbnails['derbycon']
        },
        {
            'title' : 'DerbyCon 4.0 (2014)',
            'id' : 'PLNhlcxQZJSm8o9c_2_iDDTV6tCPdMp5dg',
            'thumbnail' : thumbnails['derbycon']
        },
        {
            'title' : 'DerbyCon 3.0 (2013)',
            'id' : 'PLNhlcxQZJSm-Wo3Kpvn8oIm_rD5PwlmHX',
            'thumbnail' : thumbnails['derbycon']
        },
        {
            'title' : 'DerbyCon 2.0 (2012)',
            'id' : 'PLNhlcxQZJSm97hLg2WXjW1qTytN-pbDtv',
            'thumbnail' : thumbnails['derbycon']
        },
        {
            'title' : 'DerbyCon 1.0 (2011)',
            'id' : 'PL2ABA97A5B8AA1005',
            'thumbnail' : thumbnails['derbycon']
        },
        {
            'title' : 'GrrCon 2016',
            'id' : 'PLNhlcxQZJSm88_x7IQKSFzhtp9ileHB72',
            'thumbnail' : thumbnails['grrcon']
        },
        {
            'title' : 'GrrCon 2015',
            'id' : 'PLNhlcxQZJSm-lvGvO_MQ6x08wdwLdh4YJ',
            'thumbnail' : thumbnails['grrcon']
        },
        {
            'title' : 'ShowMeCon 2016',
            'id' : 'PLNhlcxQZJSm9NT-zQ9jHdYRhtGOASAYT7',
            'thumbnail' : thumbnails['showmecon']
        },
        {
            'title' : 'ShowMeCon 2015',
            'id' : 'PLNhlcxQZJSm9zsNKfwujM4JgEk1wOc44m',
            'thumbnail' : thumbnails['showmecon']
        },
        {
            'title' : 'CircleCityCon 2016',
            'id' : 'PLNhlcxQZJSm_fAztb-LmQapZiEM08cV-6',
            'thumbnail' : thumbnails['circlecitycon']
        },
        {
            'title' : 'CircleCityCon 2015',
            'id' : 'PLNhlcxQZJSm9TV35bUYvhjUpdAR8iPT5R',
            'thumbnail' : thumbnails['circlecitycon']
        },
        {
            'title' : 'CircleCityCon 2014',
            'id' : 'PLNhlcxQZJSm8AQVCGin_go3JgJe4dVgPR',
            'thumbnail' : thumbnails['circlecitycon']
        },
        {
            'title' : 'Black Hat USA 2016',
            'id' : 'PLH15HpR5qRsXm0-rMacuWBxWcB2fmsmEw',
            'thumbnail' : thumbnails['blackhat']
        },
        {
            'title' : 'Black Hat USA 2015',
            'id' : 'PLH15HpR5qRsXF78lrpWP2JKpPJs_AFnD7',
            'thumbnail' : thumbnails['blackhat']
        },
        {
            'title' : 'Black Hat USA 2014',
            'id' : 'PLH15HpR5qRsUBgeytB_T4xnKzr4Iv3upj',
            'thumbnail' : thumbnails['blackhat']
        },
        {
            'title' : 'Black Hat USA 2013',
            'id' : 'PLH15HpR5qRsUtTv7IQKftKGOcRLGtwuoF',
            'thumbnail' : thumbnails['blackhat']
        },
        {
            'title' : 'Bsides Augusta 2016',
            'id' : 'PLNhlcxQZJSm_4V8VDudQyBFp8b91rBHTj',
            'thumbnail' : thumbnails['bsides']
        },
        {
            'title' : 'Bsides Detroit 2016',
            'id' : 'PLNhlcxQZJSm-AtNWUBV2eI_zNDGHRrbhk',
            'thumbnail' : thumbnails['bsides']
        },
        {
            'title' : 'Bsides Nashville 2016',
            'id' : 'PLNhlcxQZJSm8OerdQZyQAdi7GG1ufgRaw',
            'thumbnail' : thumbnails['bsides']
        },
        {
            'title' : 'Bsides Knoxville 2016',
            'id' : 'PLNhlcxQZJSm_AgX2w6eHs3EIeaErUlm-5',
            'thumbnail' : thumbnails['bsides']
        },
        {
            'title' : 'Bsides SF 2016',
            'id' : 'PLNhlcxQZJSm_vceoN_dHHm44mpT_UbaWF',
            'thumbnail' : thumbnails['bsides']
        },
        {
            'title' : 'Bsides LV 2015',
            'id' : 'PLNhlcxQZJSm_wpMC42BKPCknT-JhnZGos',
            'thumbnail' : thumbnails['bsides']
        },
        {
            'title' : 'Bsides Tampa 2015',
            'id' : 'PLNhlcxQZJSm_by2u3gZUlcPPU0IQtvRTS',
            'thumbnail' : thumbnails['bsides']
        },
        {
            'title' : 'DEF CON 24 (2016)',
            'id' : 'PL9fPq3eQfaaAvXV3hJc4yHuNxoviVckoE',
            'thumbnail' : thumbnails['defcon']
        },
        {
            'title' : 'DEF CON 23 (2015)',
            'id' : 'PL9fPq3eQfaaBuHqVvDzPoWxznYYmyx5UX',
            'thumbnail' : thumbnails['defcon']
        },
        {
            'title' : 'DEF CON 22 (2014)',
            'id' : 'PL9fPq3eQfaaBCdjbKFYjosh1s1EkaYdsQ',
            'thumbnail' : thumbnails['defcon']
        },
        {
            'title' : 'DEF CON 21 (2013)',
            'id' : 'PL9fPq3eQfaaBD_8E9PJ8yyiTL0JhynlGK',
            'thumbnail' : thumbnails['defcon']
        },
        {
            'title' : 'DEF CON 20 (2012)',
            'id' : 'PL9fPq3eQfaaDcbIEMSzdL5yuzh_m6BB-E',
            'thumbnail' : thumbnails['defcon']
        },
        {
            'title' : 'DEF CON 19 (2011)',
            'id' : 'PL9fPq3eQfaaBoESMifnn5w4S487vrmGR6',
            'thumbnail' : thumbnails['defcon']
        },
        {
            'title' : 'DEF CON 18 (2010)',
            'id' : 'PL9fPq3eQfaaC26TgwyDg2Db-m5E7jRRbj',
            'thumbnail' : thumbnails['defcon']
        },
        {
            'title' : 'DEF CON 17 (2009)',
            'id' : 'PL9fPq3eQfaaDjnjDsjgmtASOWg8a8neEE',
            'thumbnail' : thumbnails['defcon']
        },
        {
            'title' : 'DEF CON 16 (2008)',
            'id' : 'PL9fPq3eQfaaBY3OjTaGyaBzgc80sOFkG8',
            'thumbnail' : thumbnails['defcon']
        },
        {
            'title' : 'DEF CON 15 (2007)',
            'id' : 'PL9fPq3eQfaaCji1aEQBUrIpPQf9-HazLL',
            'thumbnail' : thumbnails['defcon']
        },
        {
            'title' : 'DEF CON 14 (2006)',
            'id' : 'PL9fPq3eQfaaAxDI0xo83ZFzDAZgXO3Yhy',
            'thumbnail' : thumbnails['defcon']
        },
        {
            'title' : 'DEF CON 13 (2005)',
            'id' : 'PL9fPq3eQfaaBwvKmscgwI2B-S981fgVrH',
            'thumbnail' : thumbnails['defcon']
        },
        {
            'title' : 'DEF CON 12 (2004)',
            'id' : 'PL9fPq3eQfaaAU98_NKiJ-7simP1s-O2zs',
            'thumbnail' : thumbnails['defcon']
        },
        {
            'title' : 'DEF CON 11 (2003)',
            'id' : 'PL9fPq3eQfaaAlKSZpQad9gwnASyhJ33Zi',
            'thumbnail' : thumbnails['defcon']
        },
        {
            'title' : 'DEF CON 10 (2002)',
            'id' : 'PL9fPq3eQfaaChpuiKkNQ0uwmYdpPoI65z',
            'thumbnail' : thumbnails['defcon']
        },
        {
            'title' : 'DEF CON 9 (2002)',
            'id' : 'PL9fPq3eQfaaCzGwJQmga1SRJUedjp2t5c',
            'thumbnail' : thumbnails['defcon']
        },
        {
            'title' : 'DEF CON 8 (2001)',
            'id' : 'PL9fPq3eQfaaCotE0QrvM2eTmm-59Gvt9Z',
            'thumbnail' : thumbnails['defcon']
        },
        {
            'title' : 'DEF CON 7 (2000)',
            'id' : 'PL9fPq3eQfaaBxFm9YU4aafXz75peLDXhX',
            'thumbnail' : thumbnails['defcon']
        }
    ]

    return menu

# Entry point
def run():
    plugintools.log("docu.run")

    # Get params
    params = plugintools.get_params()

    if params.get("action") is None:
        main_list(params)
    else:
        action = params.get("action")
        exec action+"(params)"

    plugintools.close_item_list()

# Main menu
def main_list(params):
    plugintools.log("docu.main_list "+repr(params))

    for item in infosec_list():
        plugintools.add_item(
            #action="",
            title=item['title'],
            url="plugin://plugin.video.youtube/playlist/" + item['id'] + "/",
            thumbnail=item['thumbnail'],
            folder=True )
run()
