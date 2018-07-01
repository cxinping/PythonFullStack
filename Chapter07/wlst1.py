# -*- coding:utf-8 -*-

import re

# webLogic Server 用户
username = 'weblogic'
# webLogic Server 密码
password = 'weblogic0'
# URL 地址
adminUrl = 't3://localhost:7001'
# 连接到WebLogic Server实例
connect(username,password,adminUrl)

p1 = 'web.*'
# 使用正则表达式，匹配已经部署的java web应用名称中，以web命名的
apps = re.findall(p1,ls('AppDeployments'))
# 显示apps的类型
print("type(apps)= %s" % type(apps))
# 显示apps的数量
print("len(apps)=%s" % len(apps))
print(apps)

# 断开 WLST 与 WebLogic Server 实例的连接
disconnect()