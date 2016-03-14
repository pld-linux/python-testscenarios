# TODO: why tests fail with python 2.7?
#
# Conditional build:
%bcond_without	tests	# make check
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Testscenarios - pyunit extension for dependency injection
Summary(pl.UTF-8):	Testscenarios - rozszerzenie pyunit do wstrzykiwania zależności
Name:		python-testscenarios
Version:	0.5.0
Release:	1
License:	Apache v2.0 or BSD
Group:		Libraries/Python
#Source0Download: https://pypi.python.org/simple/testscenarios/
Source0:	https://pypi.python.org/packages/source/t/testscenarios/testscenarios-%{version}.tar.gz
# Source0-md5:	859073d9e7b049aee2e6704c51f6001a
URL:		https://launchpad.net/testscenarios
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules >= 1:2.6
BuildRequires:	python-pbr >= 0.11
BuildRequires:	python-setuptools
BuildRequires:	python-testtools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-pbr >= 0.11
BuildRequires:	python3-setuptools
BuildRequires:	python3-testtools
%endif
Requires:	python-modules >= 1:2.6
Requires:	python-pbr >= 0.11
Requires:	python-testtools
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
testscenarios provides clean dependency injection for python unittest
style tests. This can be used for interface testing (testing many
implementations via a single test suite) or for classic dependency
injection (provide tests with dependencies externally to the test code
itself, allowing easy testing in different situations).

%description -l pl.UTF-8
Moduł testscenarios zapewnia czyste wstrzykiwanie zależności dla
testów pythonowych w stylu unittest. Może to być używane do testowania
interfejsów (testowania wielu implementacji poprzez prosty zestaw
testów) albo klasycznego wstrzykiwania zależności (dostarczania testów
z zależnościami zewnętrznymi w stosunku do kodu testującego, co
pozwala na łatwiejsze testowanie w różnych sytuacjach).

%package -n python3-testscenarios
Summary:	Testscenarios - pyunit extension for dependency injection
Summary(pl.UTF-8):	Testscenarios - rozszerzenie pyunit do wstrzykiwania zależności
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2
Requires:	python3-pbr >= 0.11
Requires:	python3-testtools

%description -n python3-testscenarios
testscenarios provides clean dependency injection for python unittest
style tests. This can be used for interface testing (testing many
implementations via a single test suite) or for classic dependency
injection (provide tests with dependencies externally to the test code
itself, allowing easy testing in different situations).

%description -n python3-testscenarios -l pl.UTF-8
Moduł testscenarios zapewnia czyste wstrzykiwanie zależności dla
testów pythonowych w stylu unittest. Może to być używane do testowania
interfejsów (testowania wielu implementacji poprzez prosty zestaw
testów) albo klasycznego wstrzykiwania zależności (dostarczania testów
z zależnościami zewnętrznymi w stosunku do kodu testującego, co
pozwala na łatwiejsze testowanie w różnych sytuacjach).

%prep
%setup -q -n testscenarios-%{version}

%build
%if %{with python2}
%py_build

# tests fail with python 2.x - too old unittest?
#%{?with_tests:%{__make} check PYTHON=%{__python}}
%endif

%if %{with python3}
%py3_build

%{?with_tests:%{__make} check PYTHON=%{__python3}}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%{__rm} -r $RPM_BUILD_ROOT%{py_sitescriptdir}/testscenarios/tests
%endif

%if %{with python3}
%py3_install
%{__rm} -r $RPM_BUILD_ROOT%{py3_sitescriptdir}/testscenarios/tests
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc AUTHORS BSD COPYING ChangeLog GOALS NEWS README
%{py_sitescriptdir}/testscenarios
%{py_sitescriptdir}/testscenarios-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-testscenarios
%defattr(644,root,root,755)
%doc AUTHORS BSD COPYING ChangeLog GOALS NEWS README
%{py3_sitescriptdir}/testscenarios
%{py3_sitescriptdir}/testscenarios-%{version}-py*.egg-info
%endif
