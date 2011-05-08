%define name gir-repository
%define version 0.6.6
%define git 20100907
%define rel 4
%if %git
%define release %mkrel -c %git %rel
%else
%define release %mkrel %rel
%endif

%define api 1.0

Summary: GObject Introspection Repository
Name: %{name}
Version: %{version}
Release: %{release}
%if %git
Source0:       %{name}-%{git}.tar.xz
%else
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/%name/%{name}-%{version}.tar.bz2
%endif
Patch0: gir-repository-disable-gtk.patch
Patch1: gir-repository-fix-goo-build.patch
License: LGPLv2+
Group: Development/C
Url: http://www.gnome.org
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: gobject-introspection-devel >= 0.9.5
BuildRequires: xft2-devel
BuildRequires: libxfixes-devel
BuildRequires: libxml2-devel
BuildRequires: GL-devel
BuildRequires: libpoppler-glib-devel
BuildRequires: nautilus-devel
BuildRequires: libnotify-devel
BuildRequires: gtksourceview-devel
BuildRequires: goocanvas-devel
BuildRequires: libgnome-keyring-devel
#BuildRequires: avahi-core-devel
BuildRequires: avahi-gobject-devel
%if %git
BuildRequires: gnome-common
%endif

Requires: %mklibname girepository 1.0 1

%description
This is a repository of GIR interface description files.


%prep
%if %git
%setup -q -n %name
%else
%setup -q
%endif
%apply_patches
%if %git
./autogen.sh -V
%else
autoreconf -fi
%endif

%build
%configure2_5x --disable-static
%make

%install
rm -rf %{buildroot}
%makeinstall_std
rm -v %buildroot%_datadir/gir-%api/Atk-1.0.gir
rm -f %buildroot%_datadir/gir-%api/DBus*-1.0.gir
rm -v %buildroot%_datadir/gir-%api/Pango-1.0.gir
rm -v %buildroot%_datadir/gir-%api/PangoCairo-1.0.gir
rm -v %buildroot%_datadir/gir-%api/PangoFT2-1.0.gir
rm -v %buildroot%_datadir/gir-%api/PangoXft-1.0.gir
rm -v -f %buildroot%_datadir/gir-%api/GConf-2.0.gir
rm -v -f %buildroot%_datadir/gir-%api/GMenu-2.0.gir
rm -v -f %buildroot%_datadir/gir-%api/Gst*0.10.gir
rm -v -f %buildroot%_datadir/gir-%api/GSSDP-1.0.gir
rm -v -f %buildroot%_datadir/gir-%api/GUPnP-1.0.gir
rm -v -f %buildroot%_datadir/gir-%api/Soup-2.4.gir
rm -v -f %buildroot%_datadir/gir-%api/Unique-1.0.gir
rm -v -f %buildroot%_datadir/gir-%api/WebKit-1.0.gir
rm -v -f %buildroot%_datadir/gir-%api/Wnck-1.0.gir
rm -v %buildroot%_libdir/girepository-%api/Atk-1.0.typelib
rm -v %buildroot%_libdir/girepository-%api/DBus*-1.0.typelib
rm -v -f %buildroot%_libdir/girepository-%api/GConf-2.0.typelib
rm -v -f %buildroot%_libdir/girepository-%api/GMenu-2.0.typelib
rm -v -f %buildroot%_libdir/girepository-%api/Gst*0.10.typelib
rm -v -f %buildroot%_libdir/girepository-%api/GSSDP-1.0.typelib
rm -v -f %buildroot%_libdir/girepository-%api/GUPnP-1.0.typelib
rm -v -f %buildroot%_libdir/girepository-%api/Soup-2.4.typelib
rm -v %buildroot%_libdir/girepository-%api/Pango-1.0.typelib
rm -v %buildroot%_libdir/girepository-%api/PangoCairo-1.0.typelib
rm -v %buildroot%_libdir/girepository-%api/PangoFT2-1.0.typelib
rm -v %buildroot%_libdir/girepository-%api/PangoXft-1.0.typelib
rm -v -f %buildroot%_libdir/girepository-%api/Unique-1.0.typelib
rm -v -f %buildroot%_libdir/girepository-%api/WebKit-1.0.typelib
rm -v -f %buildroot%_libdir/girepository-%api/Wnck-1.0.typelib
rm -v -f %buildroot%_libdir/libgirepo-DBus-custom.so
%clean
rm  -rf %{buildroot}


%files
%defattr(-,root,root)
%doc README NEWS AUTHORS
%_datadir/gir-%api/GnomeKeyring-2.0.gir
%_datadir/gir-%api/GooCanvas-0.10.gir
%_datadir/gir-%api/GtkSource-2.2.gir
%_datadir/gir-%api/Nautilus-1.0.gir
%_datadir/gir-%api/Notify-0.4.gir
%_datadir/gir-%api/Poppler-0.8.gir
%_libdir/girepository-%api/GnomeKeyring-2.0.typelib
%_libdir/girepository-%api/GooCanvas-0.10.typelib
%_libdir/girepository-%api/GtkSource-2.2.typelib
%_libdir/girepository-%api/Nautilus-1.0.typelib
%_libdir/girepository-%api/Notify-0.4.typelib
%_libdir/girepository-%api/Poppler-0.8.typelib

%_libdir/*.la
#%_libdir/pkgconfig/%name-1.0.pc
