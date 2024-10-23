%define upstream_name Apache-Test

Summary:	Test.pm wrapper with helpers for testing Apache
Name:		perl-%{upstream_name}
Version:	1.43
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/pod/Apache::Test
Source0:	https://www.cpan.org/modules/by-module/Apache/Apache-Test-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(Test)
BuildRequires:	perl-devel
Provides:	perl(Apache::TestConfigParse)
Provides:	perl(Apache::TestConfigPerl)

%description
Apache::Test is a test toolkit for testing an Apache server with any
configuration. It works with Apache 1.3 and Apache 2.0 and any of its modules,
including mod_perl 1.0 and 2.0. It was originally developed for testing
mod_perl 2.0.

%prep
%autosetup -p1 -n %{upstream_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make_build

%install
%make_install

%files
%doc CONTRIBUTORS Changes INSTALL LICENSE README SUPPORT ToDo
%{perl_vendorlib}/Apache
%{perl_vendorlib}/Bundle
%{_mandir}/man3/*
