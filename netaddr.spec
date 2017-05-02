#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : netaddr
Version  : 0.7.19
Release  : 30
URL      : https://github.com/drkjam/netaddr/archive/netaddr-0.7.19.tar.gz
Source0  : https://github.com/drkjam/netaddr/archive/netaddr-0.7.19.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
Requires: netaddr-bin
Requires: netaddr-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
Patch1: 0001-Add-missing-PKG-INFO.patch

%description
netaddr
=======
A network address manipulation library for Python
[![Circle CI](https://circleci.com/gh/drkjam/netaddr.png?style=shield)](https://circleci.com/gh/drkjam/netaddr)
[![Latest Version](https://img.shields.io/pypi/v/netaddr.svg)](https://pypi.python.org/pypi/netaddr)
[![PyPI Downloads](https://img.shields.io/pypi/dm/netaddr.svg)](https://pypi.python.org/pypi/netaddr)

%package bin
Summary: bin components for the netaddr package.
Group: Binaries

%description bin
bin components for the netaddr package.


%package python
Summary: python components for the netaddr package.
Group: Default

%description python
python components for the netaddr package.


%prep
%setup -q -n netaddr-netaddr-0.7.19
%patch1 -p1

%build
export LANG=C
export SOURCE_DATE_EPOCH=1487260402
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1487260402
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/netaddr

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
