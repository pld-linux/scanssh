Summary:	SSH Version Scanner
Summary(pl):	Skaner Wersji SSH
Name:		scanssh
Version:	1.6b
Release:	1
License:	BSD
Group:		Networking	
Source0:	http://monkey.org/~provos/%{name}-%{version}.tar.gz
Patch0:		%{name}-ac_fixes.patch
URL:		http://monkey.org/~provos/scanssh/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libpcap-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Scanssh scans the given addresses and networks for running SSH
servers. It will query their version number and displays the results
in a list.

%description -l pl
Scanssh przeszukuje podane adres i sieci w poszukiwaniu uruchomionych
serwerów SSH, po czym odpytuje siê je o ich wersjê i wy¶wietla wyniki
w postaci listy.

%prep
%setup -q -n scanssh
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/scanssh
%{_mandir}/man1/scanssh.*
