FROM centos:8

RUN yum install python36 -y
RUN pip3 install joblib && pip3 install scikit-learn

COPY 2nd.pk1 /
COPY mycode.py /

CMD python36 mycode.py