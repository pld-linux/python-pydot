%define 	module	pydot
Summary:	Python interface to Graphviz's Dot language 
Summary(pl.UTF-8):   Pythonowy interfejs do języka Dot z pakietu Graphviz
Name:		python-%{module}
Version:	0.9.10
Release:	0.1
License:	MIT
Group:		Libraries/Python
Source0:	http://dkbza.org/data/%{module}-%{version}.tar.gz
# Source0-md5:	d59609a3b69b19ad018c55d765945baf
URL:		http://dkbza.org/pydot.html
BuildRequires:	python-pyparsing >= 1.2
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
Requires:	python-pyparsing >= 1.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pydot provides an interface for creating both directed and non
directed graphs from Python. Currently all attributes implemented in
the Dot language up to Graphviz 1.16 are supported.

%description -l pl.UTF-8
pydot udostępnia interfejs do tworzenia zarówno skierowanych jak i
nieskierowanych grafów z poziomu Pythona. Aktualnie obsługuje
wszystkie atrybuty zaimplementowane w języku dot do wersji Graphviza
1.16.

%prep
%setup -q -n %{module}-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install --optimize=2 --root=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT%{py_scriptdir} -type f -name "*.py" | xargs rm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog LICENSE README
%{py_sitescriptdir}/*.py[co]
