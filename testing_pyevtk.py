#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 18:53:35 2020

@author: carlosar
"""
import toolkit.helpers as helpers
import os
outdir = './outdata/pyevtk'
helpers.make_save_directory(outdir)
helpers.delete_files(outdir)

def structured_example():
    # directly copied from the pyevtk github examples: 
    # pyevtk/examples/structured.py
    
    
    from pyevtk.hl import gridToVTK
    import numpy as np
    import random as rnd
    
    # Dimensions
    nx, ny, nz = 6, 6, 2
    lx, ly, lz = 1.0, 1.0, 1.0
    dx, dy, dz = lx / nx, ly / ny, lz / nz
    
    ncells = nx * ny * nz
    npoints = (nx + 1) * (ny + 1) * (nz + 1)
    
    # Coordinates
    X = np.arange(0, lx + 0.1 * dx, dx, dtype="float64")
    Y = np.arange(0, ly + 0.1 * dy, dy, dtype="float64")
    Z = np.arange(0, lz + 0.1 * dz, dz, dtype="float64")
    
    x = np.zeros((nx + 1, ny + 1, nz + 1))
    y = np.zeros((nx + 1, ny + 1, nz + 1))
    z = np.zeros((nx + 1, ny + 1, nz + 1))
    
    # We add some random fluctuation to make the grid
    # more interesting
    for k in range(nz + 1):
        for j in range(ny + 1):
            for i in range(nx + 1):
                x[i, j, k] = X[i] + (0.5 - rnd.random()) * 0.1 * dx
                y[i, j, k] = Y[j] + (0.5 - rnd.random()) * 0.1 * dy
                z[i, j, k] = Z[k] + (0.5 - rnd.random()) * 0.1 * dz
    
    # Variables
    pressure = np.random.rand(ncells).reshape((nx, ny, nz))
    temp = np.random.rand(npoints).reshape((nx + 1, ny + 1, nz + 1))
    
    fname = os.path.join(outdir,'structured')
    gridToVTK(
        fname,
        x,
        y,
        z,
        cellData={"pressure": pressure},
        pointData={"temp": temp},
    )

    return 0

def vector_field():
    # directly copied from the pyevtk github examples: 
    # pyevtk/examples/structured.py, 
    # and then we modified this but now for vector data
    
    
    from pyevtk.hl import gridToVTK
    import numpy as np
    import random as rnd
    
    # Dimensions
    nx, ny, nz = 4, 9, 1
    lx, ly, lz = 1.0, 1.0, 1.0
    dx, dy, dz = lx / nx, ly / ny, lz / nz
    
    ncells = nx * ny * nz
    npoints = (nx + 1) * (ny + 1) * (nz + 1)
    
    # Coordinates
    X = np.arange(0, lx + 0.1 * dx, dx, dtype="float64")
    Y = np.arange(0, ly + 0.1 * dy, dy, dtype="float64")
    Z = np.arange(0, lz + 0.1 * dz, dz, dtype="float64")
    
    x = np.zeros((nx + 1, ny + 1, nz + 1))
    y = np.zeros((nx + 1, ny + 1, nz + 1))
    z = np.zeros((nx + 1, ny + 1, nz + 1))
    
    # We add some random fluctuation to make the grid
    # more interesting
    for k in range(nz + 1):
        for j in range(ny + 1):
            for i in range(nx + 1):
                x[i, j, k] = X[i] #+ (0.5 - rnd.random()) * 0.1 * dx
                y[i, j, k] = Y[j] #+ (0.5 - rnd.random()) * 0.1 * dy
                z[i, j, k] = Z[k] #+ (0.5 - rnd.random()) * 0.1 * dz
    
    # Variables
    pressure = np.random.rand(ncells).reshape((nx, ny, nz))
    temp = np.random.rand(npoints).reshape((nx + 1, ny + 1, nz + 1))
    
    fname = os.path.join(outdir,'vector')
    gridToVTK(
        fname,
        x,
        y,
        z,
        cellData={"pressure": pressure},
        pointData={"vel": (temp, -temp, temp)},
    )
    return 0
    