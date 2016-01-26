##### INSTALL

Run as sudo

```
apt-get install python-pythonmagick

pip install pyPdf

apt-get install libpq-dev python-dev

apt-get install libopencv-dev python-opencv

ln /dev/null /dev/raw1394 # disable warning message
```

##### USAGE

``python inspection.py -h``

``python inspection.py data/test/A.pdf data/test/A.pdf``

``python inspection.py --cases example --include Example1 data/test/A.pdf data/test/F.pdf``

``python inspection.py --cases example --include Example2 --exclude DefaultTest data/test/A.pdf data/test/F.pdf``

``python inspection.py --cases example --include Example3 --exclude DefaultTest --check any data/test/A.pdf data/test/F.pdf``



