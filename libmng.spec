#
# Conditional build:
%bcond_without	sdl	# don't build SDL-based contribs
#
Summary:	A library of functions for manipulating MNG format files
Summary(pl):	Biblioteka do obr�bki plik�w w formacie MNG
Summary(uk):	��̦����� ����æ� ��� ������ � ������� � �����Ԧ MNG
Summary(ru):	���������� ������� ��� ������ � ������� � ������� MNG
Name:		libmng
Version:	1.0.8
Release:	1
License:	BSD-like
Group:		Libraries
Source0:	http://dl.sourceforge.net/libmng/%{name}-%{version}.tar.gz
# Source0-md5:	d688ca879c934e9cde8b323cf3025f89
Patch0:		%{name}-automake.patch
URL:		http://www.libmng.com/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	lcms-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libtool
BuildRequires:	zlib-devel
# for contribs
%{?with_sdl:BuildRequires:	SDL-devel}
BuildRequires:	gtk+2-devel >= 1:2.0.0
BuildRequires:	motif-devel >= 2.0
Obsoletes:	libmng1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libmng - library for reading, writing, displaying and examing
Multiple-Image Network Graphics. MNG is the animation extension to the
popular PNG image-format.

%description -l pl
libmng - biblioteka do czytania, zapisywania, wy�wietlania i
pobierania informacji z plik�w MNG (Multiple-Image Network Graphics).
MNG to rozszerzenie o animacje popularnego formatu obrazk�w PNG.

%description -l ru
libmng - ���������� ��� ������, ������, ����������� � ��������
Multiple-Image Network Graphics. MNG - ��� ������������ ���������� ���
����������� ������� ����������� PNG.

%description -l uk
libmng - ¦�̦����� ��� �������, ������, צ���������� �� ��������
Multiple-Image Network Graphics. MNG - �� �Φ��æ��� ���������� ���
����������� ������� ��������� PNG.

%package devel
Summary:	Development tools for programs to manipulate MNG format files
Summary(pl):	Pakiet do tworzenia program�w obrabiaj�cych pliki MNG
Summary(ru):	�������� ���������� ��� ��������, ���������� � ������� � ������� MNG
Summary(uk):	������ �������� ��� ������ � ����������, �� �������� � ������� � �����Ԧ MNG
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	lcms-devel
Requires:	libjpeg-devel
Requires:	zlib-devel
Obsoletes:	libmng1-devel

%description devel
The libmng-devel package contains the header files necessary for
developing programs using the MNG (Multiple-Image Network Graphics)
library.

If you want to develop programs which will manipulate MNG image format
files, you should install libmng-devel. You'll also need to install
the libmng package.

%description devel -l pl
Ten pakiet zawiera pliki nag��wkowe potrzebne do tworzenia program�w
u�ywaj�cych biblioteki libmng do obr�bki plik�w MNG.

%description devel -l ru
����� libmng-devel �������� ������ � ���������� ������������,
����������� ��� ���������� ��������, ������������ ���������� MNG
(Multiple-Image Network Graphics).

%description devel -l uk
����� libmng-devel ͦ����� ������ �� ¦�̦����� ������ͦ���, ����Ȧ�Φ
��� �������� �������, �� �������������� ¦�̦����� MNG (Multiple-Image
Network Graphics).

%package static
Summary:	Static MNG libraries
Summary(pl):	Biblioteki statyczne MNG
Summary(ru):	����������� ���������� ��� ������ � ������� � ������� MNG
Summary(uk):	�������� ¦�̦����� ��� ������ � ������� � �����Ԧ MNG
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static MNG libraries.

%description static -l pl
Biblioteki statyczne MNG.

%description static -l ru
����������� ���������� ��� ������ � ������� � ������� MNG.

%description static -l uk
�������� ¦�̦����� ��� ������ � ������� � �����Ԧ MNG.

