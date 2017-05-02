Name     : cinder-controller-services
Version  : 2015.1.0
Release  : 11
Source0  : cinder-api.service
Source1  : cinder-scheduler.service
Source2  : api.ini
Summary  : Cinder Controller Services
Group    : Development/Tools
License  : Apache-2.0

%description
Cinder Controller Services files

%setup

%build

%install
mkdir -p %{buildroot}/usr/lib/systemd/system
mkdir -p %{buildroot}/usr/share/uwsgi/cinder
install -m 0644 %{SOURCE0} %{buildroot}/usr/lib/systemd/system/
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/systemd/system/
install -m 0644 %{SOURCE2} %{buildroot}/usr/share/uwsgi/cinder

%files
%defattr(-,root,root,-)
/usr/lib/systemd/system/cinder-api.service
/usr/lib/systemd/system/cinder-scheduler.service
/usr/share/uwsgi/cinder/api.ini
