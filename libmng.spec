Summary:	A library of functions for manipulating MNG format files
Name:		libmng
Version:	0.9.2
Release:	1
License:	AS IS
Group:		Libraries
Group(pl):	Biblioteki
Group(fr):	Librairies
Source0:	ftp://download.sourceforge.net/pub/sourceforge/libmng/%{name}-%{version}.tar.gz
Patch0:		libmng-automake.patch
URL:		http://www.libmng.com/
BuildPrereq:	automake
BuildPrereq:	autoconf
BuildPrereq:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libmng - library for reading, writing, displaying and examing
Multiple-Image Network Graphics. MNG is the animation extension to the
popular PNG image-format.

%package devel
Summary:	Development tools for programs to manipulate MNG format files
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Group(fr):	Development/Librairies
Requires:	%{name} = %{version}

%description devel
The libmng-devel package contains the header files and static
libraries necessary for developing programs using the MNG
(Multiple-Image Network Graphics) library.

If you want to develop programs which will manipulate MNG image format
files, you should install libmng-devel. You'll also need to install
the libmng package.

%package static
Summary:	Static MNG libraries
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Group(fr):	Development/Librairies
Requires:	%{name}-devel = %{version}

%description static
Static MNG libraries.

%prep
%setup -q
%patch -p1

%build
aclocal
automake
autoconf
LDFLAGS="-s"; export LDFLAGS
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/lib*.so.*.*

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man*/* \
	CHANGES README* doc/{doc.readme,libmng.txt}

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_mandir}/man5/*

%files devel
%defattr(644,root,root,755)
%doc *.gz doc/*.gz
%{_includedir}/*
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%{_libdir}/libmng.a
