# -*- coding:utf-8 -*-
import re

# WebLogic Server IP地址
ip = '127.0.0.1'
# 部署的web应用名称
webAppName = r'web2'
# webLogic Server 用户
username = 'weblogic'
# webLogic Server 密码
password = 'weblogic0'
# URL
adminUrl = 't3://' +ip + ':7001'
# webLogic 目标服务器
targetServer = 'AdminServer'
# 部署的web应用地址
webAppPath = r'c:/web2'

# 连接到WebLogic Server实例
connect(username,password,adminUrl)

p1 = webAppName
apps = re.findall(p1, ls('AppDeployments'))

# 判断是否已经部署了web应用，如果部署了先卸载应用在部署应用
if len(apps)> 0:
	# 卸载web应用
    undeploy(webAppName)
    print('deployed ',webAppName)

# 部署web应用	
deploy(appName=webAppName,path = webAppPath,targets=targetServer)
print('*** deploy web app Successfly ***')

# 断开 WLST 与 WebLogic Server 实例的连接
disconnect()
