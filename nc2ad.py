#!/usr/bin/env python3

'''
Author: Marcos Conceição
    E-mail: marcosrdac@gmail.com
    GitHub: marcosrdac

This program exports a NetCDF4 data variable to a Fortran binary file.

Dependencies:
    Python libraries:
        numpy, scipy and netcdf4.
'''


import numpy as np
import netCDF4 as nc
from scipy.io import FortranFile as ff
from os import getcwd
from os.path import join, dirname, basename, splitext, isdir, isfile
from sys import argv


def print_help():
    '''
    Prints a help text.
    '''
    print('''
USAGE: nc2ad.py INPUT_FILE_PATH [-v VARIABLE] [-o OUTPUT_FILE_BASE_PATH]

Default output file path:
    {filedir}/{filename}_{variable}_{nrows}_{ncols}.ad

EXAMPLES:

    Interactive mode for variable selection (output file saved in myfiles):
        nc2ad.py myfiles/netcdf_file.nc

        The outputfile for this example would be at the following path:
            "myfiles/netcdf_file_{SELECTED_VARIABLE}_256_128.ad"

    Explicitly selecting variable "lat" (output file saved in myfiles):
        nc2ad.py myfiles/netcdf_file.nc lat

        The outputfile for this example would be at the following path:
            "myfiles/netcdf_file_lat_256_128.ad"

    Explicitly selecting variable "lat" and output file directory:
        nc2ad.py myfiles/netcdf_file.nc lat -o myotherfiles

        The outputfile for this example would be at the following path:
            "myotherfiles/netcdf_file_lat_256_128.ad"

    Explicitly selecting variable "lat" and output file base path:
        nc2ad.py myfiles/netcdf_file.nc lat -o myotherfiles/fotran_binary

        The outputfile for this example would be at the following path:
            "myotherfiles/fortran_binary_lat_256_128.ad"


            {filedir}/{filename}_{variable}_{nrows}_{ncols}.ad


    ''')

def choose_variable(ncf):
    '''
    Show all variables of an open NetCDF file.
    '''
    variables = list(ncf.variables.keys())
    print('Choose a variable to be converted:')
    for i, variable in enumerate(variables):
        print(f'\t{i+1}\t{variable}')
    variable_number = int(input('Variable number: '))-1
    variable = variables[variable_number]
    print()
    return(variable)


# defining array data type
dtype=np.float32


if __name__=='__main__':
    if '-h' in argv or '--help' in argv:
        print_help()
    else:

        # user definition
        try:
            infilepath = argv[1]
        except IndexError:
            print('Input file not given as agument! Use "nc2ad.py --help" for instructions.')
            exit()

        ncf = nc.Dataset(infilepath)

        if '-v' in argv or '--variable' in argv:
            try:
                variable = argv[argv.index('-v')+1]
            except ValueError:
                try:
                    variable = argv[argv.index('--variable')+1]
                except ValueError:
                    variable = argv[argv.index('--V')+1]
        else:
            variable = choose_variable(ncf)

    arr = ncf[variable]
    #arr = np.load('array.npy')

    # saving array
    nrows = arr.shape[0]
    ncols = arr.shape[1]

    if '-o' in  argv or '--output-basepath' in argv or '-O' in argv:
        try:
            outfilepath = argv[argv.index('-o')+1]
        except ValueError:
            try:
                outfilepath = argv[argv.index('--outdir')+1]
            except ValueError:
                outfilepath = argv[argv.index('-O')+1]

        if not isdir(outfilepath):
            outdir = dirname(outfilepath)
            outfilename = basename(outfilepath)
        else:
            outdir = outfilepath
            outfilename = splitext(basename(infilepath))[0]
    else:
        outdir = dirname(infilepath)
        outfilename = splitext(basename(infilepath))[0]

    outfilepath = join(outdir, f'{outfilename}_{variable}_{nrows}_{ncols}.ad')

    print(f'Saving output at: "{outfilepath}".', end='\n\n')
    openfile = ff(outfilepath, mode='w')
    openfile.write_record(arr)
    openfile.close()

    ## [ testing purposes only ]
    ## reopening array
    #openfile = ff(infilepath, mode='r')
    #arr = openfile.read_reals(dtype)
    #openfile.close()
    #print(arr)

    print('Done.')
