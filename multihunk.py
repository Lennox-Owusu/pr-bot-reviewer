def load(path):
    data = open(path).read()
    return eval(data)              # BUG: eval() on file contents (code injection)


def helper(x):
    return x + 1


def run(cmd):
    import os
    return os.system(cmd)          # BUG: command injection via os.system
