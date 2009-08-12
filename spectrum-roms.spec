%define real_version 20081224

Name:           spectrum-roms
Version:        0.0.%{real_version}
Release:        1
Summary:        A collection of Spectrum ROM images

Group:          Applications/Emulators
License:        Distributable
URL:            http://www.chiark.greenend.org.uk/~cjwatson/code/spectrum-roms/
Source0:        http://www.chiark.greenend.org.uk/~cjwatson/code/spectrum-roms/spectrum-roms-%{real_version}.tar.gz
Source1:        spectrum-roms-distribution.txt
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
install -pm 0644 %{SOURCE1} .

# Remove installed docs
rm -rf $RPM_BUILD_ROOT%{_docdir}


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%{_datadir}/%{name}
%doc ChangeLog README spectrum-roms-distribution.txt 


%changelog
* Sat Jul 25 2009 Andrea Musuruane <musuruan@gmail.com> 0.0.20081224-1
- First release

