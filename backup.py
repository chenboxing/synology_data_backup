#! /usr/bin/env python
# -*- coding: utf-8 -*-


import logging
import logging.config
import ConfigParser
import string,os,sys


import ftp_session
import dsm

# 日志
logging.config.fileConfig("logger.conf")
logger = logging.getLogger("example01")


# 加载配置配置文件,获取DSN参数需要远程下载的任务数
# 返回值
# dsm:字典
# tasks: 列表,存放下载任务字典
def load_config():

    dsm = {}
    tasks = []

    try:
        cf =  ConfigParser.ConfigParser()
        cf.read("settings.conf")

        # 获取所有节
        secs = cf.sections()
        for sec in secs:
            task = {}
            if sec == "dsm":
               task = dsm

            for item in cf.items(sec):
                task[item[0]] = item[1]

            if sec.startswith("task_"):
                task_key = sec.replace("task_","")
                task["task_key"] = task_key
                tasks.append(task)

    except Exception as e:
        logger.error("加载配置文件出现异常:{}".format(e))


    return (dsm,tasks)

def file_exists(file_path):
    return os.path.exists(file_path)


# 主函数
def main():

    # 加载配置文件
    dsm_info,tasks_info = load_config()

    if len(dsm_info) == 0  or len(tasks_info) == 0:
        logger.error("获取参数为空,{},{}".format(dsm_info,tasks_info))
        return


    # 遍历每个下载任务,获取ftp/sftp下载url
    for task in tasks_info:
        ftp_file = None

        if task["ftp_type"] == "ftp":
            ftp_session = FtpSession()
            ftp_file =  ftp_session.get_latest_file()
        elif task["ftp_type"] == "sftp":
            ftp_session = SFtpSession()
            ftp_file = ftp_session.get_latest_file()
        if not ftp_file is None:
            task_key = dsm_info,task["task_key"]
            dsm = DSM(dsm_info,task_key)
            target_file = ospath.join(dsm["dsm_data_folder"],task_key,ftp_file.filename)

            if not file_exists(ftp_file.name) and not dsm.task_exist(ftp_file.name):   #如果文件

                dir_path = os.path.dirname(target_file)
                # 如果存放下载文件的目录不存在,则创建下载目录
                if not os.path.exists(dir_path)
                    os.makedirs(dir_path)

                # 创建下载任务
                dsm.create_task(ftp_file.url)
                logger.info "已添加任务{}到Download Station".format(ftp_file.url)

if __name__ == '__main__':
    main()