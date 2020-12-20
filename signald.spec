%define debug_package %{nil}

Name:          signald
Version:       0.11.0
Release:       1%{?dist}
Summary:       A daemon that facilitates communication over Signal
License:       GPLv3

URL:           https://gitlab.com/thefinn93/signald
Source0:       %{url}/-/archive/%version/%name-%version.tar.gz

BuildArch:     noarch

BuildRequires: java-11-openjdk-devel

Requires:      java-11-openjdk
Requires:      qrencode

%description
%{summary}.

%prep
%autosetup

%build
./gradlew build

%install
VERSION=%{version} ./gradlew installDist
install -D build/install/%{name}/bin/%{name} %{buildroot}%{_bindir}/%{name}

sed -i 's|$APP_HOME/lib|%{_libdir}|g' %{buildroot}%{_bindir}/%{name}

mkdir -p %{buildroot}%{_libdir}
cp build/install/%{name}/lib/* %{buildroot}%{_libdir}/

# this empty directory is required for signald to start
install -dm 777 %{buildroot}/var/run/signald

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_libdir}/*
/var/run/signald/
