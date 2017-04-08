# aws_nexrad
This repository contains scripts scripts for downloading and processing  Level 2 NEXRAD data. The data are downloaded in archive 2 format (see https://www.roc.noaa.gov/wsr88d/PublicDocs/ICDs/2620010E.pdf for details) by interfacing with the AWS-NOAA NEXRAD s3 data service. Next, we convert the radar file to cfradial format using the RadxConvert utility from the RADX package (https://www.ral.ucar.edu/projects/titan/docs/radial_formats/radx.html). Finally, we can plot and work with the converted radar volume file by extracting data from each sweep.

We acheive this workflow with three scripts in this repository: `aws_nexrad.py` for downloading the radar data, `nexrad2netcdf` and the `RadxConvert` progmram for converting to netCDF, and `restructure_cfrad.py` for extracting the sweep information and plotting the data.

The NEXRAD site, date, and time are set in the 'aws_nexrad.py' script; by default the current time is used to find the most recent radar volume file on the s3 server.  Input to the 'nexrad2netcdf' script is given in the command line with simply the name of the downloaded radar file. Once the file is converted, 'nexrad2netcdf' automatically calls the 'restructure_cfrad.py' script with the filename input given via the command line in python with 'sys.argv[1]'. Thus, going through the default workflow is as follows:

'python aws_nexrad.py
nexrad2netcdf KCCX<date and time>'