%package progs
Summary:	libmng utilities (fbmngplay, mngtree)
Summary(pl):	Narz�dzia do libmng (fbmngplay, mngtree)
Group:		Applications/Graphics
Requires:	%{name} = %{version}-%{release}

%description progs
libmng utilities that don't depend on additional libraries (fbmngplay,
mngtree).

%description progs -l pl
Narz�dzia do libmng nie wymagaj�ce dodatkowych bibliotek (fbmngplay,
mngtree).

%package progs-gtk
Summary:	gmngview - GTK+-based MNG viewer
Summary(pl):	gmngview - przegl�darka plik�w MNG oparta na GTK+
Group:		X11/Applications/Graphics
Requires:	%{name} = %{version}-%{release}

%description progs-gtk
gmngview - GTK+-based MNG viewer.

%description progs-gtk -l pl
gmngview - przegl�darka plik�w MNG oparta na GTK+.

%package progs-motif
Summary:	xmngplay - X11/Motif-based MNG viewer
Summary(pl):	xmngplay - przegl�darka plik�w MNG oparta na bibliotekach X11/Motif
Group:		X11/Applications/Graphics
Requires:	%{name} = %{version}-%{release}

%description progs-motif
xmngplay - X11/Motif-based MNG viewer.

%description progs-motif -l pl
xmngplay - przegl�darka plik�w MNG oparta na bibliotekach X11/Motif.

%package progs-sdl
Summary:	mngplay - SDL-based MNG viewer
Summary(pl):	mngplay - przegl�darka plik�w MNG oparta na SDL
Group:		Applications/Graphics
Requires:	%{name} = %{version}-%{release}

%description progs-sdl
mngplay - SDL-based MNG viewer.

%description progs-sdl -l pl
mngplay - przegl�darka plik�w MNG oparta na SDL.

%prep
%setup -q
%patch0 -p1

%build
cp makefiles/{Makefile.am,configure.in} .
cp doc/makefiles/Makefile.am doc
cp doc/man/makefiles/Makefile.am doc/man
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-shared \
	--enable-static \
	--with-zlib \
	--with-jpeg
%{__make}

%{__make} -C contrib/gcc/fbmngplay fbmngplay \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -Wall -D_REENTRANT -I../../.." \
	LDFLAGS="%{rpmldflags} -L../../../.libs"

%{__make} -C contrib/gcc/gtk-mng-view gmngview \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -Wall -I../../.. `pkg-config --cflags gdk-pixbuf-2.0 gtk+-2.0`" \
	LIBS="%{rpmldflags} -L../../../.libs -lmng `pkg-config --libs gdk-pixbuf-2.0 gtk+-2.0`"

%{__make} -C contrib/gcc/mngtree -f makefile.linux \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -Wall -DMNG_USE_SO -I../../.." \
	LDFLAGS="%{rpmldflags} -L../../../.libs -lmng"

%if %{with sdl}
%{__cc} -o contrib/gcc/sdl-mngplay/mngplay contrib/gcc/sdl-mngplay/mngplay.c \
	%{rpmldflags} %{rpmcflags} -I. \
	 -L.libs -lmng `sdl-config --libs`
%endif

%{__make} -C contrib/gcc/xmngview compile \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -Wall -I../../.. -I/usr/X11R6/include" \
	LIBS="-L../../../.libs -lmng -L/usr/X11R6/%{_lib} -lXm -lXt -lX11"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install contrib/gcc/*/{fbmngplay,gmngview,mngtree%{?with_sdl:,mngplay},xmngview} \
	$RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGES LICENSE README 
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_mandir}/man5/*

%files devel
%defattr(644,root,root,755)
%doc doc/{doc.readme,libmng.txt,Plan*.png}
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%{_libdir}/libmng.a

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/fbmngplay
%attr(755,root,root) %{_bindir}/mngtree

%files progs-gtk
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gmngview

%files progs-motif
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xmngview

%if %{with sdl}
%files progs-sdl
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mngplay
%endif
