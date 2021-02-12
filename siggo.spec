%define debug_package %{nil}

Name: siggo
Version: 0.9.0
Release: 1%{?dist}
Summary: A terminal ui for signal-cli, written in Go
License: GPLv3+

URL: https://github.com/derricw/siggo
Source0: %{url}/archive/%{version}.tar.gz

BuildRequires: git
BuildRequires: golang

Requires: signal-cli
Requires: libmatthew-java

%description
%{summary}.

%prep
%autosetup

%build
make build

%install
install -p -D -m755 bin/%{name}         %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}

%doc README.md
%license LICENSE
