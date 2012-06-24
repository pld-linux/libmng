Summary:	A library of functions for manipulating MNG format files
Summary(pl):	Biblioteka do obr�bki plik�w w formacie MNG
Summary(uk):	��̦����� ����æ� ��� ������ � ������� � �����Ԧ MNG
Summary(ru):	���������� ������� ��� ������ � ������� � ������� MNG
Name:		libmng
Version:	1.0.5
Release:	1
License:	BSD-like
Group:		Libraries
Source0:	http://dl.sourceforge.net/libmng/%{name}-%{version}.tar.gz
# Source0-md5: e4f8f11231f01aa540a9b99251ab8bb6
Patch0:		%{name}-automake.patch
URL:		http://www.libmng.com/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	lcms-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libtool
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	libmng1

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
Requires:	%{name} = %{version}
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
Requires:	%{name}-devel = %{version}

%description static
Static MNG libraries.

%description static -l pl
Biblioteki statyczne MNG.

%description static -l ru
����������� ���������� ��� ������ � ������� � ������� MNG.

%description static -l uk
�������� ¦�̦����� ��� ������ � ������� � �����Ԧ MNG.

%prep
%setup -q
%patch0 -p1

%build
rm -f acinclude.m4 missing
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

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

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
%doc Changes README* doc/{doc.readme,libmng.txt}
%{_includedir}/*
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%{_libdir}/libmng.a
