Name:		libvirt-snmp
Version:	0.0.3
Release:	1%{?dist}%{?extra_release}
Summary:	SNMP functionality for libvirt

Group:		Development/Libraries
License:	GPLv2+
URL:		http://libvirt.org
Source0:	http://www.libvirt.org/sources/snmp/libvirt-snmp-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

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
%defattr(-,root,root,-)
%{_bindir}/libvirtMib_subagent
%{_datadir}/snmp/mibs/LIBVIRT-MIB.txt
%doc README NEWS ChangeLog AUTHORS
%{_mandir}/man1/libvirtMib_subagent.1*


%changelog
* Fri Sep  7 2012 Michal Privoznik <mprivozn@redhat.com> 0.0.3-1
- various bug fixes and improvements

* Wed Mar 23 2011 Michal Privoznik <mprivozn@redhat.com> 0.0.2-1
- add SNMP trap/notification support

* Fri Mar 11 2011 Michal Privoznik <mprivozn@redhat.com> 0.0.1-3
- remove LIBVIRT-MIB.txt from doc

* Wed Mar  9 2011 Michal Privoznik <mprivozn@redhat.com> 0.0.1-2
- resolve licensing conflicts
- add unified header to sources

* Thu Feb  2 2011 Michal Privoznik <mprivozn@redhat.com> 0.0.1-1
- initial revision
