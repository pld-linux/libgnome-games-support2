#
# Conditional build:
%bcond_without	static_libs	# static library
#
Summary:	Support library for GNOME games
Summary(pl.UTF-8):	Biblioteka wspierająca dla gier GNOME
Name:		libgames-support
Version:	1.0
Release:	1
License:	LGPL v3+
Group:		X11/Libraries
Source0:	http://download.gnome.org/sources/libgames-support/1.0/%{name}-%{version}.tar.xz
# Source0-md5:	4504b352f4a91cfe152ef791fe939762
BuildRequires:	autoconf >= 2.69
BuildRequires:	automake >= 1:1.11
BuildRequires:	glib2-devel >= 1:2.40.0
BuildRequires:	gtk+3-devel >= 3.20.0
BuildRequires:	intltool >= 0.50.2
BuildRequires:	libgee-devel >= 0.8
BuildRequires:	libtool >= 2:2.2
BuildRequires:	pkgconfig
BuildRequires:	vala >= 2:0.24.0
Requires:	glib2 >= 1:2.40.0
Requires:	gtk+3 >= 3.20.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libgames-support is a small library intended for internal use by GNOME
Games, but it may be used by others. The API will only break with the
major version number. The ABI is unstable.

%description -l pl.UTF-8
libgames-support to mała biblioteka przeznaczona do użytku
wewnętrznego gier ze środowiska GNOME, ale może być wykorzystywana
także przez innych. API może się zmieniać tylko wraz z głównym numerem
wersji; ABI nie jest stabilne.

%package devel
Summary:	Header files for libgames-support library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libgames-support
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.40.0
Requires:	gtk+3-devel >= 3.20.0

%description devel
Header files for libgames-support library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libgames-support.

%package static
Summary:	Static libgames-support library
Summary(pl.UTF-8):	Statyczna biblioteka libgames-support
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libgames-support library.

%description static -l pl.UTF-8
Statyczna biblioteka libgames-support.

%package -n vala-libgames-support
Summary:	Vala API for libgames-support library
Summary(pl.UTF-8):	API języka Vala do bibliotek libgames-support
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description -n vala-libgames-support
Vala API for libgames-support library.

%description -n vala-libgames-support -l pl.UTF-8
API języka Vala do bibliotek libgames-support.

%prep
%setup -q

%build
%{__intltoolize}
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
%attr(755,root,root) %{_libdir}/libgames-support.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgames-support.so.2

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgames-support.so
%{_includedir}/gnome-games
%{_pkgconfigdir}/libgames-support-1.0.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libgames-support.a
%endif

%files -n vala-libgames-support
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/libgames-support-1.0.vapi
