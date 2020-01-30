%global pypi_name msldap

Name:           python-%{pypi_name}
Version:        0.2.5
Release:        3%{?dist}
Summary:        Python library to play with MS LDAP

License:        MIT
URL:            https://github.com/skelsec/msldap
Source0:        %{pypi_source}
Source1:        https://raw.githubusercontent.com/skelsec/msldap/master/LICENSE
BuildArch:      noarch

%description
Python library to play with MS LDAP.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Python library to play with MS LDAP.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info
cp -a %{SOURCE1} LICENSE
sed -i -e '/^#!\//, 1d' %{pypi_name}/{*.py,*/*.py,*/*/*.py}
sed -i -e 's/ldap3<2.5.2/ldap3/g' setup.py

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.md
%license LICENSE
%{_bindir}/msldap
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py*.egg-info

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 23 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.5-2
- Fix requirement (rhbz#1790355)

* Sun Jan 12 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.5-1
- Initial package
