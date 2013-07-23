# -*- coding: utf-8 -*-

import re, sys

from symbol import Symbol, isSymbol
from lambda_eq import LambdaEq, Combination, isLambdaSymbol, isLambdaEq

class Parser(object):
    def __init__(self):
        super(Parser, self).__init__()

    def corresponded_paren(self, idx, src):
        right_paren = 1

        for i, c in enumerate(src[idx+1:]):
            if c == '(':
                right_paren += 1
            elif c == ')':
                right_paren -= 1
                if right_paren == 0:
                    return i+1
            else: pass
        raise SyntaxError("uncorrespond paren")
        return -1

    def sandByParen(self, src):
        if src[0] == '(' and src[-1] == ')':
            return True
        else: return False

    def canBePeeled(self, src):
        if self.sandByParen(src):
            if self.corresponded_paren(0, src) == len(src)-1:
                return True
        else: return False

    def peel(self, src):
        return src[1:-1]

    def canBeDecomposed(self, src):
        right_vs_left = 0

        for c in src:
            if c == '(':
                right_vs_left += 1
            elif c == ')':
                right_vs_left -= 1
            elif c == ' ' and right_vs_left == 0:
                return True
            else: pass

        return False

    def decompose(self, src):
        right_vs_left = 0
        data = []
        buf = ''

        for c in src:
            if c == '(':
                right_vs_left += 1
                buf = buf + c
            elif c == ')':
                right_vs_left -= 1
                buf = buf + c
            elif c == ' ' and right_vs_left == 0:
                data.append(buf)
                buf = ''
            else:
                buf = buf + c

        data.append(buf)
        return data

    def parse(self, src):
        if self.canBePeeled(src):
            return self.parse(self.peel(src))
        elif self.canBeDecomposed(src):
            return [self.parse(x) for x in self.decompose(src)]
        else:
            return Symbol(src)

    def lambdanize(self, data_list):
        if isSymbol(data_list):
            return data_list
        else:
            if len(data_list) == 3:
                if isLambdaSymbol(data_list[0]):
                    return LambdaEq(data_list[1], self.lambdanize(data_list[2]))
                else:
                    return [self.lambdanize(x) for x in data_list]
            else:
                return [self.lambdanize(x) for x in data_list]

    def combine(self, data_list):
        if isSymbol(data_list):
            return data_list
        elif isLambdaEq(data_list):
            return data_list
        else:
            if len(data_list) == 2:
                if isLambdaEq(data_list[0]):
                    return Combination(data_list[0], self.combine(data_list[1]))
                else:
                    return [self.combine(x) for x in data_list]
            else:
                return [self.combine(x) for x in data_list]

    def open_file(self, fname):
        return open(fname, 'r').readlines()

    def pre_process(self, code_list):
        src = ''.join([re.sub(r'\n', ' ', x) for x in code_list])
        src = re.sub(r'\t', ' ', src)
        src = re.sub(r'[\s]+', ' ', src)
        src = re.sub('\)[\s]*\(', ') (', src)
        if src[-1] == ' ':
            src = src[:-1]
        return src

    def run(self, code_list):
        return self.combine(self.lambdanize(self.parse(self.pre_process(code_list))))

    def run_from_file(self, fname):
        return self.run(self.open_file(fname))

if __name__ == '__main__':
    fname = sys.argv[1]

    p = Parser()
    print p.run_from_file(fname)