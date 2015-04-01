Name     : cinder-controller-services
Version  : 2015.1.0b3
Release  : 2
Source0  : cinder-api.service
Source1  : cinder-scheduler.service
Summary  : Cinder Controller Services
Group    : Development/Tools
License  : Apache-2.0

%description
Cinder Controller Services files

%setup

%build

%install
mkdir -p %{buildroot}/usr/lib/systemd/system
install -m 0644 %{SOURCE0} %{buildroot}/usr/lib/systemd/system/
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/systemd/system/

%files
%defattr(-,root,root,-)
/usr/lib/systemd/system/cinder-api.service
/usr/lib/systemd/system/cinder-scheduler.service
