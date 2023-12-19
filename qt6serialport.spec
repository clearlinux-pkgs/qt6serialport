#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v3
# autospec commit: c1050fe
#
Name     : qt6serialport
Version  : 6.6.1
Release  : 5
URL      : https://download.qt.io/official_releases/qt/6.6/6.6.1/submodules/qtserialport-everywhere-src-6.6.1.tar.xz
Source0  : https://download.qt.io/official_releases/qt/6.6/6.6.1/submodules/qtserialport-everywhere-src-6.6.1.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause GFDL-1.3 GPL-2.0 GPL-3.0 LGPL-3.0
Requires: qt6serialport-lib = %{version}-%{release}
Requires: qt6serialport-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : mesa-dev
BuildRequires : pkgconfig(libudev)
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
No detailed description available

%package dev
Summary: dev components for the qt6serialport package.
Group: Development
Requires: qt6serialport-lib = %{version}-%{release}
Provides: qt6serialport-devel = %{version}-%{release}
Requires: qt6serialport = %{version}-%{release}

%description dev
dev components for the qt6serialport package.


%package lib
Summary: lib components for the qt6serialport package.
Group: Libraries
Requires: qt6serialport-license = %{version}-%{release}

%description lib
lib components for the qt6serialport package.


%package license
Summary: license components for the qt6serialport package.
Group: Default

%description license
license components for the qt6serialport package.


%prep
%setup -q -n qtserialport-everywhere-src-6.6.1
cd %{_builddir}/qtserialport-everywhere-src-6.6.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1703025909
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
%cmake ..
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1703025909
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/qt6serialport
cp %{_builddir}/qtserialport-everywhere-src-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/qt6serialport/b073f11f0c81a95ab5e32aa6b5d23a5955a95274 || :
cp %{_builddir}/qtserialport-everywhere-src-%{version}/LICENSES/GFDL-1.3-no-invariants-only.txt %{buildroot}/usr/share/package-licenses/qt6serialport/715f995f11805ee85601834220c43b082f457ea3 || :
cp %{_builddir}/qtserialport-everywhere-src-%{version}/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/qt6serialport/4cc77b90af91e615a64ae04893fdffa7939db84c || :
cp %{_builddir}/qtserialport-everywhere-src-%{version}/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/qt6serialport/8624bcdae55baeef00cd11d5dfcfa60f68710a02 || :
cp %{_builddir}/qtserialport-everywhere-src-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/qt6serialport/f45ee1c765646813b442ca58de72e20a64a7ddba || :
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)
/usr/lib64/qt6/metatypes/qt6serialport_relwithdebinfo_metatypes.json
/usr/lib64/qt6/mkspecs/modules/qt_lib_serialport.pri
/usr/lib64/qt6/mkspecs/modules/qt_lib_serialport_private.pri
/usr/lib64/qt6/modules/SerialPort.json

%files dev
%defattr(-,root,root,-)
/usr/include/QtSerialPort/6.6.1/QtSerialPort/private/qserialport_p.h
/usr/include/QtSerialPort/6.6.1/QtSerialPort/private/qserialportinfo_p.h
/usr/include/QtSerialPort/6.6.1/QtSerialPort/private/qtserialport-config_p.h
/usr/include/QtSerialPort/QSerialPort
/usr/include/QtSerialPort/QSerialPortInfo
/usr/include/QtSerialPort/QtSerialPort
/usr/include/QtSerialPort/QtSerialPortDepends
/usr/include/QtSerialPort/QtSerialPortVersion
/usr/include/QtSerialPort/qserialport.h
/usr/include/QtSerialPort/qserialportglobal.h
/usr/include/QtSerialPort/qserialportinfo.h
/usr/include/QtSerialPort/qtserialport-config.h
/usr/include/QtSerialPort/qtserialportexports.h
/usr/include/QtSerialPort/qtserialportversion.h
/usr/lib64/cmake/Qt6BuildInternals/StandaloneTests/QtSerialPortTestsConfig.cmake
/usr/lib64/cmake/Qt6SerialPort/Qt6SerialPortAdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6SerialPort/Qt6SerialPortConfig.cmake
/usr/lib64/cmake/Qt6SerialPort/Qt6SerialPortConfigVersion.cmake
/usr/lib64/cmake/Qt6SerialPort/Qt6SerialPortConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6SerialPort/Qt6SerialPortDependencies.cmake
/usr/lib64/cmake/Qt6SerialPort/Qt6SerialPortTargets-relwithdebinfo.cmake
/usr/lib64/cmake/Qt6SerialPort/Qt6SerialPortTargets.cmake
/usr/lib64/cmake/Qt6SerialPort/Qt6SerialPortVersionlessTargets.cmake
/usr/lib64/libQt6SerialPort.prl
/usr/lib64/libQt6SerialPort.so
/usr/lib64/pkgconfig/Qt6SerialPort.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libQt6SerialPort.so.6
/usr/lib64/libQt6SerialPort.so.6.6.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/qt6serialport/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/qt6serialport/715f995f11805ee85601834220c43b082f457ea3
/usr/share/package-licenses/qt6serialport/8624bcdae55baeef00cd11d5dfcfa60f68710a02
/usr/share/package-licenses/qt6serialport/b073f11f0c81a95ab5e32aa6b5d23a5955a95274
/usr/share/package-licenses/qt6serialport/f45ee1c765646813b442ca58de72e20a64a7ddba
