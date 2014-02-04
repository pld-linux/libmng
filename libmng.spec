#
# Conditional build:
%bcond_without	gtk		# don't build GTK+-based contribs
%bcond_without	motif		# don't build Motif-based contribs
%bcond_without	sdl		# don't build SDL-based contribs
%bcond_without	static_libs	# don't build static libraries
#
Summary:	A library of functions for manipulating MNG format files
Summary(pl.UTF-8):	Biblioteka do obróbki plików w formacie MNG
Summary(uk.UTF-8):	Бібліотека функцій для роботи з файлами у форматі MNG
Summary(ru.UTF-8):	Библиотека функций для работы с файлами в формате MNG
Name:		libmng
Version:	2.0.2
Release:	1
License:	BSD-like
Group:		Libraries
Source0:	http://downloads.sourceforge.net/libmng/%{name}-%{version}.tar.xz
# Source0-md5:	3804bf2523af9b4e0670b5982b3bf984
Patch0:		%{name}-automake.patch
Patch1:		%{name}-gcc4.patch
Patch2:		%{name}-jpeg.patch
URL:		http://www.libmng.com/
BuildRequires:	autoconf >= 2.65
BuildRequires:	automake >= 1.3
BuildRequires:	lcms2-devel >= 2
BuildRequires:	libjpeg-devel
BuildRequires:	libtool
BuildRequires:	zlib-devel
# for contribs
%{?with_sdl:BuildRequires:	SDL-devel}
%{?with_gtk:BuildRequires:	gtk+2-devel >= 1:2.0.0}
%{?with_motif:BuildRequires:	motif-devel >= 2.0}
BuildRequires:	pkgconfig
%{?with_motif:BuildRequires:	xorg-lib-libXt-devel}
Obsoletes:	libmng1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libmng - library for reading, writing, displaying and examing
Multiple-Image Network Graphics. MNG is the animation extension to the
popular PNG image-format.

%description -l pl.UTF-8
libmng - biblioteka do czytania, zapisywania, wyświetlania i
pobierania informacji z plików MNG (Multiple-Image Network Graphics).
MNG to rozszerzenie o animacje popularnego formatu obrazków PNG.

%description -l ru.UTF-8
libmng - библиотека для чтения, записи, отображения и изучения
Multiple-Image Network Graphics. MNG - это анимационное расширение для
популярного формата изображений PNG.

%description -l uk.UTF-8
libmng - бібліотека для читання, запису, відображення та вивчення
Multiple-Image Network Graphics. MNG - це анімаційне розширення для
популярного формату зображень PNG.

%package devel
Summary:	Development tools for programs to manipulate MNG format files
Summary(pl.UTF-8):	Pakiet do tworzenia programów obrabiających pliki MNG
Summary(ru.UTF-8):	Средства разработки для программ, работающих с файлами в формате MNG
Summary(uk.UTF-8):	Засоби розробки для роботи з програмами, що працюють з файлами у форматі MNG
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	lcms2-devel >= 2
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

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe potrzebne do tworzenia programów
używających biblioteki libmng do obróbki plików MNG.

%description devel -l ru.UTF-8
Пакет libmng-devel содержит хедеры и библиотеки разработчика,
необходимые для разработки программ, использующих библиотеку MNG
(Multiple-Image Network Graphics).

%description devel -l uk.UTF-8
Пакет libmng-devel містить хедери та бібліотеки програміста, необхідні
для розробки програм, що використовують бібліотеку MNG (Multiple-Image
Network Graphics).

%package static
Summary:	Static MNG libraries
Summary(pl.UTF-8):	Biblioteki statyczne MNG
Summary(ru.UTF-8):	Статическая библиотека для работы с файлами в формате MNG
Summary(uk.UTF-8):	Статична бібліотека для роботи з файлами у форматі MNG
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static MNG libraries.

%description static -l pl.UTF-8
Biblioteki statyczne MNG.

%description static -l ru.UTF-8
Статическая библиотека для работы с файлами в формате MNG.

%description static -l uk.UTF-8
Статична бібліотека для роботи з файлами у форматі MNG.

%package progs
Summary:	libmng utilities (fbmngplay, mngtree)
Summary(pl.UTF-8):	Narzędzia do libmng (fbmngplay, mngtree)
Group:		Applications/Graphics
Requires:	%{name} = %{version}-%{release}

