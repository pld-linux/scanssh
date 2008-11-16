Summary:	SSH Version Scanner
Summary(pl.UTF-8):	Skaner Wersji SSH
Name:		scanssh
Version:	2.1
Release:	2
License:	BSD
Group:		Networking
Source0:	http://monkey.org/~provos/%{name}-%{version}.tar.gz
# Source0-md5:	9fab4253b56b2d15367d4872b370cdcb
Patch0:		%{name}-ac_fixes.patch
URL:		http://monkey.org/~provos/scanssh/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	libdnet-devel
BuildRequires:	libevent-devel
BuildRequires:	libpcap-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Scanssh scans the given addresses and networks for running SSH
servers. It will query their version number and displays the results
in a list.

%description -l pl.UTF-8
Scanssh przeszukuje podane adresy i sieci w poszukiwaniu uruchomionych
serwerów SSH, po czym odpytuje się je o ich wersję i wyświetla wyniki
w postaci listy.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/scanssh
%{_mandir}/man1/scanssh.*
