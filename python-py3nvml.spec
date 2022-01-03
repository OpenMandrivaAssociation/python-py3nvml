%global srcname py3nvml

Name:           python-%{srcname}
Version:        0.2.7
Release:        1
Summary:        Python 3 Bindings for NVML library. Get NVIDIA GPU status inside your program.
Group:          System/Libraries
License:        BSD-3-Clause License
URL:            https://github.com/fbcotter/py3nvml
Source0:        https://files.pythonhosted.org/packages/source/p/py3nvml/py3nvml-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  pkgconfig(python)
BuildRequires:  python3dist(setuptools)
%{?python_provide:%python_provide python-%{srcname}}

%description
Python 3 compatible bindings to the NVIDIA Management Library. Can be used to query the state of the GPUs on your system. 
This was ported from the NVIDIA provided python bindings nvidia-ml-py, which only supported python 2. 
I have forked from version 7.352.0. The old library was itself a wrapper around the NVIDIA Management Library.

In addition to these NVIDIA functions to query the state of the GPU, 
I have written a couple functions/tools to help in using gpus (particularly for a shared gpu server). 
These are:
- A function to 'restrict' the available GPUs by setting the CUDA_VISIBLE_DEVICES environment variable.
- A script for displaying a differently formatted nvidia-smi.

%prep
%autosetup -p1

%build
%py_build

%install
%py_install


%files
%license LICENSE.txt
%doc CHANGELOG.rst README.rst
%{python_sitelib}/%{srcname}/
%{python_sitelib}/%{srcname}-%{version}-py%{python_version}.egg-info/
#{_bindir}/%{srcname}
