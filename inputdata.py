#!/usr/bin/env python
# encoding: utf-8

import redis
import re
import os

rds = redis.StrictRedis(host=os.getenv('REDIS_HOST'),port=6662,db=1)
rds1 = redis.StrictRedis(host=os.getenv('REDIS_HOST'),port=6662,db=2)
f = open("data1.txt")

while True :
    try :
        s = f.next()
    except :
        break
    res = s.split('|')
    print (res)
    res.pop()
    #print len(res)
  # res.pop()
    dic={"group":res[1],"belong":res[0],"name":res[3],"desc":res[4]}
    rds.hmset(res[2],dic)
    rds1.lpush(str(res[0]),res[2])
   # print rds.hvals(res[2])
