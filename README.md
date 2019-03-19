# rpm-internal-ant-contrib

Build a RPM package for the **internal-ant-contrib** project.

## RPM build

```
$ docker run --rm -it --volume $(pwd):/specs --volume $(pwd):/output localhost:5000/aallrd/internal-build-rpm --build
[INFO] [14:32:47] RPM spec file: ant-contrib.spec
[...]
[SUCCESS] [14:32:54] Binary RPM file(s):
[SUCCESS] [14:32:54] * /root/rpmbuild/RPMS/noarch/internal-ant-contrib-1.0b3-1.el6.noarch.rpm
[SUCCESS] [14:32:54] Source RPM file(s):
[SUCCESS] [14:32:54] * /root/rpmbuild/SRPMS/internal-ant-contrib-1.0b3-1.el6.src.rpm
```

## RPM installation

### Using YUM

```
# Configure the vendor repo on the server
$ cat <<EOF >> /etc/yum.repos.d/vendors.repo

[vendor-internal]
name=internal
baseurl=http://localhost:4000/vendors/internal
enabled=1
gpgcheck=0
proxy=_none_
EOF

# Install the package using Yum
$ yum install -y --disablerepo=* --enablerepo=internal internal-ant-contrib
```

### Using RPM

```
$ wget http://localhost:4000/vendors/internal/internal-ant-contrib-1.0b3-1.el6.noarch.rpm
$ rpm -ivh internal-ant-contrib-1.0b3-1.el6.noarch.rpm
Preparing...            ########################################### [100%]
   1:internal-ant-contrib  ########################################### [100%]
```

## Usage

This package is an additional library for the **internal-ant** package.
