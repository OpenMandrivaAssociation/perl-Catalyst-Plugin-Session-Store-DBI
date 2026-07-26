%define	upstream_name	 Catalyst-Plugin-Session-Store-DBI
Name:		perl-%{upstream_name}
Version:	0.16
Release:	7

Summary:	Store your sessions in a database
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://dev.catalyst.perl.org/repos/Catalyst/Catalyst-Plugin-Session-Store-DBI
Source0:	https://cpan.metacpan.org/authors/id/F/FL/FLORA/Catalyst-Plugin-Session-Store-DBI-%{version}.tar.gz

BuildRequires:	make
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
%setup -q -n %{upstream_name}-%{version}

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

