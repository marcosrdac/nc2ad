# nc2ad

This program exports a NetCDF4 file variable to a Fortran binary file.


## Dependencies:

| Python libraries |
| - |
| numpy |
| scipy |
| netcdf4 |

Install them with

```
pip install numpy scipy netcdf4
```


## USAGE

USAGE: nc2ad.py INPUT_FILE_PATH [-v VARIABLE] [-o OUTPUT_FILE_BASE_PATH]

Default output file path:
    {filedir}/{filename}_{variable}_{nrows}_{ncols}.ad


# USAGE EXAMPLE


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


## contact

  Name: Marcos Conceição
  E-mail: marcosrdac@gmail.com
  GitHub: github/marcosrdac
  Website: marcosrdac.github.io
