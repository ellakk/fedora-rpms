Name:           xkeysnail
Version:        0.4.0
Release:        %autorelease
Summary:        Simplified and community-driven man pages

License:        MIT
URL:            https://github.com/mooz/xkeysnail
Source0:        https://files.pythonhosted.org/packages/source/x/%{name}/%{name}-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

%description
xkeysnail is yet another keyboard remapping tool for X environment
written in Python. It's like xmodmap but allows more flexible remappings.

%global debug_package %{nil}

%prep
%autosetup -n %{name}-%{version}

%generate_buildrequires
%pyproject_buildrequires
%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files xkeysnail

%files -f %{pyproject_files}
# %license LICENSE.md
#%doc README.md
%{_bindir}/%{name}

%changelog
