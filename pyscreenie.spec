# sitelib for noarch packages, sitearch for others (remove the unneeded one)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}

Name:           pyscreenie
Version:        1.9.4
Release:        1%{?dist}
Summary:        Python/Glade/GTK app to grab a timed screenshot
Group:          Applications/Utilities

License:        GPLv2
URL:            http://www.thelupine.com/pyscreenie
Source0:        pyscreenie-1.9.4.tar.gz

BuildArch:      noarch
BuildRequires:  python
Requires:       pygobject3, sqlite, pexpect

%description
pyscreenie is a simple Python/Glade/GTK application that presents the user
with a simple set of choices that will allow them to setup a schedule to 
take a screenshot of the main desktop

%prep
%setup -q


%build
# Remove CFLAGS=... for noarch packages (unneeded)
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

 
%files
%defattr(-,root,root,-)
/usr/bin/pyscreenie
/usr/bin/pyscreenie-scheduler
/usr/share/applications/pyscreenie.desktop
/usr/share/pyscreenie/pyscreenie.glade
/usr/share/pyscreenie/pyscreenie-logo.png
/usr/share/pyscreenie/pyscreenie-32x32.png
/usr/share/pyscreenie/pyscreenie-64x64.png
%doc README ChangeLog 
/usr/share/man/man1/pyscreenie.1.gz
# For noarch packages: sitelib
%{python_sitelib}/*


%changelog
* Sun Jun 22 2014 TheLupine <thelupine@gmail.com> - 1.9.4-1
- inital Fedora20 release

