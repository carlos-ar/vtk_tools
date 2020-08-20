# -*- coding: utf-8 -*-
"""
This file writes an xdmf file using meshio, but re-writes the atrribute name
"Name" to the "Grid" tag in the "Grid" collection
"""
import os
import meshio
import numpy as np
from xml.etree import ElementTree as ET
from meshio._common import write_xml


def write_xdmf(filename, time, points, cells, data, bug=False):
    """
    """
    filename = filename+'.xmf'
    with meshio.xdmf.TimeSeriesWriter(filename) as writer:
        writer.write_points_cells(points, cells)
        for t in time:
            
            writer.write_data(t, point_data={"vel": data})
            
    if bug == False:
        grids = writer.collection.findall("Grid")
        for g in grids:
            g.set("Name","mesh_name")
        writer.collection.set("Name","MeshIO bug")
        write_xml(writer.filename, writer.xdmf_file)
            # ET.SubElement(grid, "Grid", Name="mesh")

            
time_array = [0.0, 0.1, 0.21]
points = np.array(
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
cells = [("hexahedron", np.array([[0, 1, 2, 3, 4, 5, 6, 7]]))]
ps = np.shape(points)
data = np.random.rand(ps[0],ps[1])

write_xdmf('visit_mesh', time_array, points, cells, data)