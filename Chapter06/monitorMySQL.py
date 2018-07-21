# -*- coding: utf-8 -*-

import os
import time

# 在Linux下启动MySQL数据库命令
cmd = 'systemctl start mysqld'
print('*** 监听MySQL服务开始了')

while True:
    # 查看MySQL占用的进程号和命令
    mysqld_status = os.popen('ps -C mysqld -o pid,cmd').read()
    mysqld_status_list = mysqld_status.split('\n')
    #print(mysqld_status_list)

    # 使用ps命令查询MySQL占用进程的返回内容,如果返回内容的行数等于小于2时，可以判定为MySQL服务异常退出
    if len(mysqld_status_list) <= 2:

        # 使用os.system()启动MySQL命令，如果返回值为0说明启动MySQL 成功，否则启动MySQL失败。
        status = os.system(cmd)
        if status == 0:
            print('mysqld started...')
        else:
            print('error')

    # 每3秒查询一次MySQL的状态
    time.sleep(3)

