# Not needed here, debug info is empty
%define _enable_debug_packages %{nil}
%define debug_package %{nil}

%define git 20100907
%define api 1.0

Summary:	GObject Introspection Repository
Name:		gir-repository
Version:	0.6.6
Release:	0.%{git}.8
License:	LGPLv2+
Group:		Development/C
Url:		http://www.gnome.org
%if %{git}
Source0:	%{name}-%{git}.tar.xz
%else
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
%endif
Patch0:		gir-repository-disable-gtk.patch
Patch1:		gir-repository-fix-goo-build.patch
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(xft)
BuildRequires:	pkgconfig(xfixes)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(poppler-glib)
BuildRequires:	pkgconfig(libnautilus-extension)
BuildRequires:	pkgconfig(libnotify)
BuildRequires:	pkgconfig(gtksourceview-2.0)
BuildRequires:	pkgconfig(goocanvas)
BuildRequires:	pkgconfig(gnome-keyring-1)
BuildRequires:	pkgconfig(avahi-gobject)
%if %{git}
BuildRequires:	gnome-common
%endif

Requires:	%{mklibname girepository 1.0 1}

%description
This is a repository of GIR interface description files.

%prep
%if %{git}
%setup -q -n %{name}
%else
%setup -q
%endif

%apply_patches
%if %{git}
./autogen.sh -V
%else
autoreconf -fi
%endif

%build
%configure2_5x --disable-static
%make

%install
%makeinstall_std
rm -v %{buildroot}%{_datadir}/gir-%{api}/Atk-1.0.gir
rm -f %{buildroot}%{_datadir}/gir-%{api}/DBus*-1.0.gir
rm -v %{buildroot}%{_datadir}/gir-%{api}/Pango-1.0.gir
rm -v %{buildroot}%{_datadir}/gir-%{api}/PangoCairo-1.0.gir
rm -v %{buildroot}%{_datadir}/gir-%{api}/PangoFT2-1.0.gir
rm -v -f %{buildroot}%{_datadir}/gir-%{api}/GConf-2.0.gir
rm -v -f %{buildroot}%{_datadir}/gir-%{api}/GMenu-2.0.gir
rm -v -f %{buildroot}%{_datadir}/gir-%{api}/Gst*0.10.gir
rm -v -f %{buildroot}%{_datadir}/gir-%{api}/GSSDP-1.0.gir
rm -v -f %{buildroot}%{_datadir}/gir-%{api}/GUPnP-1.0.gir
rm -v -f %{buildroot}%{_datadir}/gir-%{api}/Soup-2.4.gir
rm -v -f %{buildroot}%{_datadir}/gir-%{api}/Unique-1.0.gir
rm -v -f %{buildroot}%{_datadir}/gir-%{api}/WebKit-1.0.gir
rm -v -f %{buildroot}%{_datadir}/gir-%{api}/Wnck-1.0.gir
rm -v %{buildroot}%{_libdir}/girepository-%{api}/Atk-1.0.typelib
rm -v -f %{buildroot}%{_libdir}/girepository-%{api}/GConf-2.0.typelib
rm -v -f %{buildroot}%{_libdir}/girepository-%{api}/GMenu-2.0.typelib
rm -v -f %{buildroot}%{_libdir}/girepository-%{api}/Gst*0.10.typelib
rm -v -f %{buildroot}%{_libdir}/girepository-%{api}/GSSDP-1.0.typelib
rm -v -f %{buildroot}%{_libdir}/girepository-%{api}/GUPnP-1.0.typelib
rm -v -f %{buildroot}%{_libdir}/girepository-%{api}/Soup-2.4.typelib
rm -v %{buildroot}%{_libdir}/girepository-%{api}/Pango-1.0.typelib
rm -v %{buildroot}%{_libdir}/girepository-%{api}/PangoCairo-1.0.typelib
rm -v %{buildroot}%{_libdir}/girepository-%{api}/PangoFT2-1.0.typelib
rm -v -f %{buildroot}%{_libdir}/girepository-%{api}/Unique-1.0.typelib
rm -v -f %{buildroot}%{_libdir}/girepository-%{api}/WebKit-1.0.typelib
rm -v -f %{buildroot}%{_libdir}/girepository-%{api}/Wnck-1.0.typelib
rm -v -f %{buildroot}%{_libdir}/libgirepo-DBus-custom.so

%files
%doc README NEWS AUTHORS
%{_datadir}/gir-%{api}/GnomeKeyring-2.0.gir
%{_datadir}/gir-%{api}/GooCanvas-0.10.gir
%{_datadir}/gir-%{api}/GtkSource-2.2.gir
%{_datadir}/gir-%{api}/Nautilus-1.0.gir
%{_datadir}/gir-%{api}/Notify-0.4.gir
%{_datadir}/gir-%{api}/Poppler-0.8.gir
%{_libdir}/girepository-%{api}/GnomeKeyring-2.0.typelib
%{_libdir}/girepository-%{api}/GooCanvas-0.10.typelib
%{_libdir}/girepository-%{api}/GtkSource-2.2.typelib
%{_libdir}/girepository-%{api}/Nautilus-1.0.typelib
%{_libdir}/girepository-%{api}/Notify-0.4.typelib
%{_libdir}/girepository-%{api}/Poppler-0.8.typelib

