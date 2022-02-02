%global         debug_package %{nil}
%global         __strip /bin/true
%global         _missing_build_ids_terminate_build 0
%global         _build_id_links none

Name:           libcusparselt
Version:        0.2.0.1
Release:        2%{?dist}
Summary:        CUDA Library for Sparse Matrix-Matrix Multiplication
License:        NVIDIA License
URL:            https://docs.nvidia.com/cuda/cusparselt/index.html
ExclusiveArch:  x86_64 aarch64

Source0:        https://developer.download.nvidia.com/compute/libcusparse-lt/0.2.0/local_installers/libcusparse_lt-linux-x86_64-%{version}.tar.gz
Source1:        https://developer.download.nvidia.com/compute/libcusparse-lt/0.2.0/local_installers/libcusparse_lt-linux-sbsa-%{version}.tar.gz

Conflicts:      %{name}0 < %{?epoch:%{epoch}:}%{version}-%{release}
# Drop in next release:
Provides:       cuda-cusparselt = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      cuda-cusparselt < %{?epoch:%{epoch}:}%{version}-%{release}

%description
NVIDIA cuSPARSELt is a high-performance CUDA library dedicated to general
matrix-matrix operations in which at least one operand is a sparse matrix.

The cuSPARSELt APIs allow flexibility in the algorithm/operation selection,
epilogue, and matrix characteristics, including memory layout, alignment, and
data types.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       cuda-devel%{?_isa}
Conflicts:      %{name}-devel < %{?epoch:%{epoch}:}%{version}-%{release}
# Drop in next release:
Provides:       cuda-cusparselt-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      cuda-cusparselt-devel < %{?epoch:%{epoch}:}%{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for developing
applications that use cuSPARSELt.

%package        static
Summary:        Static libraries for %{name}
Requires:       %{name}-devel%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
# Drop in next release:
Provides:       cuda-cusparselt-static = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      cuda-cusparselt-static < %{?epoch:%{epoch}:}%{version}-%{release}

%description    static
Static libraries for cuSPARSELt.

%prep
%ifarch x86_64
%setup -q -n libcusparse_lt
%endif

%ifarch aarch64
%setup -q -T -b 1 -n libcusparse_lt
%endif

%build
# Nothing to build

%install
mkdir -p %{buildroot}%{_libdir}/
mkdir -p %{buildroot}%{_includedir}/cuda/

install -p -m0755 lib64/libcusparseLt.so* %{buildroot}%{_libdir}/
install -p -m0644 lib64/libcusparseLt_static.a %{buildroot}%{_libdir}/
install -p -m0644 include/cusparseLt.h %{buildroot}%{_includedir}/

%ldconfig_scriptlets

%files
%license LICENSE.txt
%{_libdir}/libcusparseLt.so.*

%files devel
%{_includedir}/cusparseLt.h
%{_libdir}/libcusparseLt.so

%files static
%{_libdir}/libcusparseLt_static.a

%changelog
* Wed Feb 02 2022 Simone Caronni <negativo17@gmail.com> - 0.2.0.1-2
- Rename to libcusparselt.

* Tue Nov 02 2021 Simone Caronni <negativo17@gmail.com> - 0.2.0.1-1
- Update to 0.2.0.1.

* Wed Jul 28 2021 Simone Caronni <negativo17@gmail.com> - 0.1.0.2-1
- First build.
