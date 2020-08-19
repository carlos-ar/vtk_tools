#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 10:59:37 2020

@author: carlosar
"""

import os, errno, shutil

def make_save_directory(directory, printflag=False):
    try:
        if printflag is True:
            print('Made directory: \n{0}'.format(directory))
        os.makedirs(directory)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    return

def delete_files(folder):
    # https://stackoverflow.com/questions/185936/how-to-delete-the-contents-of-a-folder
    # folder = '/path/to/folder'
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))