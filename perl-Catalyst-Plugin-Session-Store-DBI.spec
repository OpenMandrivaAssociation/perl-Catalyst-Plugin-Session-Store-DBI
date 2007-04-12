%define	module	Catalyst-Plugin-Session-Store-DBI
%define	name	perl-%{module}
%define version 0.07
%define release %mkrel 1

Summary:	Store your sessions in a database
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL or Artistic
Group:		Development/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/A/AG/AGRUNDMA//%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}
BuildRequires:	perl
BuildRequires:	perl(Catalyst) >= 5.49
BuildRequires:	perl(Catalyst::Plugin::Session) >= 0.05
BuildRequires:	perl(DBI)
BuildRequires:	perl(MIME::Base64)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This storage module will store session data in a database using DBI.


%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%check
./Build test

%install
%{__rm} -rf %{buildroot}
./Build install destdir=%buildroot

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/Catalyst

