from secd import SECDMachine
from parse import Parser

secd = SECDMachine()
p = Parser()

def test(fname):
    secd.clear()
    code = p.run_from_file(fname)
    secd.c = [code]
    return secd.update()