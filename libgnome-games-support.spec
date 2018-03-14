#
# Conditional build:
%bcond_without	static_libs	# static library

Summary:	Support library for GNOME games
Summary(pl.UTF-8):	Biblioteka wspierająca dla gier GNOME
Name:		libgnome-games-support
Version:	1.4.0
Release:	1
License:	LGPL v3+
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libgnome-games-support/1.4/%{name}-%{version}.tar.xz
# Source0-md5:	3cd6de98aa0e70c6c8b46a62efe5ba4c
BuildRequires:	autoconf >= 2.69
BuildRequires:	automake >= 1:1.11
BuildRequires:	gettext-tools >= 0.19.8
BuildRequires:	glib2-devel >= 1:2.40.0
BuildRequires:	gtk+3-devel >= 3.20.0
BuildRequires:	libgee-devel >= 0.8
BuildRequires:	libtool >= 2:2.2
BuildRequires:	pkgconfig
BuildRequires:	vala >= 2:0.40.0
Requires:	glib2 >= 1:2.40.0
Requires:	gtk+3 >= 3.20.0
Provides:	libgames-support = %{version}-%{release}
Obsoletes:	libgames-support < 1.2.0-1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libgnome-games-support is a small library intended for internal use by
GNOME Games, but it may be used by others. The API will only break
with the major version number. The ABI is unstable.

%description -l pl.UTF-8
libgnome-games-support to mała biblioteka przeznaczona do użytku
wewnętrznego gier ze środowiska GNOME, ale może być wykorzystywana
także przez innych. API może się zmieniać tylko wraz z głównym numerem
wersji; ABI nie jest stabilne.

%package devel
Summary:	Header files for libgnome-games-support library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libgnome-games-support
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.40.0
Requires:	gtk+3-devel >= 3.20.0
Provides:	libgames-support-devel = %{version}-%{release}
Obsoletes:	libgames-support-devel < 1.2.0-1

%description devel
Header files for libgnome-games-support library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libgnome-games-support.

%package static
Summary:	Static libgnome-games-support library
Summary(pl.UTF-8):	Statyczna biblioteka libgnome-games-support
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Provides:	libgames-support-static = %{version}-%{release}
Obsoletes:	libgames-support-static < 1.2.0-1

%description static
Static libgnome-games-support library.

%description static -l pl.UTF-8
Statyczna biblioteka libgnome-games-support.

%package -n vala-libgnome-games-support
Summary:	Vala API for libgnome-games-support library
Summary(pl.UTF-8):	API języka Vala do bibliotek libgnome-games-support
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Provides:	vala-libgames-support = %{version}-%{release}
Obsoletes:	vala-libgames-support < 1.2.0-1
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description -n vala-libgnome-games-support
Vala API for libgnome-games-support library.

%description -n vala-libgnome-games-support -l pl.UTF-8
API języka Vala do bibliotek libgnome-games-support.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules \
	%{?with_static_libs:--enable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS README
%attr(755,root,root) %{_libdir}/libgnome-games-support-1.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgnome-games-support-1.so.3

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgnome-games-support-1.so
%{_includedir}/gnome-games-support-1
%{_pkgconfigdir}/libgnome-games-support-1.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libgnome-games-support-1.a
%endif

%files -n vala-libgnome-games-support
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/libgnome-games-support-1.vapi
