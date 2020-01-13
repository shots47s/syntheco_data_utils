#!/bin/bash
#SBATCH -N 1
#SBATCH -p RM
#SBATCH -t 6:00:00
#SBATCH --ntasks-per-node=1

set -x 

cd $SCRATCH
source ~/sdmx/bin/activate

python read-sdmx-value.py Generic_98-313-XCB2011021.xml test.xml
