Summary:	Command line tool for PowerDNS and its MySQL backend 
Name:		zonemanip
Version:	0.1.4
Release:	%mkrel 8
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
