Name:		libvirt-snmp
Version:	0.0.3
Release:	5%{?dist}
Summary:	SNMP functionality for libvirt

Group:		Development/Libraries
License:	GPLv2+
URL:		http://libvirt.org
Source0:	http://www.libvirt.org/sources/snmp/libvirt-snmp-%{version}.tar.gz

BuildRequires: net-snmp-perl net-snmp net-snmp-utils net-snmp-devel libvirt-devel

%description
Provides a way to control libvirt through SNMP protocol.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

%files
%{_bindir}/libvirtMib_subagent
%{_datadir}/snmp/mibs/LIBVIRT-MIB.txt
%doc README NEWS ChangeLog AUTHORS
%{_mandir}/man1/libvirtMib_subagent.1*


%changelog
* Fri Feb 14 2014 Michal Privoznik <mprivozn@redhat.com> - 0.0.3-5
- Rebuild for fixed net-snmp (libvirt-snmp BZ: 1064346 net-snmp BZ: 1064437)
- Fix day name in the changelog (Feb 2 2011 was Wed not Thu)

* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 0.0.3-4
- Mass rebuild 2014-01-24

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 0.0.3-3
- Mass rebuild 2013-12-27

* Fri Jul 12 2013 Jan Safranek <jsafrane@redhat.com> - 0.0.3-2
- Rebuilt for new net-snmp

* Thu Feb 21 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.0.3-2
- Merge f18 into rawhide, cleanup spec

* Fri Feb 15 2013 Michal Privoznik <mprivozn@redhat.com> 0.0.3-1
- various bug fixes and improvements

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Apr 13 2012 Jindrich Novy <jnovy@redhat.com> 0.0.2-4
- rebuild against new librpm

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Sep 19 2011 Adam Jackson <ajax@redhat.com> 0.0.2-2
- Rebuild for new snmp lib sonames

* Wed Mar 23 2011 Michal Privoznik <mprivozn@redhat.com> 0.0.2-1
- add SNMP trap/notification support

* Fri Mar 11 2011 Michal Privoznik <mprivozn@redhat.com> 0.0.1-3
- remove LIBVIRT-MIB.txt from doc

* Wed Mar  9 2011 Michal Privoznik <mprivozn@redhat.com> 0.0.1-2
- resolve licensing conflicts
- add unified header to sources

* Wed Feb  2 2011 Michal Privoznik <mprivozn@redhat.com> 0.0.1-1
- initial revision
