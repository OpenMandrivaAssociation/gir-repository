%define name gir-repository
%define version 0.6.1
%define release %mkrel 1

Summary: GObject Introspection Repository
Name: %{name}
Version: %{version}
Release: %{release}
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/%name/%{name}-%{version}.tar.bz2
Patch: gir-repository-0.6.1-soup-build.patch
Patch1: gir-repository-0.6.1-missing-files.patch
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
BuildRequires: babl-devel
BuildRequires: nautilus-devel
BuildRequires: webkitgtk-devel
BuildRequires: libnotify-devel
BuildRequires: clutter-gtk-devel clutter-cairo-devel
BuildRequires: libgstreamer-plugins-base-devel
BuildRequires: gtksourceview-devel
BuildRequires: vte-devel
BuildRequires: goocanvas-devel
BuildRequires: gupnp-devel
BuildRequires: avahi-gobject-devel avahi-core-devel
BuildRequires: unique-devel
BuildRequires: gnome-menus-devel
Requires: gobject-introspection

%description
This is a repository of GIR interface description files.


%prep
%setup -q
%patch -p1
%patch1 -p1
autoreconf

%build
%configure2_5x --disable-static
#make it find libtool
export PATH=$(pwd):$PATH
#gw parallel make fails in 0.6.1
make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root)
%doc README NEWS TODO AUTHORS
%_datadir/gir/Atk-1.0.gir
%_datadir/gir/Avahi-0.6.gir
%_datadir/gir/AvahiCore-0.6.gir
%_datadir/gir/Babl-0.0.gir
%_datadir/gir/Clutter-0.8.gir
%_datadir/gir/ClutterCairo-0.8.gir
%_datadir/gir/ClutterJson-0.8.gir
%_datadir/gir/DBus-1.0.gir
%_datadir/gir/GConf-2.0.gir
%_datadir/gir/GL-1.0.gir
%_datadir/gir/GMenu-2.0.gir
%_datadir/gir/GSSDP-1.0.gir
%_datadir/gir/Gdk-2.0.gir
%_datadir/gir/GdkPixbuf-2.0.gir
%_datadir/gir/GnomeKeyring-2.0.gir
%_datadir/gir/GooCanvas-0.10.gir
%_datadir/gir/Gst-0.10.gir
%_datadir/gir/GstAudio-0.10.gir
%_datadir/gir/GstBase-0.10.gir
%_datadir/gir/GstController-0.10.gir
%_datadir/gir/GstFft-0.10.gir
%_datadir/gir/GstInterfaces-0.10.gir
%_datadir/gir/GstNet-0.10.gir
%_datadir/gir/GstNetbuffer-0.10.gir
%_datadir/gir/GstPbutils-0.10.gir
%_datadir/gir/GstRiff-0.10.gir
%_datadir/gir/GstRtp-0.10.gir
%_datadir/gir/GstRtsp-0.10.gir
%_datadir/gir/GstSdp-0.10.gir
%_datadir/gir/GstTag-0.10.gir
%_datadir/gir/GstVideo-0.10.gir
%_datadir/gir/Gtk-2.0.gir
%_datadir/gir/GtkClutter-0.8.gir
%_datadir/gir/GtkSource-2.2.gir
%_datadir/gir/Gupnp-1.0.gir
%_datadir/gir/JSCore-1.0.gir
%_datadir/gir/Nautilus-1.0.gir
%_datadir/gir/Notify-0.4.gir
%_datadir/gir/Pango-1.0.gir
%_datadir/gir/PangoCairo-1.0.gir
%_datadir/gir/PangoFT2-1.0.gir
%_datadir/gir/PangoX-1.0.gir
%_datadir/gir/PangoXft-1.0.gir
%_datadir/gir/Poppler-0.8.gir
%_datadir/gir/Soup-2.0.gir
%_datadir/gir/Unique-1.0.gir
%_datadir/gir/Vte-1.0.gir
%_datadir/gir/WebKit-1.0.gir
%_datadir/gir/cairo-1.0.gir
%_datadir/gir/fontconfig-2.0.gir
%_datadir/gir/freetype2-2.0.gir
%_datadir/gir/libxml2-2.0.gir
%_datadir/gir/xfixes-4.0.gir
%_datadir/gir/xft-2.0.gir
%_datadir/gir/xlib-2.0.gir
%_libdir/girepository/Atk-1.0.typelib
%_libdir/girepository/Avahi-0.6.typelib
%_libdir/girepository/AvahiCore-0.6.typelib
%_libdir/girepository/Babl-0.0.typelib
%_libdir/girepository/Clutter-0.8.typelib
%_libdir/girepository/ClutterCairo-0.8.typelib
%_libdir/girepository/ClutterJson-0.8.typelib
%_libdir/girepository/DBus-1.0.typelib
%_libdir/girepository/GConf-2.0.typelib
%_libdir/girepository/GL-1.0.typelib
%_libdir/girepository/GMenu-2.0.typelib
%_libdir/girepository/GSSDP-1.0.typelib
%_libdir/girepository/Gdk-2.0.typelib
%_libdir/girepository/GdkPixbuf-2.0.typelib
%_libdir/girepository/GnomeKeyring-2.0.typelib
%_libdir/girepository/GooCanvas-0.10.typelib
%_libdir/girepository/Gst-0.10.typelib
%_libdir/girepository/GstAudio-0.10.typelib
%_libdir/girepository/GstBase-0.10.typelib
%_libdir/girepository/GstController-0.10.typelib
%_libdir/girepository/GstFft-0.10.typelib
%_libdir/girepository/GstInterfaces-0.10.typelib
%_libdir/girepository/GstNet-0.10.typelib
%_libdir/girepository/GstNetbuffer-0.10.typelib
%_libdir/girepository/GstPbutils-0.10.typelib
%_libdir/girepository/GstRiff-0.10.typelib
%_libdir/girepository/GstRtp-0.10.typelib
%_libdir/girepository/GstRtsp-0.10.typelib
%_libdir/girepository/GstSdp-0.10.typelib
%_libdir/girepository/GstTag-0.10.typelib
%_libdir/girepository/GstVideo-0.10.typelib
%_libdir/girepository/Gtk-2.0.typelib
%_libdir/girepository/GtkClutter-0.8.typelib
%_libdir/girepository/GtkSource-2.2.typelib
%_libdir/girepository/Gupnp-1.0.typelib
%_libdir/girepository/JSCore-1.0.typelib
%_libdir/girepository/Nautilus-1.0.typelib
%_libdir/girepository/Notify-0.4.typelib
%_libdir/girepository/Pango-1.0.typelib
%_libdir/girepository/PangoCairo-1.0.typelib
%_libdir/girepository/PangoFT2-1.0.typelib
%_libdir/girepository/PangoX-1.0.typelib
%_libdir/girepository/PangoXft-1.0.typelib
%_libdir/girepository/Poppler-0.8.typelib
%_libdir/girepository/Soup-2.0.typelib
%_libdir/girepository/Unique-1.0.typelib
%_libdir/girepository/Vte-1.0.typelib
%_libdir/girepository/WebKit-1.0.typelib
%_libdir/girepository/cairo-1.0.typelib
%_libdir/girepository/fontconfig-2.0.typelib
%_libdir/girepository/freetype2-2.0.typelib
%_libdir/girepository/libxml2-2.0.typelib
%_libdir/girepository/xfixes-4.0.typelib
%_libdir/girepository/xft-2.0.typelib
%_libdir/girepository/xlib-2.0.typelib

%_libdir/libgirepo-Clutter-custom.la
%_libdir/libgirepo-Clutter-custom.so
%_libdir/libgirepo-Gdk-custom.la
%_libdir/libgirepo-Gdk-custom.so
%_libdir/libgirepo-Gtk-custom.la
%_libdir/libgirepo-Gtk-custom.so
%_libdir/pkgconfig/%name-1.0.pc
