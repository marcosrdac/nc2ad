# nc2ad

This program exports a NetCDF4 file variable to a Fortran binary file.


## Dependencies:

You need `Python 3+` and `pip 3+` in order to use this script.

| Python libraries needed |
| - |
| numpy |
| scipy |
| netcdf4 |

If your distribution still calls `python` as `python2`, instead of `python3` (you can tell that by sending `realpath $(which python)`), as debian and debian based distros do (Ubuntu and Linux Mint are examples), use `pip3` instead of `pip` to install these dependencies with:

Install them with:
```
pip install --user numpy scipy netcdf4
# or, if  python3 isn't default,
pip3 install --user numpy scipy netcdf4
```


## USAGE

```sh
./nc2ad.py INPUT_FILE_PATH [-v VARIABLE] [-o OUTPUT_FILE_BASE_PATH]
```

if nc2ad.py isn't executable, use
```sh
chmod +x nc2ad.py
```
before the first command.


### Default output file path:
```sh
{filedir}/{filename}_{variable}_{nrows}_{ncols}.ad
```


### Interactive mode for variable selection (output file saved in myfiles):
```sh
./nc2ad.py myfiles/netcdf_file.nc
```
The outputfile for this example would be at the following path:
```
myfiles/netcdf_file_SELECTEDVAR_256_128.ad
```


### Explicitly selecting variable "lat" (output file saved in myfiles):
```sh
./nc2ad.py myfiles/netcdf_file.nc lat
```
The outputfile for this example would be at the following path:
```
myfiles/netcdf_file_lat_256_128.ad
```


### Explicitly selecting variable "lat" and output file directory:
```sh
./nc2ad.py myfiles/netcdf_file.nc lat -o myotherfiles
```
The outputfile for this example would be at the following path:
```
myotherfiles/netcdf_file_lat_256_128.ad
```


### Explicitly selecting variable "lat" and output file base path:
```sh
./nc2ad.py myfiles/netcdf_file.nc lat -o myotherfiles/fotran_binary
```
The outputfile for this example would be at the following path:
```
myotherfiles/fortran_binary_lat_256_128.ad
```


## Testing

Create fake NetCDF data with:

```sh
python create_testfile.py
```
Now there is a testfile.nc NetCDF4 file inside the folder. Its variables are x, y and z.


Extract a variable to fortran binary (.ad) with:

```sh
./nc2ad testfile.py
```

See its values in Fortran with:
```sh
./testadopen.f90
```

Use `testadopen.f90` as a templates for oppening these .ad files.


## contact

  - *Name*: Marcos Conceição
  - *E-mail*: [marcosrdac@gmail.com](mailto:marcosrdac@gmail.com)
  - *GitHub*: [marcosrdac](github.com/marcosrdac)
  - *Website*: [marcosrdac.github.io](http://marcosrdac.github.io)