%description progs
libmng utilities that don't depend on additional libraries (fbmngplay,
mngtree).

%description progs -l pl.UTF-8
Narzędzia do libmng nie wymagające dodatkowych bibliotek (fbmngplay,
mngtree).

%package progs-gtk
Summary:	gmngview - GTK+-based MNG viewer
Summary(pl.UTF-8):	gmngview - przeglądarka plików MNG oparta na GTK+
Group:		X11/Applications/Graphics
Requires:	%{name} = %{version}-%{release}

%description progs-gtk
gmngview - GTK+-based MNG viewer.

%description progs-gtk -l pl.UTF-8
gmngview - przeglądarka plików MNG oparta na GTK+.

%package progs-motif
Summary:	xmngplay - X11/Motif-based MNG viewer
Summary(pl.UTF-8):	xmngplay - przeglądarka plików MNG oparta na bibliotekach X11/Motif
Group:		X11/Applications/Graphics
Requires:	%{name} = %{version}-%{release}

%description progs-motif
xmngplay - X11/Motif-based MNG viewer.

%description progs-motif -l pl.UTF-8
xmngplay - przeglądarka plików MNG oparta na bibliotekach X11/Motif.

%package progs-sdl
Summary:	mngplay - SDL-based MNG viewer
Summary(pl.UTF-8):	mngplay - przeglądarka plików MNG oparta na SDL
Group:		Applications/Graphics
Requires:	%{name} = %{version}-%{release}

%description progs-sdl
mngplay - SDL-based MNG viewer.

%description progs-sdl -l pl.UTF-8
mngplay - przeglądarka plików MNG oparta na SDL.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
cp makefiles/{Makefile.am,configure.ac} .
#sed -i '/AM_C_PROTOTYPES/d' configure.in
cp doc/makefiles/Makefile.am doc
cp doc/man/makefiles/Makefile.am doc/man
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-zlib \
	--with-jpeg \
	%{!?with_static_libs:--disable-static}
%{__make}

%{__make} -C contrib/gcc/fbmngplay fbmngplay \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -Wall -D_REENTRANT -I../../.." \
	LDFLAGS="%{rpmldflags} -L../../../.libs"

%if %{with gtk}
%{__make} -C contrib/gcc/gtk-mng-view gmngview \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -Wall -I../../.. `pkg-config --cflags gdk-pixbuf-2.0 gtk+-2.0`" \
	LIBS="%{rpmldflags} -L../../../.libs -lmng -lz `pkg-config --libs gdk-pixbuf-2.0 gtk+-2.0`"
%endif

%{__make} -C contrib/gcc/mngtree -f makefile.linux \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -Wall -DMNG_USE_SO -I../../.." \
	LDFLAGS="%{rpmldflags} -L../../../.libs -lmng"

%if %{with sdl}
%{__cc} -o contrib/gcc/sdl-mngplay/mngplay contrib/gcc/sdl-mngplay/mngplay.c \
	%{rpmldflags} %{rpmcflags} -I. \
	 -L.libs -lmng `sdl-config --libs` -lz
%endif

%if %{with motif}
%{__make} -C contrib/gcc/xmngview compile \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -Wall -I../../.." \
	LIBS="-L../../../.libs -lmng -lXm -lXt -lX11 -lXext"
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install contrib/gcc/*/{fbmngplay%{?with_gtk:,gmngview},mngtree%{?with_sdl:,mngplay}%{?with_motif:,xmngview}} \
	$RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGES LICENSE README
%attr(755,root,root) %{_libdir}/libmng.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmng.so.2
%{_mandir}/man5/jng.5*
%{_mandir}/man5/mng.5*

%files devel
%defattr(644,root,root,755)
%doc doc/{doc.readme,libmng.txt,Plan*.png}
%attr(755,root,root) %{_libdir}/libmng.so
%{_libdir}/libmng.la
%{_includedir}/libmng*.h
%{_pkgconfigdir}/libmng.pc
%{_mandir}/man3/libmng.3*

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libmng.a
%endif

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/fbmngplay
%attr(755,root,root) %{_bindir}/mngtree

%if %{with gtk}
%files progs-gtk
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gmngview
%endif

%if %{with motif}
%files progs-motif
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xmngview
%endif

%if %{with sdl}
%files progs-sdl
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mngplay
%endif
