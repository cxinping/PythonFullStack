# -*- coding: utf-8 -*-

import random
from multiprocessing.managers import BaseManager
from multiprocessing import Queue

# 发送任务的队列
task_queue = Queue()
# 接收结果的队列
result_queue = Queue()

def return_task_queue():
    global task_queue
    return task_queue

def return_result_queue():
    global result_queue
    return result_queue

# 从BaseManager继承的QueueManager
class QueueManager(BaseManager):
    pass

if __name__ == '__main__':
    # 把两个Queue都注册到网络上, callable参数关联了Queue对象
    QueueManager.register('get_task_queue', callable=return_task_queue)
    QueueManager.register('get_result_queue', callable=return_result_queue)
    # 绑定端口5000, 设置验证码'abc'
    manager = QueueManager(address=('127.0.0.1', 5000), authkey=b'abc')
    # 启动Queue
    manager.start()

    # 获得通过网络访问的Queue对象
    task = manager.get_task_queue()
    result = manager.get_result_queue()

    # 放10个任务进去
    for i in range(10):
        n = random.randint(0, 10000)
        print('Put task %d' % n)
        # 对task_queue进行写入数据，相当于分配任务
        task.put(n)

    # 从result队列读取结果:
    print('Try get results.')
    for i in range(10):
        # 等待workers处理后返回的结果，响应过期时间为10秒
        r = result.get(timeout=10)
        print('Result:%s' % r)

    # 关闭Queue
    manager.shutdown()
