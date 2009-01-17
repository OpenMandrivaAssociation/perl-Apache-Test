%define _requires_exceptions perl(Apache2::Const)\\|perl(ModPerl::Config)
%define _provides_exceptions perl(HTTP::Request::Common)
%define module	Apache-Test

Summary:	Test.pm wrapper with helpers for testing Apache
Name: 		perl-%{module}
Version: 	1.31
Release:	%mkrel 2.735284.1
License:	GPL or Artistic
Group: 		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source0:	http://www.cpan.org/modules/by-module/Apache/%{module}.tar.gz
Provides:	perl(Apache::TestConfigParse)
Provides:	perl(Apache::TestConfigPerl)
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Apache::Test is a test toolkit for testing an Apache server with any
configuration. It works with Apache 1.3 and Apache 2.0 and any of its modules,
including mod_perl 1.0 and 2.0. It was originally developed for testing
mod_perl 2.0.

%prep

%setup -q -n %{module}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%install
rm -rf %{buildroot}

%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CONTRIBUTORS Changes INSTALL LICENSE README SUPPORT ToDo
%{perl_vendorlib}/Apache
%{perl_vendorlib}/Bundle
%{perl_vendorlib}/MyTest/Util.pm
%{_mandir}/*/*
