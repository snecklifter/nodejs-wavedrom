%{?nodejs_find_provides_and_requires}

%global module_name wavedrom

Name:       nodejs-%{module_name}
Version:    2.6.8
Release:    1%{?dist}
Summary:    Digital timing diagram in your browser
License:    MIT
URL:        https://www.npmjs.com/package/%{module_name}
Source0:    https://registry.npmjs.org/%{module_name}/-/%{module_name}-${version}.tgz

BuildArch:  noarch

BuildRequires:  nodejs-packaging

ExclusiveArch: %{nodejs_arches} noarch

%description
WaveDrom draws your Timing Diagram or Waveform from simple textual description.
It comes with description language, rendering engine and the editor.
WaveDrom editor works in the browser or can be installed on your system.
Rendering engine can be embeded into any webpage. 

%prep
%setup -q -n package 

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{module_name}
cp -pr %{module_name}.js package.json \
    %{buildroot}%{nodejs_sitelib}/%{module_name}

%{nodejs_symlink_deps}

%check
%{nodejs_symlink_deps} --check

%files
%doc README.md
%license LICENSE
%{nodejs_sitelib}/%{module_name}

%changelog
* Wed Oct 28 2020 Christopher Brown <chris.brown@redhat.com> - 2.6.8-1
- Initial package
