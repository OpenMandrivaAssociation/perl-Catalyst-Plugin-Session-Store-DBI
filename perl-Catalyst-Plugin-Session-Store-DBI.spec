%define	module	Catalyst-Plugin-Session-Store-DBI
%define	name	perl-%{module}
%define version 0.13
%define release %mkrel 3

Summary:	Store your sessions in a database
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL or Artistic
Group:		Development/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/A/AG/AGRUNDMA//%{module}-%{version}.tar.gz
Url:		http://search.cpan.org/dist/%{module}
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
%{__perl} Makefile.PL installdirs=vendor
%make

%check
%__make test

%install
%{__rm} -rf %{buildroot}
%makeinstall_std

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/Catalyst

