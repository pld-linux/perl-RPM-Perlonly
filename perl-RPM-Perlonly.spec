#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	RPM
%define	pnam	Perlonly
Summary:	RPM::Perlonly - a Perl only implementaion of a RPM header reader
Summary(pl):	RPM::Perlonly - czysto perlowa implementacja czytnika nag³ówków RPM
Name:		perl-RPM-Perlonly
Version:	1.0.1
Release:	2
License:	LGPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Perl-RPM-Perlonly is a clone of RPM::Header written in only Perl, so
it provides a way to read a rpm package on systems where rpm is not
installed. Perl-RPM-Perlonly can used as a drop in replacement for
RPM::Header, if needed also the other way round.

%description -l pl
Modu³ RPM-Perlonly to klon RPM::Header napisany w samym Perlu, przez
co pozwala odczytywaæ pakiety rpm na systemach bez zainstalowanego
rpm-a. RPM-Perlonly mo¿e byæ w razie potrzeby u¿ywany jako zamiennik
RPM::Header.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
