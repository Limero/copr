%define debug_package %{nil}

Name:          pmbootstrap
Version:       1.31.0
Release:       1%{?dist}
Summary:       Sophisticated chroot/build/flash tool to develop and install postmarketOS
License:       GPLv3

URL:           https://gitlab.com/postmarketOS/pmbootstrap
Source0:       %{url}/-/archive/%version/%name-%version.tar.gz

BuildArch:     noarch

BuildRequires: python3-devel
BuildRequires: python3-setuptools

Requires:      openssl

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
%{python3_sitelib}/pmb/
%{_bindir}/%{name}
