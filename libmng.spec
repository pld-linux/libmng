Summary:	A library of functions for manipulating MNG format files
Summary(pl):	Biblioteka do obrÛbki plikÛw w formacie MNG
Name:		libmng
Version:	1.0.3
Release:	2
License:	BSD-like
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	‚…¬Ã…œ‘≈À…
Group(uk):	‚¶¬Ã¶œ‘≈À…
Source0:	http://prdownloads.sourceforge.net/libmng/%{name}-%{version}.tar.gz
Patch0:		%{name}-automake.patch
URL:		http://www.libmng.com/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libjpeg-devel
BuildRequires:	libtool
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libmng - library for reading, writing, displaying and examing
Multiple-Image Network Graphics. MNG is the animation extension to the
popular PNG image-format.

%description -l pl
libmng - biblioteka do czytania, zapisywania, wy∂wietlania i
pobierania informacji z plikÛw MNG (Multiple-Image Network Graphics).
MNG to rozszerzenie o animacje popularnego formatu obrazkÛw PNG.

%package devel
Summary:	Development tools for programs to manipulate MNG format files
Summary(pl):	Pakiet do tworzenia programÛw obrabiaj±cych pliki MNG
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name} = %{version}
Requires:	libjpeg-devel
Requires:	zlib-devel

%description devel
The libmng-devel package contains the header files necessary for
developing programs using the MNG (Multiple-Image Network Graphics)
library.

If you want to develop programs which will manipulate MNG image format
files, you should install libmng-devel. You'll also need to install
the libmng package.

%description devel -l pl
Ten pakiet zawiera pliki nag≥Ûwkowe potrzebne do tworzenia programÛw
uøywaj±cych biblioteki libmng do obrÛbki plikÛw MNG.

%package static
Summary:	Static MNG libraries
Summary(pl):	Biblioteki statyczne MNG
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name}-devel = %{version}

%description static
Static MNG libraries.

%description static -l pl
Biblioteki statyczne MNG.

%prep
%setup -q
%patch -p1

%build
rm -f acinclude.m4 missing
libtoolize --copy --force
aclocal
autoconf
automake -a -c
%configure \
	--enable-shared \
	--enable-static \
	--with-zlib \
	--with-jpeg
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README* doc/{doc.readme,libmng.txt}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

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
