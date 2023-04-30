%global         debug_package %{nil}
Name:           starship
Version:        1.14.2
Release:        1%{?dist}
Summary:        Minimal, blazing-fast, and infinitely customizable prompt for any shell!
License:        ISC
URL:            https://github.com/starship/starship
Source0:        %{url}/releases/download/v%{version}/%{name}-x86_64-unknown-linux-gnu.tar.gz

%description
Minimal, blazing-fast, and infinitely customizable prompt for any shell!

%prep
%setup

%build

%install
install -p -D %{name} %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}
