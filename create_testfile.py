#!/usr/bin/env python


import numpy as np
import netCDF4 as nc

DTYPE = np.float32

# defining array
z_arr = np.arange(1,13, dtype=DTYPE).reshape(4,3)

rootgrp = nc.Dataset("testfile.nc", "w", format="NETCDF4")
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
