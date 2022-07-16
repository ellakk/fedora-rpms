%global forgeurl https://github.com/ccope/PaperWM/tree/gnome-42
%global commit 132bbb5c1aa0a7923e02afebee1aa7e3e3569221
%global extension paperwm
%global uuid %{extension}@hedning:matrix.org

%forgemeta -v

Name: gnome-shell-extension-%{extension}
Version: %{commit}
Release: 1%{?dist}
Summary: Tiling window manager
URL: %{forgeurl}
Source:  %{forgesource}
License: GPLv3+

Requires: gnome-shell-extension-common


%description
PaperWM is an experimental Gnome Shell extension providing scrollable tiling of
windows and per monitor workspaces.

%prep
%forgesetup -v

%install
install -D -p -m 644 LICENSE -t %{buildroot}%{_datadir}/licenses/%{name}
install -D -p -m 644 README.md -t %{buildroot}%{_docdir}/%{name}
for i in $(find -type f)
  do
      install -Dm 644 $i %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}/$i
  done
install -D -p -m 0644 \
  schemas/org.gnome.shell.extensions.org-scrollwm.gschema.xml \
  %{buildroot}%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.%{extension}.gschema.xml

%files
%license LICENSE
%doc README.md
%{_datadir}/gnome-shell/extensions/%{uuid}
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.%{extension}.gschema.xml
