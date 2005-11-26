# TODO:
# - summary, desc,
%define 	module	pydot
Summary:	Python package with interface to Graphviz's Dot language 
Summary(pl):	Pakiet dla pytona
Name:		python-%{module}
Version:	0.9.10
Release:	0.1
License:	MIT
Group:		Libraries/Python
Source0:	http://dkbza.org/data/%{module}-%{version}.tar.gz
# Source0-md5:	d59609a3b69b19ad018c55d765945baf
URL:		http://dkbza.org/pydot.html
BuildRequires:	rpm-pythonprov
BuildRequires:	graphviz-devel
BuildRequires:	graphviz-python
BuildRequires:	python-pyparsing
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%description -l pl

%prep
%setup -q -n %{module}-%{version}


%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

#broken!
python setup.py install --optimize=2 --root=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT%{py_scriptdir} -type f -name "*.py" | xargs rm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{py_sitescriptdir}/*
