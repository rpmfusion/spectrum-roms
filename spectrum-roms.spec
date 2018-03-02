%define real_version 20081224

Name:           spectrum-roms
Version:        0.0.%{real_version}
Release:        10%{?dist}
Summary:        A collection of Spectrum ROM images

License:        Distributable
URL:            http://www.chiark.greenend.org.uk/~cjwatson/code/spectrum-roms/
Source0:        http://www.chiark.greenend.org.uk/~cjwatson/code/%{name}/%{name}-%{real_version}.tar.gz
Source1:        %{name}-distribution.txt

BuildArch:      noarch
BuildRequires:  perl


%description
This package provides images of the read-only memories from various
versions of the Sinclair Spectrum. They can be used with various emulators.


%prep
%setup -q -n %{name}


%build
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT%{_prefix}

# Install Amstrad distribution acknowledge
install -pm 0644 %{SOURCE1} distribution.txt

# Remove installed docs
rm -rf $RPM_BUILD_ROOT%{_docdir}


%files
%{_datadir}/%{name}
%doc ChangeLog README distribution.txt 


%changelog
* Fri Mar 02 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 0.0.20081224-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 0.0.20081224-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Mar 26 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 0.0.20081224-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Andrea Musuruane <musuruan@gmail.com> - 0.0.20081224-7
- Added perl BR per
  https://fedoraproject.org/wiki/Changes/Build_Root_Without_Perl
- Dropped cleaning at the beginning of %%install

* Sun Aug 31 2014 Sérgio Basto <sergio@serjux.com> - 0.0.20081224-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Aug 12 2013 Andrea Musuruane <musuruan@gmail.com> 0.0.20081224-5
- Dropped obsolete Group, Buildroot, %%clean and %%defattr

* Tue Mar 12 2013 Nicolas Chauvet <kwizart@gmail.com> - 0.0.20081224-4
- https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Feb 09 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.0.20081224-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Aug 12 2009 Andrea Musuruane <musuruan@gmail.com> 0.0.20081224-2
- Cosmetic changes

* Sat Jul 25 2009 Andrea Musuruane <musuruan@gmail.com> 0.0.20081224-1
- First release

