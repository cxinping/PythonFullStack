# -*- coding:utf-8 -*-

import re

username = 'weblogic'
password = 'weblogic0'
adminUrl = 't3://localhost:7001'
connect(username,password,adminUrl)

p1 = 'web.*'
apps = re.findall(p1,ls('AppDeployments'))
print(type(apps))
print(len(apps))
print(apps)