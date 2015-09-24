#!/bin/sh

datadir=data
year=2014
short_year=14

mkdir -p $datadir
cd $datadir
curl -O http://www.bls.gov/tus/atususersguide.pdf
curl -O http://www.bls.gov/tus/atusintcodebk$short_year.pdf
curl -O http://www.bls.gov/tus/lexiconnoex$year.pdf
curl -O http://www.bls.gov/tus/special.requests/atussum_$year.zip
curl -O http://www.bls.gov/tus/special.requests/atusresp_$year.zip
curl -O http://www.bls.gov/tus/special.requests/atusrost_$year.zip
curl -O http://www.bls.gov/tus/special.requests/atusact_$year.zip
curl -O http://www.bls.gov/tus/special.requests/atuswho_$year.zip
curl -O http://www.bls.gov/tus/special.requests/atusrostec_$year.zip
curl -O http://www.bls.gov/tus/special.requests/atuscps_$year.zip

for f in *.zip; do
  unzip $f
done
