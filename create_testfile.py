#!/usr/bin/env python


import numpy as np
import netCDF4 as nc

z_arr = np.random.random((3,4))
#y_arr, x_arr = np.mgrid[0:z_arr.shape[0], 0:z_arr.shape[1]]
#y_index = np.linspace(-3, 6, z_arr.shape[0])
#x_index = np.linspace(-4, 5, z_arr.shape[1])
#x_arr, y_arr = np.meshgrid(x_index, y_index)
#print(x_arr)
#print(y_arr)
#print(z_arr)

DTYPE = np.float32

rootgrp = nc.Dataset("test_array.nc", "w", format="NETCDF4")
rootgrp.description = "Test array."

rootgrp.createDimension("x", None)
rootgrp.createDimension("y", None)
x = rootgrp.createVariable("x", "f4", ("x"))
x.units = "m"
y = rootgrp.createVariable("y", "f4", ("y"))
y.units = "m"

z = rootgrp.createVariable("z", "f4", ("x", "y"))
z.units = "m"

x[:] = np.linspace(-4, 5, z_arr.shape[1])
y[:] = np.linspace(-3, 6, z_arr.shape[0])
z[:,:] = z_arr

rootgrp.close()
