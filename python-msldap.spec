%global pypi_name msldap

Name:           python-%{pypi_name}
Version:        0.2.10
Release:        1%{?dist}
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
%{python3_sitelib}/%{pypi_name}-%{version}-py*.egg-info/

%changelog
* Mon Mar 16 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.10-1
- Update to latest upstream release 0.2.10

* Tue Mar 03 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.7-1
- Update to latest upstream release 0.2.7

* Thu Jan 23 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.5-2
- Fix requirement (rhbz#1790355)

* Sun Jan 12 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.5-1
- Initial package
