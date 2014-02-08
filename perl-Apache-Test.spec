%define upstream_name Apache-Test
%define upstream_version 1.37

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3
Summary:	Test.pm wrapper with helpers for testing Apache
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Apache/%{upstream_name}-%{upstream_version}.tar.gz
BuildArch:	noarch
Provides:	perl(Apache::TestConfigParse)
Provides:	perl(Apache::TestConfigPerl)
BuildRequires:	perl-devel

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


%changelog
* Thu Apr 19 2012 Oden Eriksson <oeriksson@mandriva.com> 1.370.0-1
+ Revision: 791919
- fix deps
- try to make it pass the anal rpmlint crap tests
- 1.37
- various fixes

* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.360.0-5
+ Revision: 765050
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1.360.0-4
+ Revision: 763474
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.360.0-3
+ Revision: 667024
- mass rebuild

* Mon Feb 28 2011 Funda Wang <fwang@mandriva.org> 1.360.0-2
+ Revision: 640741
- rebuild to obsolete old packages

* Thu Feb 03 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.360.0-1
+ Revision: 635491
- update to new version 1.36

* Mon Jan 24 2011 Oden Eriksson <oeriksson@mandriva.com> 1.350.0-1
+ Revision: 632474
- 1.35

* Fri Jan 21 2011 Oden Eriksson <oeriksson@mandriva.com> 1.350.0-0.0.rc1.1
+ Revision: 631990
- 1.35-rc1

* Tue Dec 14 2010 Oden Eriksson <oeriksson@mandriva.com> 1.340.0-0.0.rc1.1mdv2011.0
+ Revision: 621715
- 1.34-rc1

* Wed Sep 15 2010 Oden Eriksson <oeriksson@mandriva.com> 1.330.0-1mdv2011.0
+ Revision: 578481
- 1.33

* Fri Apr 16 2010 Oden Eriksson <oeriksson@mandriva.com> 1.320.0-1mdv2010.1
+ Revision: 535380
- 1.32

* Thu Feb 25 2010 Oden Eriksson <oeriksson@mandriva.com> 1.310.0-3mdv2010.1
+ Revision: 510956
- fix build
- 1.31 (final)

* Thu Feb 11 2010 Oden Eriksson <oeriksson@mandriva.com> 1.310.0-2mdv2010.1
+ Revision: 504134
- 1.31-rc2 (r908895)

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 1.310.0-1mdv2010.0
+ Revision: 402968
- rebuild using %%perl_convert_version

* Sun Jun 28 2009 Oden Eriksson <oeriksson@mandriva.com> 1.31-2.789147.1mdv2010.0
+ Revision: 390410
- new svn snap (r789147)

* Sat Jan 17 2009 Oden Eriksson <oeriksson@mandriva.com> 1.31-2.735284.1mdv2009.1
+ Revision: 330588
- new svn snap (r735284)

* Thu Aug 28 2008 Oden Eriksson <oeriksson@mandriva.com> 1.31-2.689836.1mdv2009.0
+ Revision: 276866
- new snap (r689836)

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 1.31-2.664495.1mdv2009.0
+ Revision: 265337
- rebuild early 2009.0 package (before pixel changes)

* Sun Jun 08 2008 Oden Eriksson <oeriksson@mandriva.com> 1.31-0.664495.1mdv2009.0
+ Revision: 216841
- new svn snap -r664495

* Sun May 04 2008 Oden Eriksson <oeriksson@mandriva.com> 1.31-0.653194.1mdv2009.0
+ Revision: 200955
- use a recent svn snapshot (r653194)
- use a recent svn snapshot (r653194)

* Tue Jan 15 2008 Oden Eriksson <oeriksson@mandriva.com> 1.30-2mdv2008.1
+ Revision: 152215
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Nov 27 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.30-1mdv2008.1
+ Revision: 113403
- new version
  drop useless depdendencies
  spec cleanup

* Sun Aug 12 2007 Pixel <pixel@mandriva.com> 1.29-3mdv2008.0
+ Revision: 62207
- don't wrongly provide perl(HTTP::Request::Common)


* Sun Mar 11 2007 Oden Eriksson <oeriksson@mandriva.com> 1.29-2mdv2007.1
+ Revision: 141321
- rebuild

* Tue Dec 12 2006 Oden Eriksson <oeriksson@mandriva.com> 1.29-1mdv2007.1
+ Revision: 95362
- 1.29
- rebuild
- Import perl-Apache-Test

* Sat Jun 03 2006 Oden Eriksson <oeriksson@mandriva.com> 1.28-2mdv2007.0
- don't run pointless tests, instead build apache, mod_perl 
  and sit back and watch

* Wed Feb 22 2006 Oden Eriksson <oeriksson@mandriva.com> 1.28-1mdk
- 1.28
- fix deps

* Tue Jan 31 2006 Oden Eriksson <oeriksson@mandriva.com> 1.28-0.r373875.1mdk
- use a recent snap (r373875)

* Wed Nov 02 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.27-1mdk
- 1.27

* Tue Oct 04 2005 Nicolas L�cureuil <neoclust@mandriva.org> 1.26-2mdk
- BuildRequires fix

* Wed Sep 28 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.26-1mdk
- New release 1.26
- spec cleanup
- better summary
- fix directory ownership
- enable tests

* Sun Jun 19 2005 Oden Eriksson <oeriksson@mandriva.com> 1.25-mdk2
- rule out some perl auto requires

* Sun Jun 19 2005 Oden Eriksson <oeriksson@mandriva.com> 1.25-1mdk
- 1.25

* Thu May 05 2005 Oden Eriksson <oeriksson@mandriva.com> 1.23-1mdk
- 1.23

* Wed Apr 20 2005 Oden Eriksson <oeriksson@mandriva.com> 1.22-1mdk
- 1.22
- use the %%mkrel macro

* Sat Jan 22 2005 Oden Eriksson <oden.eriksson@linux-mandrake.com> 1.20-1mdk
- 1.20
- drop upstream P0

* Sat Jan 15 2005 Oden Eriksson <oden.eriksson@linux-mandrake.com> 1.19-4mdk
- fix deps

* Sat Jan 15 2005 Oden Eriksson <oden.eriksson@linux-mandrake.com> 1.19-3mdk
- fix deps

* Thu Jan 13 2005 Oden Eriksson <oden.eriksson@linux-mandrake.com> 1.19-2mdk
- added P0 to nuke bad regexp (Stas Bekman)

* Wed Jan 12 2005 Oden Eriksson <oden.eriksson@linux-mandrake.com> 1.19-1mdk
- initial mandrake package

