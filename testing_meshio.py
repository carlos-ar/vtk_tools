#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 10:32:20 2020

@author: carlosar
"""
import meshio
import numpy

def mesh(mesh_type='tri'):
    """Creates template meshes from meshio helpers module
    
    The following meshes are from the meshio tests
    
    
    Args:
        mesh_type: the type of mesh you wish to use, only tri, quad, and hex
          are currently available
    
    Returns:
        points: A numpy array of shape number of points, and x, y (and z) point
          locations
          points -> np.array( (n_points, xyz_points) )
        cells: A list with a tuple of mesh type and numpy array with cell node
          locations.
          cells- > list('type', np.array( n_cells, nodes ) )
    """
    if mesh_type == 'tri':
        points = numpy.array([
                [0.0, 0.0, 0.0],
                [0.0, 1.0, 0.0],
                [0.0, 0.0, 1.0],
                ])
        cells = [
                ("triangle", numpy.array([[0, 1, 2]]))
            ]
    elif mesh_type == 'quad':
        points = numpy.array(
            [
                [0.0, 0.0, 0.0],
                [1.0, 0.0, 0.0],
                [2.0, 0.0, 0.0],
                [2.0, 1.0, 0.0],
                [1.0, 1.0, 0.0],
                [0.0, 1.0, 0.0],
            ]
        )/3.0
        cells = [("quad", numpy.array([[0, 1, 4, 5], [1, 2, 3, 4]]))]
    elif mesh_type == 'hex':
        points = numpy.array(
            [
                [0.0, 0.0, 0.0],
                [1.0, 0.0, 0.0],
                [1.0, 1.0, 0.0],
                [0.0, 1.0, 0.0],
                [0.0, 0.0, 1.0],
                [1.0, 0.0, 1.0],
                [1.0, 1.0, 1.0],
                [0.0, 1.0, 1.0],
            ]
        )
        cells = [("hexahedron", numpy.array([[0, 1, 2, 3, 4, 5, 6, 7]]))]
    return points, cells

def write_vtk_file(filename, points, cells, data):
    """Writes single vtk mesh file
    
    Args:
        filename: 
    """
    filename = filename+'.vtk'
    meshio.write_points_cells(
        filename,
        points,
        cells,
        # Optionally provide extra data on points, cells, etc.
        point_data={"vel": data},
        # cell_data=cell_data,
        # field_data=field_data
        )
    
def write_xdmf(filename, points, cells, data):
    filename = filename+'.xmf'
    with meshio.xdmf.TimeSeriesWriter(filename) as writer:
        writer.write_points_cells(points, cells)
        for t in [0.0, 0.1, 0.21]:
            writer.write_data(t, point_data={"vel": data})
            

    
def make_mesh(mesh_type):
    """Creates mesh types in meshio I/O format
    
    From
    
    Args:
        mesh_type:
    
    Returns:
        points: A numpy array of shape number of points, and x, y (and z) point
          locations
          points -> np.array( (n_points, xyz_points) )
        cells: A list with a tuple of mesh type and numpy array with cell node
          locations.
          cells- > list('type', np.array( n_cells, nodes ) )
  """
    nx = 4; ny =  4
    x0 = -2; xn = 1
    y0 = -3; yn = 2
    x = numpy.linspace(x0,xn,nx)
    y = numpy.linspace(y0,yn,ny)
    if mesh_type == 'hex':
        nz = 4;
        z0 = -0.25; zn = 1.2
        z = numpy.linspace(z0,zn,nz)
        xv, yv, zv = numpy.meshgrid(x, y, z, indexing='ij')
    
        points = numpy.array([numpy.ravel(xv), numpy.ravel(yv), numpy.ravel(zv)]).T
        num_cells = (nx-1)*(ny-1)*(nz-1)
        
        hex_cells = 8
        
        cells = numpy.zeros((num_cells, hex_cells))
        
        n_cell = 0
        for k in range(0, nz-1):
            for j in range(0, ny-1):
                for i in range(0,nx-1):

                    cells[n_cell,0] = nz*ny*(i)   + nz*(j)   + (k)
                    cells[n_cell,1] = nz*ny*(i)   + nz*(j)   + (k+1)
                    cells[n_cell,2] = nz*ny*(i)   + nz*(j+1) + (k+1)
                    cells[n_cell,3] = nz*ny*(i)   + nz*(j+1) + (k)
                    cells[n_cell,4] = nz*ny*(i+1) + nz*(j)   + (k)
                    cells[n_cell,5] = nz*ny*(i+1) + nz*(j)   + (k+1)
                    cells[n_cell,6] = nz*ny*(i+1) + nz*(j+1) + (k+1)
                    cells[n_cell,7] = nz*ny*(i+1) + nz*(j+1) + (k)
                        
                    n_cell+=1
        cells_out = [("hexahedron", cells)] 

    elif mesh_type == 'quad':
        xv, yv = numpy.meshgrid(x, y, indexing='ij')
        
        points = numpy.array([numpy.ravel(xv), numpy.ravel(yv)]).T
        num_cells = (nx-1)*(ny-1)
        
        quad_cells = 4
        
        cells = numpy.zeros((num_cells, quad_cells))
        
        n_cell = 0
        for j in range(0, ny-1):
            for i in range(0,nx-1):            
                cells[n_cell,0] = ny*(i)   + (j)
                cells[n_cell,1] = ny*(i)   + (j+1)
                cells[n_cell,2] = ny*(i+1) + (j+1)
                cells[n_cell,3] = ny*(i+1) + (j)
                    
                n_cell+=1

        cells_out = [("quad", cells)] 
    elif mesh_type == 'tri':
        points, cells_out = mesh(mesh_type)
    else:
        print('mesh not supported!')
        
        
    return points, cells_out

def vel_func(x,y,z, constant=False):
    """Creates arbritary velocity field
    
    Args:
        filename: 
    """
    if constant == True:
        u = 2;v=1;w=0
    else:
        u,v,w = tuple(2.0*numpy.random.rand(3))
    return u,v,w

def make_vector_data(points):
    point_shape = numpy.shape(points)
    num_points = point_shape[0]
    vel = numpy.zeros((num_points, 3))
    print(point_shape)
    if point_shape[1] == 3:
        x = points[:,0]; y = points[:,1]; z = points[:,2]
    else:
        x = points[:,0]; y = points[:,1]; z = numpy.zeros(numpy.shape(y))
        
    for n in range(0, num_points):
        u,v,w = vel_func(x[n],y[n],z[n])
        vel[n,0] = u
        vel[n,1] = v
        vel[n,2] = w
    
    return vel

