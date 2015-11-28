%define 	module	pydot
Summary:	Python interface to Graphviz's Dot language
Summary(pl.UTF-8):	Pythonowy interfejs do języka Dot z pakietu Graphviz
Name:		python-%{module}
Version:	1.0.28
Release:	2
License:	MIT
Group:		Libraries/Python
Source0:	http://pydot.googlecode.com/files/pydot-%{version}.tar.gz
# Source0-md5:	c0a7a027176a62c412fd0f54951af692
URL:		http://code.google.com/p/pydot/
BuildRequires:	python-pyparsing >= 1.2
BuildRequires:	rpm-pythonprov
# if py_postclean is used
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-modules
Requires:	python-pyparsing >= 1.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pydot provides an interface for creating both directed and non
directed graphs from Python. Currently all attributes implemented in
the Dot language up to Graphviz 2.26.3 are supported.

%description -l pl.UTF-8
pydot udostępnia interfejs do tworzenia zarówno skierowanych jak i
nieskierowanych grafów z poziomu Pythona. Aktualnie obsługuje
wszystkie atrybuty zaimplementowane w języku dot do wersji Graphviza
2.26.3.

%prep
%setup -q -n %{module}-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install
%py_install
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
# %%doc ChangeLog LICENSE README
%{py_sitescriptdir}/*.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/pydot-*.egg-info
%endif
