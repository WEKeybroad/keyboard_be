#!/usr/bin/env python
# encoding: utf-8

from flask import jsonify, request
from . import  api
import redis
rds = redis.StrictRedis(host='localhost',port=6666,db=1)
rds1 = redis.StrictRedis(host='localhost',port=6666,db=3)

@api.route('/key/',methods=['POST'])
def key() :
    keys = request.get_json().get('keyword')
    res = rds.hgetall(keys)
    if len(res) == 0 :
        return jsonify({ "msg" : "none"}) , 404
    res.update({"keys":keys})
    group = res['group']
    belong = res['belong']
    llen = rds1.llen(belong)
  #  print llen
    tmp = rds1.lrange(belong,0,llen)
    tmp = list(set(tmp))
    res1 = []
    for name in  tmp :
        temp = rds.hgetall(name)
        if keys.encode("utf-8") != name and temp['group'] == group :
            temp.update({"keys":name})
            res1.append(temp)
   # res1 = set(res1)
    return jsonify({ 'one' : res ,
                     'more' : res1 }) , 200

