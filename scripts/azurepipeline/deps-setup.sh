#!/bin/bash

# Install deps
sudo apt-get -qq update
sudo apt-get install -y git zip wget bzip2

#have to install g7zip 16.2 9.2 is too old install over alternative repo does not work.

wget https://mirrors.aliyun.com/oldubuntu-releases/ubuntu/pool/main/d/dpkg/dpkg-dev_1.17.13ubuntu1_all.deb
wget http://neurodebian.ovgu.de/debian/pool/main/p/p7zip/p7zip-full_16.02+dfsg-1~nd16.04+1_amd64.deb
wget http://neurodebian.ovgu.de/debian/pool/main/p/p7zip/p7zip_16.02+dfsg-1~nd16.04+1_amd64.deb
wget http://neurodebian.ovgu.de/debian/pool/main/n/neurodebian/neurodebian-popularity-contest_0.40.1~nd16.04+1_all.deb
wget http://archive.ubuntu.com/ubuntu/pool/main/p/popularity-contest/popularity-contest_1.64ubuntu2_all.deb

sudo dpkg -i --force-all dpkg-dev_1.17.13ubuntu1_all.deb
sudo dpkg -i popularity-contest_1.64ubuntu2_all.deb 
sudo dpkg -i neurodebian-popularity-contest_0.40.1~nd16.04+1_all.deb 
sudo dpkg -i p7zip_16.02+dfsg-1~nd16.04+1_amd64.deb
sudo dpkg -i p7zip-full_16.02+dfsg-1~nd16.04+1_amd64.deb
