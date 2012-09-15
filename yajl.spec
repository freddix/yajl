Summary:	Yet Another JSON Library
Name:		yajl
Version:	2.0.4
Release:	1
License:	BSD
Group:		Libraries
Source:		http://github.com/lloyd/yajl/tarball/%{version}
URL:		http://lloyd.github.com/yajl/
BuildRequires:	cmake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		builddirname	$(tar tf %{SOURCE0} | sed 1q)

%description
YAJL (Yet Another JSON Library) is a JSON parsing library written
in C.

%package devel
Summary:	Header files for YAJL library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for YAJL library.

%prep
%setup -qc
cd %{builddirname}
sed -i -e 's| share/pkgconfig| %{_pkgconfigdir}|' src/CMakeLists.txt

%build
cd %{builddirname}
install -d build
cd build
%cmake ..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
cd %{builddirname}

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/json_reformat
%attr(755,root,root) %{_bindir}/json_verify
%attr(755,root,root) %ghost %{_libdir}/libyajl.so.2
%attr(755,root,root) %{_libdir}/libyajl.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libyajl.so
%{_includedir}/yajl
%{_pkgconfigdir}/*.pc

