#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import errno
import os
import subprocess
import sys

def run_gcc():
    args = sys.argv[1:]
    try:
        proc = subprocess.Popen(args)
        return proc.wait()
    except OSError as e:
        if e.errno == errno.ENOENT:
            print(f"{args[0]}: {e.strerror}", file=sys.stderr)
            print("Is your PATH set correctly?", file=sys.stderr)
        else:
            print(" ".join(args), str(e), file=sys.stderr)
        return e.errno

if __name__ == '__main__':
    sys.exit(run_gcc())
