# ToDo:
# - yes I know it breaks many things here, but that's why it has a release
#   lower than 1, some of those issues should be fixed in the next version
# - the commented out parts are for the next version, where hopefully they
#   will work
# - anyway - DO NOT TOUCH UNTIL TOLD TO DO SO, IT'S A MESS PRIVATE!
# - Dumbest Spec in History candidate!
#
%include	/usr/lib/rpm/macros.python

Summary:	Janosik - a free alternative for Platnik
Summary(pl):	Janosik - darmowa alternatywa dla Porgramu Platnika
Name:		janosik
Version:	0.0.2
Release:	0.2
License:	GPL
Group:		Applications
Source0:	http://www.nongnu.org/janosik/download/%{name}-%{version}.tar.gz
# Source0-md5:	14a7556b27fbf2c27728dc7850ad91a6
URL:		http://www.nongnu.org/janosik/
Requires:	python-pyRXP
Requires:	python-pygtk-glade
BuildRequires:	rpm-pythonprov
BuildRequires:	python >= 2.2.1
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/local

%description
Janosik is a multi-platform alternative for the Platnik program

%description -l pl
Janosik jest wieloplatformowym odpowiednikiem programu P³atnik, s³u¿±cym
do rozliczeñ z Zak³adem Ubezpieczeñ Spo³ecznych.

%prep
%setup -q -n %{name}-%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT
#install -d $RPM_BUILD_ROOT{%{_datadir}/%{name},%{_bindir},%{_libdir}}
#mv src/{import.py,janosik.py,jan-glade.py,eksport.py,weryfikacja.py} $RPM_BUILD_ROOT%{_bindir}
#mv src/*.py $RPM_BUILD_ROOT%{_libdir}
#mv src/* $RPM_BUILD_ROOT%{_datadir}/%{name}
install -d $RPM_BUILD_ROOT%{_prefix}/%{name}
cp -r * $RPM_BUILD_ROOT%{_prefix}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
#%%doc doc test ANNOUNCE CREDITS LICENCE README README.dom README.pyexpat README.sgmlop
#%attr(755,root,root) %{_bindir}/*
#%{_libdir}/*.py
#%dir %{_datadir}/%{name}
#%{_datadir}/%{name}/*
%dir %{_prefix}/%{name}
%{_prefix}/%{name}/*
%attr(755,root,root) %{_prefix}/%{name}/src/jan*.py
%attr(755,root,root) %{_prefix}/%{name}/src/*port.py
%attr(755,root,root) %{_prefix}/%{name}/src/weryfikacja.py
