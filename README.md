##### Requirements 

Ubuntu >= 14.10 

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

``python inspection.py data/test/A.pdf data/test/B.pdf``

``python inspection.py --cases example --include Example1 data/test/A.pdf data/test/F.pdf``

``python inspection.py --cases example --include Example2 --exclude DefaultTest data/test/A.pdf data/test/F.pdf``

``python inspection.py --cases example --include Example3 --exclude DefaultTest --check any data/test/A.pdf data/test/F.pdf``

##### Algorithms

http://docs.opencv.org/2.4/modules/imgproc/doc/histograms.html?highlight=comparehist#comparehist

https://en.wikipedia.org/wiki/Longest_common_subsequence_problem

##### Python Modules

https://docs.python.org/2/library/unittest.html

##### Functionality Tests

``python -m unittest test``
