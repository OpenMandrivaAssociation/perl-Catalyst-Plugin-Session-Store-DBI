%define	upstream_name	 Catalyst-Plugin-Session-Store-DBI
%define upstream_version 0.15

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Store your sessions in a database
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/A/AG/AGRUNDMA//%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(Catalyst) >= 5.49
BuildRequires:	perl(Catalyst::Plugin::Session) >= 0.05
BuildRequires:	perl(Class::Data::Inheritable)
BuildRequires:	perl(DBI)
BuildRequires:	perl(MIME::Base64)

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
This storage module will store session data in a database using DBI.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
%doc Changes
%{_mandir}/man3/*
%{perl_vendorlib}/Catalyst
