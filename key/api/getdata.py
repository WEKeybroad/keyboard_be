#!/usr/bin/env python
# encoding: utf-8

from flask import jsonify, request
from . import  api
import redis
import os


@api.route('/key/',methods=['POST'])
def key() :
    system_ = request.get_json().get('system')
    systems = system_.encode("utf-8")
    if systems not in ['Mac','Win'] :
        return jsonify({ "msg" : "not the system"}), 404
    if systems == 'Mac' :
        rds = redis.StrictRedis(host=os.getenv('REDIS_HOST'),port=6662,db=3)
        rds1 = redis.StrictRedis(host=os.getenv('REDIS_HOST'),port=6662,db=4)
    else :
        print type(systems)
        print systems
        rds = redis.StrictRedis(host=os.getenv('REDIS_HOST'),port=6662,db=1)
        rds1 = redis.StrictRedis(host=os.getenv('REDIS_HOST'),port=6662,db=2)

    keys = request.get_json().get('keyword')
    kind = request.get_json().get('kind')
    res = rds.hgetall(keys)
    if len(res) == 0 :
        return jsonify({ "msg1" : "none"}) , 404

    res.update({"keys":keys})
    group = res['group']
    belong = res['belong']
    if kind.encode("utf-8") != belong :
        return jsonify({ "msg" : "not the kind" }), 404

    llen = rds1.llen(belong)
    tmp = rds1.lrange(belong,0,llen)
    tmp = list(set(tmp))
    res1 = []
    for name in  tmp :
        temp = rds.hgetall(name)
        if keys.encode("utf-8") != name and temp['group'] == group :
            temp.update({"keys":name})
            res1.append(temp)
    return jsonify({ 'one' : res ,
                     'more' : res1 }) , 200


