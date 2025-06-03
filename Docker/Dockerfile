FROM ubuntu:20.04

WORKDIR /root

RUN	apt-get update && apt install -y software-properties-common 


RUN add-apt-repository "deb http://security.ubuntu.com/ubuntu xenial-security main" &&\
    apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 3B4FE6ACC0B21F32 &&\
    apt update

ENV DEBIAN_FRONTEND=noninteractive 
RUN apt install -y tzdata
RUN apt install -y wget cmake build-essential


RUN apt-get update && apt-get install -y \
    libeigen3-dev \
    libopencv-dev \
    libopencv-contrib-dev \
    libgoogle-glog-dev \
    libatlas-base-dev \
    libgflags-dev \
    libsuitesparse-dev \
    qt5-default \
    pkg-config \
	git \
	wget \
	curl \
	tar \
	unzip \
	vim \
    libvtk7-dev \
    libvtk7-qt-dev \
    libgtk-3-dev 




WORKDIR /root
RUN apt -y purge cmake
RUN wget https://github.com/Kitware/CMake/releases/download/v3.16.0/cmake-3.16.0.tar.gz
RUN tar zxvf cmake-3.16.0.tar.gz
RUN cd cmake-3.16.0 && ./bootstrap && make && make install


# build ceres-solver
RUN git clone https://ceres-solver.googlesource.com/ceres-solver
# RUN wget http://ceres-solver.org/ceres-solver-2.2.0.tar.gz && tar zxf ceres-solver-2.2.0.tar.gz
WORKDIR /root/ceres-solver
RUN git checkout tags/2.1.0 && \
    mkdir build && \
	cd build && \
	cmake \
    -DCMAKE_BUILD_TYPE=Release .. && \
	make -j${NUM_THREADS} && \
	make install


WORKDIR /root