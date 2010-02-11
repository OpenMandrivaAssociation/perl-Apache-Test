%define upstream_name    Apache-Test
%define upstream_version 1.31

%define _requires_exceptions perl(Apache2::Const)\\|perl(ModPerl::Config)
%define _provides_exceptions perl(HTTP::Request::Common)

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:	Test.pm wrapper with helpers for testing Apache
License:	GPL+ or Artistic
Group: 		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Apache/%{upstream_name}.tar.gz

BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}
Provides:	perl(Apache::TestConfigParse)
Provides:	perl(Apache::TestConfigPerl)

%description
Apache::Test is a test toolkit for testing an Apache server with any
configuration. It works with Apache 1.3 and Apache 2.0 and any of its modules,
including mod_perl 1.0 and 2.0. It was originally developed for testing
mod_perl 2.0.

%prep
%setup -q -n %{upstream_name}

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
