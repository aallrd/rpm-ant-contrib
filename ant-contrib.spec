Name:           internal-ant-contrib
Version:        1.0b3
Release:        1%{?dist}
Summary:        The Ant-Contrib project is a collection of tasks for Apache Ant.
License:        Apache Software License
URL:            http://ant-contrib.sourceforge.net
Source0:        http://central.maven.org/maven2/ant-contrib/ant-contrib/%{version}/ant-contrib-%{version}.jar
Requires:       internal-ant >= 1.9.13
BuildRoot:      %{_tmppath}/%{name}-%{version}-buildroot
BuildArch:      noarch

# sysroot's configuration
#------------------------
%define _prefix         /opt/internal/root/opt
%define _exec_prefix    %{_prefix}
%define _antdir         %{_prefix}/ant
%define _libdir         %{_antdir}/lib
#------------------------

%description
The Ant-Contrib project is a collection of tasks for Apache Ant.

%prep
cp %{_sourcedir}/ant-contrib-%{version}.jar %{_builddir}


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_libdir}
# Copy the files in the targeted prefix
cp ant-contrib-%{version}.jar $RPM_BUILD_ROOT/%{_libdir}/ant-contrib.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-,root,root)

# Files to include
%{_libdir}/ant-contrib.jar

%changelog
* Thu Jan 17 2019 Antoine Allard <antoine.allard@internal.com>
- Create the RPM

