%define name gir-repository
%define version 0.6.5
%define git 0
%if %git
%define release %mkrel -c %git 1
%else
%define release %mkrel 8
%endif

%define api 1.0

Summary: GObject Introspection Repository
Name: %{name}
Version: %{version}
Release: %{release}
%if %git
Source0:       %{name}-%{git}.tar.bz2
%else
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/%name/%{name}-%{version}.tar.bz2
%endif
Patch:  gir-repository-0.6.4-new-gobject-introspection.patch
#gw: add dbus-glib binding needed for gnome-bluetooth
#patch from Fedora
# https://bugzilla.gnome.org/show_bug.cgi?id=604167 
Patch1: gir-repo-install-dbus-glib.patch
License: LGPLv2+
Group: Development/C
Url: http://www.gnome.org
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: gobject-introspection-devel >= 0.6.1
BuildRequires: dbus-glib-devel
BuildRequires: xft2-devel
BuildRequires: libxfixes-devel
BuildRequires: libxml2-devel
BuildRequires: GL-devel
BuildRequires: libpoppler-glib-devel
BuildRequires: libGConf2-devel
BuildRequires: libsoup-devel
BuildRequires: gupnp-devel
BuildRequires: babl-devel
BuildRequires: nautilus-devel
BuildRequires: libnotify-devel
BuildRequires: gtksourceview-devel
BuildRequires: vte-devel
BuildRequires: goocanvas-devel
BuildRequires: libgnome-keyring-devel
BuildRequires: libwnck-devel
#BuildRequires: avahi-core-devel
BuildRequires: avahi-gobject-devel
%if %git
BuildRequires: gnome-common
%endif

Requires: gobject-introspection

%description
This is a repository of GIR interface description files.


%prep
%if %git
%setup -q -n %name
./autogen.sh -V
%else
%setup -q
%endif
%patch -p1
%patch1 -p1
autoreconf -fi

%build
%configure2_5x --disable-static
%make

%install
rm -rf %{buildroot}
%makeinstall_std
rm %buildroot%_datadir/gir-%api/Atk-1.0.gir
rm -f %buildroot%_datadir/gir-%api/JSCore-1.0.gir
rm %buildroot%_datadir/gir-%api/Pango-1.0.gir
rm %buildroot%_datadir/gir-%api/PangoCairo-1.0.gir
rm %buildroot%_datadir/gir-%api/PangoFT2-1.0.gir
rm %buildroot%_datadir/gir-%api/PangoXft-1.0.gir
rm %buildroot%_datadir/gir-%api/Gdk-2.0.gir
rm %buildroot%_datadir/gir-%api/GdkPixbuf-2.0.gir
rm -f %buildroot%_datadir/gir-%api/GMenu-2.0.gir
rm -f %buildroot%_datadir/gir-%api/Gst*0.10.gir
rm %buildroot%_datadir/gir-%api/Gtk-2.0.gir
rm -f %buildroot%_datadir/gir-%api/Unique-1.0.gir
rm -f %buildroot%_datadir/gir-%api/WebKit-1.0.gir
rm %buildroot%_libdir/girepository-%api/Atk-1.0.typelib
rm -f %buildroot%_libdir/girepository-%api/JSCore-1.0.typelib
rm %buildroot%_libdir/girepository-%api/Gdk-2.0.typelib
rm %buildroot%_libdir/girepository-%api/GdkPixbuf-2.0.typelib
rm -f %buildroot%_libdir/girepository-%api/GMenu-2.0.typelib
rm -f %buildroot%_libdir/girepository-%api/Gst*0.10.typelib
rm %buildroot%_libdir/girepository-%api/Gtk-2.0.typelib
rm %buildroot%_libdir/girepository-%api/Pango-1.0.typelib
rm %buildroot%_libdir/girepository-%api/PangoCairo-1.0.typelib
rm %buildroot%_libdir/girepository-%api/PangoFT2-1.0.typelib
rm %buildroot%_libdir/girepository-%api/PangoXft-1.0.typelib
rm -f %buildroot%_libdir/girepository-%api/Unique-1.0.typelib
rm -f %buildroot%_libdir/girepository-%api/WebKit-1.0.typelib

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root)
%doc README NEWS AUTHORS
#%_datadir/gir-%api/Avahi-0.6.gir
#%_datadir/gir-%api/AvahiCore-0.6.gir
%_datadir/gir-%api/Babl-0.0.gir
%_datadir/gir-%api/DBus-1.0.gir
%_datadir/gir-%api/DBusGLib-1.0.gir
%_datadir/gir-%api/GConf-2.0.gir
%_datadir/gir-%api/GSSDP-1.0.gir
%_datadir/gir-%api/GnomeKeyring-2.0.gir
%_datadir/gir-%api/GooCanvas-0.10.gir
%_datadir/gir-%api/GtkSource-2.2.gir
%_datadir/gir-%api/GUPnP-1.0.gir
%_datadir/gir-%api/Nautilus-1.0.gir
%_datadir/gir-%api/Notify-0.4.gir
%_datadir/gir-%api/PangoX-1.0.gir
%_datadir/gir-%api/Poppler-0.8.gir
%_datadir/gir-%api/Soup-2.4.gir
%_datadir/gir-%api/Vte-1.0.gir
%_datadir/gir-%api/Wnck-1.0.gir
#%_libdir/girepository-%api/Avahi-0.6.typelib
#%_libdir/girepository-%api/AvahiCore-0.6.typelib
%_libdir/girepository-%api/Babl-0.0.typelib
%_libdir/girepository-%api/DBus-1.0.typelib
%_libdir/girepository-%api/DBusGLib-1.0.typelib
%_libdir/girepository-%api/GConf-2.0.typelib
%_libdir/girepository-%api/GSSDP-1.0.typelib
%_libdir/girepository-%api/GUPnP-1.0.typelib
%_libdir/girepository-%api/GnomeKeyring-2.0.typelib
%_libdir/girepository-%api/GooCanvas-0.10.typelib
%_libdir/girepository-%api/GtkSource-2.2.typelib
%_libdir/girepository-%api/Nautilus-1.0.typelib
%_libdir/girepository-%api/Notify-0.4.typelib
%_libdir/girepository-%api/PangoX-1.0.typelib
%_libdir/girepository-%api/Poppler-0.8.typelib
%_libdir/girepository-%api/Soup-2.4.typelib
%_libdir/girepository-%api/Vte-1.0.typelib
%_libdir/girepository-%api/Wnck-1.0.typelib

%_libdir/*.la
%_libdir/libgirepo-DBus-custom.so
%_libdir/libgirepo-Gdk-custom.so
%_libdir/libgirepo-Gtk-custom.so
#%_libdir/pkgconfig/%name-1.0.pc
