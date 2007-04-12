%define snap r373875

%define _requires_exceptions perl(Apache2::Const)\\|perl(ModPerl::Config)
%define module	Apache-Test

Summary:	Test.pm wrapper with helpers for testing Apache
Name: 		perl-%{module}
Version: 	1.29
Release:	%mkrel 2
License:	GPL or Artistic
Group: 		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source0:	http://search.cpan.org/CPAN/authors/id/G/GE/GEOFF/%{module}-%{version}.tar.bz2
#Source0:	%{module}-%{version}-%{snap}.tar.bz2
Provides:	perl(Apache::TestConfigParse)
Provides:	perl(Apache::TestConfigPerl)
Requires:	perl-Compress-Zlib
Requires:	perl-Devel-Cover >= 0.48
BuildRequires:	perl-Devel-Cover >= 0.48
BuildRequires:	perl-devel
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Apache::Test is a test toolkit for testing an Apache server with
any configuration. It works with Apache 1.3 and Apache 2.0 and any
of its modules, including mod_perl 1.0 and 2.0. It was originally
developed for testing mod_perl 2.0.

%prep

%setup -q -n %{module}-%{version} 

for i in `find . -type d -name .svn`; do
    if [ -e "$i" ]; then rm -rf $i; fi >&/dev/null
done

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
%{_mandir}/*/*


