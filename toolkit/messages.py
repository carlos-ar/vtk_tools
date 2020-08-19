#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 12:44:47 2018

@author: carlosruvalcaba
"""

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# Set up cases for runs
#
# C. A. Ruvalcaba-- UC Davis (2018)

# temp to convert to Python 3
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

def status(short_string,pad_length):
    # to remember
    # double quotes + r in front for escaping \n (not used)
    # double {{}} for literal in format
    status = ''
    for i in range(0,3):
        fmt = '{{{0}:-^{1}s}}\n'.format(i, pad_length)
        status += fmt+'\n'

    print('')
    print(status.format('',short_string,''))
    print('')

def notification(short_string,pad_length):
    # to remember
    # double quotes + r in front for escaping \n (not used)
    # double {{}} for literal in format
    status = ''
    for i in range(0,3):
        fmt = '{{{0}:-^{1}s}}'.format(i, pad_length)
        status += fmt +'\n'
    print('')
    print(status.format('',short_string,''))
    print('')

def warning(short_string):
    # to remember
    # double quotes + r in front for escaping \n (not used)
    # double {{}} for literal in format
    # warning 
    pad_length = 60
    status = ''
    for i in range(0,3):
        fmt = '{{{0}:!^{1}s}}'.format(i, pad_length)
        status += fmt+'\n'

    print('')
    print(status.format('','WARNING: '+short_string,''))
    print('')