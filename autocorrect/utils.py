# Python 3 Spelling Corrector
#
# Copyright 2014 Jonas McCallum.
# Updated for Python 3, based on Peter Norvig's
# 2007 version: http://norvig.com/spell-correct.html
#
# Open source, MIT license
# http://www.opensource.org/licenses/mit-license.php
"""
File reader, concat function and dict wrapper

Author: Jonas McCallum
https://github.com/foobarmus/autocorrect

"""
import re, os, tarfile
from contextlib import closing

PATH = os.path.abspath(os.path.dirname(__file__))
SOURCE_DIR = os.path.split(PATH)[0]
BZ2 = 'words.bz2'
RE = '[A-Za-z]+'

def words_from_archive(filename, map_case=False):
    """extract words from a text file in the archive"""
    bz2 = os.path.join(SOURCE_DIR, BZ2)
    tar_path = os.path.join('words', filename)
    with closing(tarfile.open(bz2, 'r:bz2')) as t:
        with closing(t.extractfile(tar_path)) as f:
            words = set(re.findall(RE, f.read().decode(encoding='utf-8')))
    if map_case:
        return {w.lower():w for w in words}
    return words

def concat(*args):
    """reversed('th'), 'e' => 'hte'"""
    args = list(args)
    for i, arg in enumerate(args):
        if not isinstance(arg, str):
            args[i] = ''.join(arg)
    return ''.join(args)

class Zero(dict):
    """dict with a zero default"""

    def __getitem__(self, key):
        return self.get(key)

    def get(self, key):
        try:
            return super(Zero, self).__getitem__(key)
        except KeyError:
            return 0

zero_default_dict = Zero