# -*- coding: utf-8 -*-

from environment import Environment

def hd(lis):
    if lis.__class__ != list:
        return lis
    else:
        if lis == []:
            return []
        else:
            return lis[0]
    # return lis[0]

def tl(lis):
    # if lis.__class__ != list:
    #     return lis
    # else:
    #     return lis[1:]
    return lis[1:]

def cons(lhs, rhs):
    rtn = []
    if lhs.__class__ == list:
        rtn.extend(lhs)
    else:
        rtn.append(lhs)
    if rhs.__class__ == list:
        rtn.extend(rhs)
    else:
        rtn.append(rhs)

    return rtn

def assoc(bv, stack_2nd):
    return Environment(bv, stack_2nd)

def derive(env, env_list):
    # rtn = [env]
    # for x in env_list: rtn.append(x)
    return cons(env, env_list)

def unitlist(body):
    return [body]
