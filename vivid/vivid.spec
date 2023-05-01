Name:           vivid
Version:        0.9.0
Release:        1%{?dist}
Summary:        vivid is a generator for the LS_COLORS
License:        MIT
URL:            https://github.com/sharkdp/vivid
Source0:        https://github.com/sharkdp/vivid/releases/download/v%{version}/vivid-v%{version}-x86_64-unknown-linux-gnu.tar.gz

%description
vivid is a generator for the LS_COLORS environment variable that controls the colorized output of ls, tree, fd, bfs, dust and many other tools.

%prep
%setup -n vivid-v%{version}-x86_64-unknown-linux-gnu

%install
install -D -p -m 755 vivid -t %{buildroot}%{_bindir}/vivid

%files
%license LICENSE-MIT
%doc README.md
%{_bindir}/%{name}
