#! /usr/bin/env python
# -*- coding: utf-8 -*-

##
# 使用Synology Download Station API远程控制文件下载
# https://global.download.synology.com/download/Document/DeveloperGuide/Synology_Download_Station_Web_API.pdf
##


import json,urllib, urllib2, os, sys

class DownloadStation:
    def __init__(self,nas_url, nas_username, nas_password):

        self.nas_url = nas_url
        self.nas_username = nas_username
        self.nas_password = nas_password

        self.sessionID = ''
        #self.tryLogin()
        self.debugInfo = {}
        self.lastError = ''

    def post(self, cgipath, data, subdir=''):
        if not isinstance(data, dict):
            logger.error("data参数应为字典")
            return
        if not data.has_key('version'):
            data.update({'version': 1})
        if not data.has_key('_sid'):
            data.update({'_sid': self.sessionID})
        data = urllib.urlencode(data)
        # i.e. http://192.168.1.11:5000/webapi/auth.cgi?xxxxx
        url = os.path.join(self.nas_url, 'webapi', subdir, cgipath)
        try:

            request = urllib2.urlopen(url, data)
            res = json.load(request)
        except:
            res = {'error': {'code': -1},'success': False}
        return res

    def login(self):
        data = { 'api':     'SYNO.API.Auth',
                 'method':  'login',
                 'version': 2,
                 'account': self.nas_username,
                 'passwd':  self.nas_password,
                 'session': 'DownloadStation',
        }
        res = self.post('auth.cgi', data)
        if not self.isSuccess(res):
            self.die( self.lastError )
        self.sessionID = res['data']['sid']

    def logout(self):
        data = { 'api':     'SYNO.API.Auth',
                 'method':  'logout',
                 'session': 'DownloadStation'
        }
        res = self.post('auth.cgi', data)
        self.sessionID = ''

    def try_login(self):
        if self.sessionID == '':
            self.login()

    # url路径当前是否正下载中
    def task_exists(self,url):
        # 获取所有任务

    # 创建新的下载任务 参数可以是本地文件或链接
    def create_task(self, url):
        self.try_login()
        if not isinstance(url, (str, unicode, list)):
            self.die('arguments error')
        uris = ','.join(url) if isinstance(url, list) else url
        try:
            if os.path.isfile(uris):
                # 使用file参数似乎有问题 自己读
                with open(uris, 'r') as fp:
                    uris = ','.join(map(lambda s: s.strip('\n \t\r'), fp.readlines()))
        except:
            pass
        data = {'api': 'SYNO.DownloadStation.Task',
                'method': 'create',
                'uri': uris
                }
        data['destination'] = 'Data/ovf'
        res = self.post('DownloadStation/task.cgi', data)
        if not self.isSuccess(res):
            self.die(self.lastError)
        print('task created.')

