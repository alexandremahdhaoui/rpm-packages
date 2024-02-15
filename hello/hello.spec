Name:           hello
Version:        2.10
Release:        0%\{?dist}
Summary:        Produces a familiar, friendly greeting

License:        GPL-3.0-or-later
URL:            https://www.gnu.org/software/hello/
Source:         http://ftp.gnu.org/gnu/hello/hello-%{version}.tar.gz

%description
The GNU Hello program produces a familiar, friendly greeting. Yes, this is
another implementation of the classic program that prints "Hello, world!" when
you run it.

%prep
%autosetup

%build
%configure
%make_build

%install
%make_install

%files

%changelog
%autochangelog
