#!/usr/bin/env python
# encoding: utf-8

import redis
import re

rds = redis.StrictRedis(host='localhost',port=6666,db=1)
rds1 = redis.StrictRedis(host='localhost',port=6666,db=3)
f = open("data.txt")

while True :
    try :
        s = f.next()
    except :
        break
    res = s.split('|')
    print res
    res.pop()
    for item in res :
        print item ,
    print
    #print len(res)
  # res.pop()
    dic={"group":res[1],"belong":res[0],"name":res[3],"desc":res[4]}
    rds.hmset(res[2],dic)
    rds1.lpush(str(res[0]),res[2])
   # print rds.hvals(res[2])
