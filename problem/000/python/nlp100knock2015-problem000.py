#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pprint
pp = pprint.PrettyPrinter(indent=2)
import sys

char = "stressed"
char_list = list(char)

#pp.pprint(char_list)
char_list.reverse()

for tmp in char_list:
    #print(tmp)
    sys.stdout.write(tmp)

print("")
