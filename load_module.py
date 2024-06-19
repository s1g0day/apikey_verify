# coding:utf-8
import gevent
from gevent.pool import Pool
from gevent import monkey;monkey.patch_all()
import urllib3
urllib3.disable_warnings()

from modules.Binaryedge_APIKEY import binaryedge_apikey_verify
from modules.Censys_APIKEY import censys_apikey_verify
from modules.Fofa_APIKEY import fofa_apikey_verify
from modules.Hunter_io_APIKEY import hunter_io_apikey_verify
from modules.Hunter_qianxin_APIKEY import hunter_qianxin_apikey_verify
from modules.Quake_APIKEY import quake_apikey_verify
from modules.Shodan_APIKEY import shodan_apikey_verify
from modules.ViruStotal_APIKEY import virustotal_apikey_verify
from modules.ZoomEyeHK_Api_APIKEY import zoomeyehk_api_apikey_verify
from modules.GithubApi_APIKEY import github_apikey_verify
from modules.Fullhunt_APIKEY import fullhunt_apikey_verify
from modules.SecurityTrails_APIKEY import securitytrails_apikey_verify

def load_module(type, files):

    APIlist = [
        binaryedge_apikey_verify,
        censys_apikey_verify,
        fofa_apikey_verify,
        hunter_io_apikey_verify,
        hunter_qianxin_apikey_verify,
        quake_apikey_verify,
        shodan_apikey_verify,
        virustotal_apikey_verify,
        zoomeyehk_api_apikey_verify,
        github_apikey_verify,
        fullhunt_apikey_verify,
        securitytrails_apikey_verify,
    ]

    def pocexec(poc_func, files):
        poc_func(files)
        gevent.sleep(0)

    if type:
        for api_func in APIlist:
            if type in api_func.__name__:
                pocexec(api_func, files)
    else:
        print("NO Type")
