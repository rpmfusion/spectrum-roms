%define real_version 20081224

Name:           spectrum-roms
Version:        0.0.%{real_version}
Release:        24%{?dist}
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
* Wed Jan 29 2025 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.0.20081224-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Aug 03 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.0.20081224-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Feb 04 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.0.20081224-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Aug 03 2023 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.0.20081224-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Aug 08 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.0.20081224-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Thu Feb 10 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.0.20081224-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Aug 04 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.0.20081224-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Feb 04 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.0.20081224-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 19 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.0.20081224-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Feb 05 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.0.20081224-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Aug 10 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.0.20081224-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 05 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.0.20081224-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Aug 19 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.0.20081224-12
- Rebuilt for Fedora 29 Mass Rebuild binutils issue

* Fri Jul 27 2018 RPM Fusion Release Engineering <sergio@serjux.com> - 0.0.20081224-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

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

