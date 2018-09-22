### WebLogic 数据源配置信息
# weblogic的服务器地址
url = 'localhost:7001'
# 登录用户名
username = 'weblogic'
# 登录密码
password = 'weblogic0'
# 数据源名称
dsName = 'mysql_ds'
# JNDI名称
dsJNDIName = 'jdbc/mysql'
# 目标服务器名称
targetName = 'AdminServer'
initialCapacity = 1
maxCapacity = 10
capacityIncrement = 1
driverName = 'com.mysql.jdbc.Driver'
driverURL = 'jdbc:mysql://localhost:3306/mytestdb'
driverUsername = 'root'
driverPassword = '123456'

# 连接到WebLogic Server 
connect(username, password, url)

# 检查数据源是否已经存在
try:
	cd('/JDBCSystemResources/' + dsName)
	print 'The JDBC Data Source ' + dsName + ' already exists.'
	exit()
except WLSTException:
	pass

print( 'Creating new JDBC Data Source named ' + dsName + '.' )

edit()
startEdit()
cd('/')

# 保存引用的目标服务器
targetServer = getMBean('/Servers/' + targetName)

# 创建数据源 JDBCSystemResource
jdbcSystemResource = create(dsName, 'JDBCSystemResource')
jdbcResource = jdbcSystemResource.getJDBCResource()
jdbcResource.setName(dsName)

# 设置 JNDI 名称
jdbcResourceParameters = jdbcResource.getJDBCDataSourceParams()
jdbcResourceParameters.setJNDINames([dsJNDIName])
jdbcResourceParameters.setGlobalTransactionsProtocol('TwoPhaseCommit')

# 创建连接池
connectionPool = jdbcResource.getJDBCConnectionPoolParams()
connectionPool.setInitialCapacity(initialCapacity)
connectionPool.setMaxCapacity(maxCapacity)
connectionPool.setCapacityIncrement(capacityIncrement)

# 创建驱动设置
driver = jdbcResource.getJDBCDriverParams()
driver.setDriverName(driverName)
driver.setUrl(driverURL)
driver.setPassword(driverPassword)
driverProperties = driver.getProperties()
userProperty = driverProperties.createProperty('user')
userProperty.setValue(driverUsername)

# 保存目标数据源
jdbcSystemResource.addTarget(targetServer)

# 保存已完成但尚未保存的编辑 
save()
# 激活在当前编辑会话期间已保存但尚未部署的更改。
activate(block='true')
print( 'Data Source created successfully.')
exit()






