%{?mingw_package_header}

%global name1 mpfr

Summary:        MinGW C library for multiple-precision floating-point computations
Name:           mingw-%{name1}
Version:        3.1.5
Release:        2%{?dist}
URL:            http://www.mpfr.org/
Source0:        http://www.mpfr.org/mpfr-%{version}/%{name1}-%{version}.tar.xz
# GFDL  (mpfr.texi, mpfr.info and fdl.texi)
License:        LGPLv3+ and GPLv3+ and GFDL
Group:          System Environment/Libraries
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-gcc
BuildRequires:  mingw32-gmp
BuildRequires:  mingw64-gmp
BuildArch:      noarch

%description
The MPFR library is a C library for multiple-precision floating-point
computations with "correct rounding". The MPFR is efficient and 
also has a well-defined semantics. It copies the good ideas from the 
ANSI/IEEE-754 standard for double-precision floating-point arithmetic 
(53-bit mantissa). MPFR is based on the GMP multiple-precision library.

# Mingw32
%package -n mingw32-%{name1}
Summary:        %{summary}

%description -n mingw32-%{name1}
The MPFR library is a C library for multiple-precision floating-point
computations with "correct rounding". The MPFR is efficient and 
also has a well-defined semantics. It copies the good ideas from the 
ANSI/IEEE-754 standard for double-precision floating-point arithmetic 
(53-bit mantissa). MPFR is based on the GMP multiple-precision library.

This package contains cross-compiled libraries and development tools
for Windows.

# Mingw64
%package -n mingw64-%{name1}
Summary:        %{summary}

%description -n mingw64-%{name1}
The MPFR library is a C library for multiple-precision floating-point
computations with "correct rounding". The MPFR is efficient and 
also has a well-defined semantics. It copies the good ideas from the 
ANSI/IEEE-754 standard for double-precision floating-point arithmetic 
(53-bit mantissa). MPFR is based on the GMP multiple-precision library.

This package contains cross-compiled libraries and development tools
for Windows.

%{?mingw_debug_package}

%prep
%setup -q -n %{name1}-%{version}

%build
%mingw_configure --disable-assert --disable-static --enable-shared
%mingw_make %{?_smp_mflags}

%install
%mingw_make install DESTDIR=$RPM_BUILD_ROOT
rm -rf $RPM_BUILD_ROOT%{mingw32_datadir}
rm -rf $RPM_BUILD_ROOT%{mingw64_datadir}
rm -rf $RPM_BUILD_ROOT%{mingw32_libdir}/*.la
rm -rf $RPM_BUILD_ROOT%{mingw64_libdir}/*.la

%files -n mingw32-%{name1}
%doc COPYING COPYING.LESSER NEWS README
%{mingw32_bindir}/libmpfr-4.dll
%{mingw32_libdir}/libmpfr.dll.a
%{mingw32_includedir}/*.h

%files -n mingw64-%{name1}
%doc COPYING COPYING.LESSER NEWS README
%{mingw64_bindir}/libmpfr-4.dll
%{mingw64_libdir}/libmpfr.dll.a
%{mingw64_includedir}/*.h

%changelog
* Thu Feb 02 2017 Jajauma's Packages <jajauma@yandex.ru> - 3.1.5-2
- Rebuild with GCC 5.4.0

* Tue Nov 01 2016 Thomas Sailer <t.sailer@alumni.ethz.ch> - 3.1.5-1
- update to 3.1.5

* Mon Mar 07 2016 Thomas Sailer <t.sailer@alumni.ethz.ch> - 3.1.4-1
- update to 3.1.4

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jul 02 2015 Thomas Sailer <t.sailer@alumni.ethz.ch> - 3.1.3-1
- update to 3.1.3

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Nov 18 2013 Thomas Sailer <t.sailer@alumni.ethz.ch> - 3.1.2-1
- update to 3.1.2

* Tue Sep 11 2012 Thomas Sailer <t.sailer@alumni.ethz.ch> - 3.1.1-3
- remove requires

* Tue Sep  4 2012 Thomas Sailer <t.sailer@alumni.ethz.ch> - 3.1.1-2
- change name macro name, changed group, removed sections not necessary for recent rpm

* Sat Aug 25 2012 Thomas Sailer <t.sailer@alumni.ethz.ch> - 3.1.1-1
- create from native spec

