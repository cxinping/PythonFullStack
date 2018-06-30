# -*- coding:utf-8 -*-


import re
import sys

ip = sys.argv[0]
webAppName = r'web4'
username = 'weblogic'
password = 'weblogic0'
adminUrl = 't3://' +ip + ':7001'
targetServer = 'AdminServer'
webAppPath = r'e:/python/web/web4'
connect(username,password,adminUrl)


p1 = webAppName
apps = re.findall(p1, ls('AppDeployments'))

if len(apps)> 0:
    undeploy(webAppName)
    print('deployed ',webAppName)
deploy(appName=webAppName,path = webAppPath,targets=targetServer)
print('Successfly:')