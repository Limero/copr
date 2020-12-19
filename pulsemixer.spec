# based on https://github.com/PhantomX/chinforpms/blob/master/pulsemixer/pulsemixer.spec
%define debug_package %{nil}

Name:          pulsemixer
Version:       1.5.1
Release:       1%{?dist}
Summary:       CLI and curses mixer for PulseAudio
License:       MIT

URL:           https://github.com/GeorgeFilipkin/pulsemixer
Source0:       %{url}/archive/%version.tar.gz

BuildArch:     noarch

BuildRequires: python3-devel
BuildRequires: python3-setuptools

Requires:      pulseaudio

%description
%{summary}.

%prep
%autosetup

%build
%py3_build

%install
%py3_install

%files
%license LICENSE
%doc README.md
%{python3_sitelib}/%{name}*.egg-info/
%{_bindir}/%{name}
