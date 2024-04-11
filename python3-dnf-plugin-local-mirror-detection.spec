Name:       python3-dnf-plugin-local-mirror-detection
Version:    1.0.0
Release:    3%{?dist}
Summary:    A DNF plugin to detect and use local mirrors if available.
License:    GPL-3.0-or-later
URL:        https://github.com/michel-ludwig/dnf-local-mirror-detection/
Source0:    https://github.com/michel-ludwig/dnf-local-mirror-detection/archive/refs/heads/master.tar.gz
BuildArch:  noarch
BuildRequires: python3-devel
BuildRequires: python3-rpm-macros
Requires: python3-dnf

%description
A DNF plugin to detect and use local mirrors if available.

%prep
%autosetup -n dnf-local-mirror-detection-master

%build

%install
mkdir -p %{buildroot}%{python3_sitelib}/dnf-plugins/
mkdir -p %{buildroot}%{_defaultlicensedir}/python-dnf-plugin-local-mirror-detection/
mkdir -p %{buildroot}%{_defaultdocdir}/python-dnf-plugin-local-mirror-detection/
install -m 0644 src/local-mirror-detection.py %{buildroot}%{python3_sitelib}/dnf-plugins/local-mirror-detection.py
install -m 0644 LICENSE %{buildroot}%{_defaultlicensedir}/python-dnf-plugin-local-mirror-detection/LICENSE
install -m 0644 README.md %{buildroot}%{_defaultdocdir}/python-dnf-plugin-local-mirror-detection/README.md

%check

%files
%{python3_sitelib}/dnf-plugins/local-mirror-detection.py
%{python3_sitelib}/dnf-plugins/__pycache__/local-mirror-detection.cpython-312.opt-1.pyc
%{python3_sitelib}/dnf-plugins/__pycache__/local-mirror-detection.cpython-312.pyc
%{_defaultlicensedir}/python-dnf-plugin-local-mirror-detection
%{_defaultdocdir}/python-dnf-plugin-local-mirror-detection

%changelog
* Wed Apr 10 2024 Jason Montleon <jmontleo@redhat.com> - 1.0.0-3
- Fix some more minor packaging discrepancies 

* Wed Apr 10 2024 Jason Montleon <jmontleo@redhat.com> - 1.0.0-2
- Fix some minor packaging discrepancies 

* Wed Apr 10 2024 Jason Montleon <jmontleo@redhat.com> - 1.0.0-1
- Initial Build
