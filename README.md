# aws_nexrad
This repository contains scripts scripts for downloading and processing  Level 2 NEXRAD data. The data are downloaded in archive 2 format (see https://www.roc.noaa.gov/wsr88d/PublicDocs/ICDs/2620010E.pdf for details) by interfacing with the AWS-NOAA NEXRAD s3 data service. Next, we convert the radar file to cfradial format using the RadxConvert utility from the RADX package (https://www.ral.ucar.edu/projects/titan/docs/radial_formats/radx.html). Finally, we can plot and work with the converted radar volume file by extracting data from each sweep.

# Installation
Download files into `aws_nexrad` directory with:
<pre><code>
mkdir aws_nexrad
cd aws_nexrad
git clone https://github.com/rskschrom/aws_nexrad.git
</pre></code>

The boto3 python package is required for this code to work. It can be installed with:

`easy_install --user boto3`

You will also need an account on Amazon Web Services that you can create for free at https://aws.amazon.com/?nc2=h_lg. For information about how to set up credentials for AWS see http://boto3.readthedocs.io/en/latest/guide/configuration.html. 

# Usage
Download NEXRAD data with the `aws_nexrad.py` script. Edit the `radsite` variable to change the NEXRAD site. Either leave the default date and time setting in the script to get the most recent radar volume scan, or uncomment and edit the date and time variables (lines 28-35). You don't need to know the exact time; the script will find the closest time of a radar volume in the archive. Once the appropriate site, date, and time variables are set run the script with:

`python aws_nexrad.py`

The included `nexrad2netcdf` uses the `RadxConvert` program to convert the Level 2 archive files to netCDF. You can alternatively use any other method for reading in or converting Level 2 NEXRAD data. The `restructure_cfrad.py` reads in the converted netCDF file and extracts sweep information and plots some of the data.

The `nexrad2netcdf` script runs with:

`./nexrad2netcdf <site><date_time>`

where `<site>` is the NEXRAD site (e.g., KCCX) and `<date_time> is in the format `YYYYMMDD_HHMNSS` (e.g., KCCX20130428_195312).
