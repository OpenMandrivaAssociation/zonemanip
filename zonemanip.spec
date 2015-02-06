Summary:	Command line tool for PowerDNS and its MySQL backend 
Name:		zonemanip
Version:	0.1.4
Release:	9
License:	GPL
Group:		System/Servers
URL:		http://soren.overgaard.org/cgi-bin/index?t=stuff
Source0:	http://soren.overgaard.org/stuff/%{name}-%{version}.tar.bz2
Patch0:		zonemanip-0.1.4-shhopt_fix.diff
Requires:	pdns-backend-mysql
Requires:	libdbi-drivers-dbd-mysql
BuildRequires:	automake
BuildRequires:	libdbi-devel
BuildRequires:	libshhopt-devel
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
zonemanip is a command line tool for manipulating records in a
gmysql backend for PowerDNS. It supports delegating ownership of
specific zones to specific shell users by maintaining a minimal
amount of metadata. Currently, most record types except AAAA and
PTR records are supported. 

%prep

%setup -q 
%patch0 -p1

%build
rm -f configure
libtoolize --copy --force; aclocal; automake --add-missing --copy --foreign; autoconf

%configure2_5x

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc INSTALL TODO
%attr(4755,root,root) %{_bindir}/%{name}


%changelog
* Mon Jan 03 2011 Oden Eriksson <oeriksson@mandriva.com> 0.1.4-8mdv2011.0
+ Revision: 627843
- don't force the usage of automake1.7

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1.4-7mdv2011.0
+ Revision: 609664
- rebuilt against new libdbi

* Wed Sep 09 2009 Thierry Vignaud <tv@mandriva.org> 0.1.4-6mdv2010.0
+ Revision: 435405
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.1.4-5mdv2009.0
+ Revision: 243007
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed May 09 2007 Oden Eriksson <oeriksson@mandriva.com> 0.1.4-3mdv2008.0
+ Revision: 25477
- Import zonemanip



* Fri Apr 28 2006 Oden Eriksson <oeriksson@mandriva.com> 0.1.4-3mdk
- rebuild

* Fri Feb 04 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 0.1.4-2mdk
- rebuild

* Fri Jan 02 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.1.4-1mdk
- 0.1.4

* Mon Dec 29 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.1.3-1mdk
- 0.1.3

* Mon Oct 06 2003 Oden Eriksson <oden.eriksson@kvikkjokk.net> 0.1.1-1mdk
- initial cooker contrib
