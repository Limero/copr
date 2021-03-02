# based on https://gitlab.com/elagost/rpm-specfiles/-/blob/master/signal-cli/signal-cli.spec
%define debug_package %{nil}

Name:          signal-cli
Version:       0.8.1
Release:       1%{?dist}
Summary:       Provides a commandline and dbus interface for secure Signal messaging
License:       GPL

URL:           https://github.com/AsamK/signal-cli
Source0:       %{url}/archive/v%version.tar.gz

BuildArch:     noarch

BuildRequires: java-11-openjdk-devel

Requires:      java-11-openjdk

%description
%{summary}.

%prep
%autosetup

%build
./gradlew build

%install
./gradlew installDist
install -D build/install/signal-cli/bin/signal-cli %{buildroot}%{_bindir}/%{name}

sed -i 's|$APP_HOME/lib|%{_libdir}|g' %{buildroot}%{_bindir}/%{name}

mkdir -p %{buildroot}%{_libdir}
cp build/install/signal-cli/lib/* %{buildroot}%{_libdir}/

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_libdir}/*
