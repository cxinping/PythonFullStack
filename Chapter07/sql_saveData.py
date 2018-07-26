# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
import pandas as pd

# 初始化引擎
engine = create_engine('mysql+pymysql://root:123456@127.0.0.1:3306/mytestdb?charset=utf8')

sdata1 = {'name' : ['王五1','王五2'], 'age' : [20, 21], 'sex':['female','male'] , 'income':[5000,6000]   }
df1 = pd.DataFrame(sdata1 )

# 使用Pandas的to_sql方法将DataFrame对象直接入库
df1.to_sql('employee', con=engine, if_exists='append')


