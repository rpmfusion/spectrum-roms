%define real_version 20081224

Name:           spectrum-roms
Version:        0.0.%{real_version}
Release:        4%{?dist}
Summary:        A collection of Spectrum ROM images

Group:          Applications/Emulators
License:        Distributable
URL:            http://www.chiark.greenend.org.uk/~cjwatson/code/spectrum-roms/
Source0:        http://www.chiark.greenend.org.uk/~cjwatson/code/%{name}/%{name}-%{real_version}.tar.gz
Source1:        %{name}-distribution.txt
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch


%description
This package provides images of the read-only memories from various
versions of the Sinclair Spectrum. They can be used with various emulators.


%prep
%setup -q -n %{name}


%build
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT%{_prefix}

# Install Amstrad distribution acknowledge
install -pm 0644 %{SOURCE1} distribution.txt

# Remove installed docs
rm -rf $RPM_BUILD_ROOT%{_docdir}


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%{_datadir}/%{name}
%doc ChangeLog README distribution.txt 


%changelog
* Tue Mar 12 2013 Nicolas Chauvet <kwizart@gmail.com> - 0.0.20081224-4
- https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Feb 09 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.0.20081224-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Aug 12 2009 Andrea Musuruane <musuruan@gmail.com> 0.0.20081224-2
- Cosmetic changes

* Sat Jul 25 2009 Andrea Musuruane <musuruan@gmail.com> 0.0.20081224-1
- First release

