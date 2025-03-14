Summary:	Support library for GNOME games
Summary(pl.UTF-8):	Biblioteka wspierająca dla gier GNOME
Name:		libgnome-games-support2
Version:	2.0.1
Release:	1
License:	LGPL v3+
Group:		X11/Libraries
Source0:	https://download.gnome.org/sources/libgnome-games-support/2.0/libgnome-games-support-%{version}.tar.xz
# Source0-md5:	a613e4693ebeac275e8fee981394cdea
URL:		https://github.com/GNOME/libgnome-games-support
BuildRequires:	gettext-tools >= 0.19.8
BuildRequires:	glib2-devel >= 1:2.40.0
BuildRequires:	gtk4-devel >= 4.2.0
BuildRequires:	libgee-devel >= 0.14.0
BuildRequires:	meson >= 0.50.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 2.042
BuildRequires:	tar >= 1:1.22
BuildRequires:	vala >= 2:0.40.0
BuildRequires:	xz
Requires:	glib2 >= 1:2.40.0
Requires:	gtk4 >= 4.2.0
Requires:	libgee >= 0.14.0
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
Requires:	gtk4-devel >= 4.2.0
Requires:	libgee-devel >= 0.14.0

%description devel
Header files for libgnome-games-support library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libgnome-games-support.

%package -n vala-libgnome-games-support2
Summary:	Vala API for libgnome-games-support library
Summary(pl.UTF-8):	API języka Vala do bibliotek libgnome-games-support
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
BuildArch:	noarch

%description -n vala-libgnome-games-support2
Vala API for libgnome-games-support library.

%description -n vala-libgnome-games-support2 -l pl.UTF-8
API języka Vala do bibliotek libgnome-games-support.

%prep
%setup -q -n libgnome-games-support-%{version}

%build
# --default-library=both doesn't work with vala generated sources
# https://github.com/mesonbuild/meson/issues/6960
# We don't need static library currently, so don't bother to make it.
%meson \
	--default-library=shared

%meson_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install -C build

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS README
%attr(755,root,root) %{_libdir}/libgnome-games-support-2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgnome-games-support-2.so.4

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgnome-games-support-2.so
%{_includedir}/gnome-games-support-2
%{_pkgconfigdir}/libgnome-games-support-2.pc

%files -n vala-libgnome-games-support2
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/libgnome-games-support-2.vapi
