Summary:	Support library for GNOME games
Name:		libgames-support
Version:	0.1
Release:	1
License:	LGPL v3+
Group:		X11/Libraries
Source0:	http://download.gnome.org/sources/libgames-support/0.1/%{name}-%{version}.tar.xz
# Source0-md5:	741a504dd001450473045079d63ada9c
BuildRequires:	autoconf >= 2.69
BuildRequires:	automake >= 1:1.11
BuildRequires:	glib2-devel >= 1:2.40.0
BuildRequires:	gtk+3-devel >= 3.12.0
BuildRequires:	intltool >= 0.50.2
BuildRequires:	libgee-devel
BuildRequires:	libtool >= 2:2.2
BuildRequires:	pkgconfig
BuildRequires:	vala >= 2:0.24.0
Requires:	glib2 >= 1:2.40.0
Requires:	gtk+3 >= 3.12.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libgames-support is a small library intended for internal use by GNOME
Games, but it may be used by others. The API will only break with the
major version number. The ABI is unstable.

%package devel
Summary:	Header files for libgames-support library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libgames-support
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.40.0
Requires:	gtk+3-devel >= 3.12.0

%description devel
Header files for libgames-support library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libgames-support.

%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -f $RPM_BUILD_ROOT%{_libdir}/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS README
%attr(755,root,root) %{_libdir}/libgames-support.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgames-support.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgames-support.so
%{_includedir}/gnome-games
%{_pkgconfigdir}/libgames-support-1.0.pc
%{_datadir}/vala/vapi/libgames-support-1.0.vapi
