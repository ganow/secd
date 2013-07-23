# -*- coding: utf-8 -*-

from symbol import isSymbol

class Environment(object):
    def __init__(self, variable, content):
        super(Environment, self).__init__()
        if not isSymbol(variable):
            raise AttributeError('1st arg of Environment must be the Symbol class.')
        self.variable = variable
        self.content = content

    def __repr__(self):
        return '<%s = %s>' % (self.variable, self.content)

def find_var_in_env(var, envs):
    for env in envs:
        if var.isEqual(env.variable):
            return env.content

    return var

def find_list_in_env(lis, envs):
    rtn = []
    for elem in lis: rtn.append(find_var_in_env(elem, envs))
    return rtn