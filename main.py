#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 20:53:34 2020

@author: carlosar
"""


import os
import testing_pyevtk
import testing_meshio
import toolkit.messages as msg
import toolkit.helpers as helpers


def test_meshio(outdir='./outdata/meshio'):
    helpers.make_save_directory(outdir)
    helpers.delete_files(outdir)
    mesh_types = ['tri','quad', 'hex']
    for m in mesh_types:
        str_out = 'making mesh: '+m+'\nin: '+outdir
        msg.status(str_out, 20)
        fname = os.path.join(outdir,m)
        p, c = testing_meshio.mesh(m)
        p, c = testing_meshio.make_mesh(m)
        d = testing_meshio.make_vector_data(p)
        testing_meshio.write_vtk_file(fname, p, c, d)
        testing_meshio.write_xdmf(fname, p, c, d)

def main():
    print('main')
    
    # testing_pyevtk.structured_example()

    # testing_pyevtk.vector_field()
    test_meshio()
if __name__ == '__main__':
   msg.status('Running application',40)
   main()
   msg.status('Finishing application run',40)