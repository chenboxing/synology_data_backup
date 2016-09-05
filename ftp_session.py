#!/usr/bin/python
# -*- coding: utf-8 -*-

import pysftp
import operator
import time

from ftplib import FTP

class FtpFile:
    def __init__(self):
        self.filename = ""
        self.size = 0
        self.date_ticks = 0
        self.ftp_url = ""

# Ftp操作类
class FtpSession:
    # host: 远程主机IP或域名
    # username: 用户名
    # password: 密码
    # remote_path: 远程下载目录
    def __init__(self,host, username, password, remote_path,port_no=21):
        self.host = host
        self.port_no = port_no
        self.username = username
        self.password = password
        self.remote_path = remote_path
        pass

    # 获取远程目录最新的文件名
    # 返回FtpFile对象
    def get_latest_file(self):
        FtpFile = None

        ftp = FTP()
        ftp.connect('211.102.90.84', 21, 30)
        ftp.login("master", "loveamy1314")

        # ls = []
        # ftp.retrlines('MLSD')
        # ftp.retrlines('MLSD', ls.append)
        # for entry in ls:
        #     print entry

        # list = ftp.nlst()       # 获得目录列表
        # for name in list:
        #     print(name)

        # print(ftp.retrlines('LIST'))
        # aftpdir = ftp.dir()


        pass

# Security Ftp 操作类
class SFtpSession:
    def __init__(self,host, username, password, remote_path,port_no=22):
        self.host = host
        self.username = username
        self.password = password
        self.remote_path = remote_path
        self.port_no = port_no
        pass

    def get_latest_file(self):

        # srv= pysftp.Connection(host='192.168.1.90', username='move8',password="j654cjo ")
        # srv= pysftp.Connection(host='211.102.90.84', username='masster',password="loveamy1314")
        # # 获取目录中最后修改的文件
        # # http://pysftp.readthedocs.io/en/release_0.2.9/pysftp.html#sftpattributes
        #
        # print("asdfasdf")
        # #srv = pysftp.Connection(host="211.102.90.92",username="move8",password="j654cjo ")
        # #srv = sftp.Connection(host="192.168.1.90", username="move8",password="j654cjo ")
        # data = srv.listdir_attr()
        # print data
        # srv.close()
        # for i in data:
        #     print i.filename
        #     print i.st_size
        #     print i.st_mtime

        FtpFile = None
        return FtpFile


# 普通FTP

ftp = FTP()
ftp.connect('211.102.90.84',21,30)
ftp.login("master","loveamy1314")
# list = ftp.nlst()       # 获得目录列表
# for name in list:
#     print(name)

#print(ftp.retrlines('LIST'))
#aftpdir = ftp.dir()

# ls = []
# ftp.retrlines('MLSD')
# ftp.retrlines('MLSD', ls.append)
# for entry in ls:
#     print entry

# folder = FTPDirectory()
# folder.getdata(ftp)
# print(max(folder, key=operator.attrgetter('mtime')).name)

# fields = data.split(';')
# for field in fields:
#     field_name, _, field_value = field.partition('=')
#     if field_name == 'type':
#         target = self.dirs if field_value == 'dir' else self.files
#     elif field_name in ('sizd', 'size'):
#         size = int(field_value)
#     elif field_name == 'modify':
#         mtime = time.mktime(time.strptime(field_value, "%Y%m%d%H%M%S"))
# if target is self.files:



# srv= pysftp.Connection(host='192.168.1.90', username='move8',password="j654cjo ")
# srv= pysftp.Connection(host='211.102.90.84', username='masster',password="loveamy1314")
# # 获取目录中最后修改的文件
# # http://pysftp.readthedocs.io/en/release_0.2.9/pysftp.html#sftpattributes
#
# print("asdfasdf")
# #srv = pysftp.Connection(host="211.102.90.92",username="move8",password="j654cjo ")
# #srv = sftp.Connection(host="192.168.1.90", username="move8",password="j654cjo ")
# data = srv.listdir_attr()
# print data
# srv.close()
# for i in data:
#     print i.filename
#     print i.st_size
#     print i.st_mtime
#


# 获取到文件名,确保文件保唯一
# 查看下载列表是否存在此文件名
# 查看此文件是否已下载

# /volumn5/Data