Name:           helm
Version:        3.8.0
Release:        1%{?dist}
Summary:        The Kubernetes Package Manager

License:        ASL 2.0
URL:            https://github.com/helm/helm
Source0:        https://get.helm.sh/helm-v%{version}-linux-amd64.tar.gz

%description
Helm helps you manage Kubernetes applications — Helm Charts help you define, install, and upgrade even the most complex Kubernetes application.

%install
#mkdir -p %{buildroot}%{_bindir}
#mkdir -p %{buildroot}%{_datadir}/licenses/%{name}
#mkdir -p %{buildroot}%{_docdir}/%{name}

tar xzf %{_sourcedir}/helm-v%{version}-linux-amd64.tar.gz
install -D -p -m 755 linux-amd64/helm -t %{buildroot}%{_bindir}
install -D -p -m 644 linux-amd64/LICENSE -t %{buildroot}%{_datadir}/licenses/%{name}
install -D -p -m 644 linux-amd64/README.md -t %{buildroot}%{_docdir}/%{name}

for i in bash,bash-completion/completions,%{name} fish,fish/vendor_completions.d,%{name}.fish zsh,zsh/site-functions,_%{name}; do IFS=","
    set -- $i
    mkdir -p %{buildroot}%{_datadir}/$2
    %{buildroot}%{_bindir}/%{name} completion $1 > %{buildroot}%{_datadir}/$2/$3
done

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/bash-completion/
%{_datadir}/fish/
%{_datadir}/zsh/

