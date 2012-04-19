%define upstream_name Apache-Test
%define upstream_version 1.37

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1
Summary:	Test.pm wrapper with helpers for testing Apache
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Apache/%{upstream_name}-%{upstream_version}.tar.gz
BuildArch:	noarch
Provides:	perl(Apache::TestConfigParse)
Provides:	perl(Apache::TestConfigPerl)

%description
Apache::Test is a test toolkit for testing an Apache server with any
configuration. It works with Apache 1.3 and Apache 2.0 and any of its modules,
including mod_perl 1.0 and 2.0. It was originally developed for testing
mod_perl 2.0.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%install

%makeinstall_std

%files
%doc CONTRIBUTORS Changes INSTALL LICENSE README SUPPORT ToDo
%{perl_vendorlib}/Apache
%{perl_vendorlib}/Bundle
%{_mandir}/*/*
