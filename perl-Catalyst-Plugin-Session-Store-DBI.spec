%define	upstream_name	 Catalyst-Plugin-Session-Store-DBI
%define upstream_version 0.16

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Store your sessions in a database
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/A/AG/AGRUNDMA//%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Catalyst) >= 5.49
BuildRequires:	perl(Catalyst::Plugin::Session) >= 0.05
BuildRequires:	perl(Class::Data::Inheritable)
BuildRequires:	perl(DBI)
BuildRequires:	perl(MIME::Base64)

BuildArch:	noarch

%description
This storage module will store session data in a database using DBI.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL installdirs=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes
%{_mandir}/man3/*
%{perl_vendorlib}/Catalyst

