%global         debug_package %{nil}
%global         __strip /bin/true
%global         _missing_build_ids_terminate_build 0
%global         _build_id_links none
%global         cuda_version 11.4

Name:           cuda-cusparselt
Version:        0.1.0.2
Release:        1%{?dist}
Summary:        CUDA Library for Sparse Matrix-Matrix Multiplication
License:        NVIDIA License
URL:            https://docs.nvidia.com/cuda/cusparselt/index.html

Source0:        https://developer.download.nvidia.com/compute/libcusparse-lt/0.1.0/local_installers/libcusparse_lt-linux-%{_arch}-%{version}.tar.gz

%description
NVIDIA cuSPARSELt is a high-performance CUDA library dedicated to general
matrix-matrix operations in which at least one operand is a sparse matrix.

The cuSPARSELt APIs allow flexibility in the algorithm/operation selection,
epilogue, and matrix characteristics, including memory layout, alignment, and
data types.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       cuda-devel%{?_isa} >= %{?epoch:%{epoch}:}%{cuda_version}

%description    devel
The %{name}-devel package contains libraries and header files for developing
applications that use cuSPARSELt.

%package        static
Summary:        Static libraries for %{name}
Requires:       %{name}-devel%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description    static
Static libraries for cuSPARSELt.

%prep
%autosetup -n libcusparse_lt

%build
# Nothing to build

%install
mkdir -p %{buildroot}%{_libdir}/
mkdir -p %{buildroot}%{_includedir}/cuda/

install -p -m0755 lib64/libcusparseLt.so* %{buildroot}%{_libdir}/
install -p -m0644 lib64/libcusparseLt_static.a %{buildroot}%{_libdir}/
install -p -m0644 include/cusparseLt.h %{buildroot}%{_includedir}/cuda/

%ldconfig_scriptlets

%files
%license LICENSE.txt
%{_libdir}/libcusparseLt.so.*

%files devel
%{_includedir}/cuda/cusparseLt.h
%{_libdir}/libcusparseLt.so

%files static
%{_libdir}/libcusparseLt_static.a

%changelog
* Wed Jul 28 2021 Simone Caronni <negativo17@gmail.com> - 0.1.0.2-1
- First build.
