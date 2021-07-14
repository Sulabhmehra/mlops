from centos:8

run yum install python3 -y
run pip3 install scikit-learn
run pip3 install pandas

copy marks.py /
copy zz.z1 /

cmd python3 zz.z1