%changelog
* Sun May 08 2011 Funda Wang <fwang@mandriva.org> 0.6.6-0.20100907.4mdv2011.0
+ Revision: 672415
- do not like babl 1.4

  + Oden Eriksson <oeriksson@mandriva.com>
    - mass rebuild

* Sat Sep 18 2010 Götz Waschk <waschk@mandriva.org> 0.6.6-0.20100907.3mdv2011.0
+ Revision: 579669
- reenable libgnomekeyring support

* Sat Sep 18 2010 Götz Waschk <waschk@mandriva.org> 0.6.6-0.20100907.2mdv2011.0
+ Revision: 579617
- fix goocanvas build

* Sun Sep 12 2010 Götz Waschk <waschk@mandriva.org> 0.6.6-0.20100907.1mdv2011.0
+ Revision: 577707
- new snapshot
- bump g-i dep
- remove vte support
- temporarily disable goocanvas and gnome-keyring
- remove dbus support

* Fri Aug 06 2010 Funda Wang <fwang@mandriva.org> 0.6.5-12.20100622.2mdv2011.0
+ Revision: 566630
- we are using newer libname now

* Fri Jul 30 2010 Götz Waschk <waschk@mandriva.org> 0.6.5-12.20100622.1mdv2011.0
+ Revision: 563375
- new git snapshot
- drop all patches
- disable gtk bindings
- remove soup, gconf support
- add libnotify support

* Mon Apr 12 2010 Götz Waschk <waschk@mandriva.org> 0.6.5-11mdv2010.1
+ Revision: 533731
- remove support for gupnp and gssdp

* Thu Mar 18 2010 Götz Waschk <waschk@mandriva.org> 0.6.5-10mdv2010.1
+ Revision: 524981
- replace patch 2 by Fedora version, renames Babl binding
- drop patch 0, no longer needed
- remove PangoX, asked by fcrozat

* Tue Mar 09 2010 Götz Waschk <waschk@mandriva.org> 0.6.5-9mdv2010.1
+ Revision: 517236
- remove wnck support

* Mon Mar 08 2010 Götz Waschk <waschk@mandriva.org> 0.6.5-8mdv2010.1
+ Revision: 516583
- fix babl build
- remove gmenu bindings

* Tue Feb 09 2010 Götz Waschk <waschk@mandriva.org> 0.6.5-7mdv2010.1
+ Revision: 502910
- disable webkit support

* Wed Jan 13 2010 Götz Waschk <waschk@mandriva.org> 0.6.5-6mdv2010.1
+ Revision: 490641
- bump
- reenable libsoup support

* Tue Dec 22 2009 Götz Waschk <waschk@mandriva.org> 0.6.5-4mdv2010.1
+ Revision: 481260
- add DbusGlib binding
- remove gtk bindings now in gtk+2.0 package
- disable soup,webkit,gupnp (b.g.o. 605115)
- remove atk

* Fri Nov 13 2009 Götz Waschk <waschk@mandriva.org> 0.6.5-3mdv2010.1
+ Revision: 465757
- remove Unique support (bug #55583)

* Tue Oct 06 2009 Götz Waschk <waschk@mandriva.org> 0.6.5-3mdv2010.0
+ Revision: 454451
- remove gstreamer support

* Sun Sep 20 2009 Götz Waschk <waschk@mandriva.org> 0.6.5-2mdv2010.0
+ Revision: 445845
- rebuild for new gupnp

* Thu Sep 10 2009 Götz Waschk <waschk@mandriva.org> 0.6.5-1mdv2010.0
+ Revision: 437373
- remove files now in pango
- update to new version 0.6.5

* Tue Aug 25 2009 Götz Waschk <waschk@mandriva.org> 0.6.4-1mdv2010.0
+ Revision: 420776
- fix build with new gobject-introspection
- add gupnp support
- update to new version 0.6.4

* Mon Jun 22 2009 Götz Waschk <waschk@mandriva.org> 0.6.3-1mdv2010.0
+ Revision: 388084
- new version

* Tue Jun 16 2009 Götz Waschk <waschk@mandriva.org> 0.6.3-0.20090616.1mdv2010.0
+ Revision: 386314
- disable gssdp as well
- disable gupnp (it is in contrib)
- new snapshot
- disable Avahi
- update file list

* Mon Feb 09 2009 Götz Waschk <waschk@mandriva.org> 0.6.2-1mdv2009.1
+ Revision: 338998
- update build deps
- new version
- drop patches
- update file list
- remove all build workarounds

  + Adam Williamson <awilliamson@mandriva.org>
    - rebuild for new avahi-core major

* Wed Nov 26 2008 Götz Waschk <waschk@mandriva.org> 0.6.1-1mdv2009.1
+ Revision: 306940
- import gir-repository


