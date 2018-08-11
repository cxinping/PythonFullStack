
import os

result = os.popen("ping 127.0.0.1 ").read()
# 返回运行结果
print(result)
