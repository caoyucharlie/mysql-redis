# -*- coding: utf-8 -*-
# 用redis实现发送接收数据
import redis


class RedisBase(object):

    def __init__(self):
        self.__conn = redis.Redis(host='47.92.164.198', port=6379)
        self.pub = 'test'
        self.sub = 'test'
    # 发布

    def publish_msg(self, msg):
        self.__conn.publish(self.pub, msg)
    # 订阅

    def subscribe_msg(self):
        pub = self.__conn.pubsub()
        pub.subscribe(self.pub)
        pub.parse_response()
        return pub




# publish
from myredis import RedisBase

obj = RedisBase()
msg = 'hello, world'
obj.publish_msg(msg)

# subscribe
from myredis import RedisBase

obj = RedisBase()
redis_sub = obj.subscribe_msg()

while True:
    msg = redis_sub.parse_response()
    print('msg:%s' % msg)