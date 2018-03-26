Name:           ros-kinetic-op3-head-control-module
Version:        0.2.0
Release:        0%{?dist}
Summary:        ROS op3_head_control_module package

Group:          Development/Libraries
License:        Apache 2.0
URL:            http://wiki.ros.org/op3_head_control_module
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       eigen3-devel
Requires:       ros-kinetic-cmake-modules
Requires:       ros-kinetic-robotis-controller-msgs
Requires:       ros-kinetic-robotis-device
Requires:       ros-kinetic-robotis-framework-common
Requires:       ros-kinetic-robotis-math
Requires:       ros-kinetic-roscpp
Requires:       ros-kinetic-sensor-msgs
Requires:       ros-kinetic-std-msgs
BuildRequires:  boost-devel
BuildRequires:  eigen3-devel
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-cmake-modules
BuildRequires:  ros-kinetic-robotis-controller-msgs
BuildRequires:  ros-kinetic-robotis-device
BuildRequires:  ros-kinetic-robotis-framework-common
BuildRequires:  ros-kinetic-robotis-math
BuildRequires:  ros-kinetic-roscpp
BuildRequires:  ros-kinetic-sensor-msgs
BuildRequires:  ros-kinetic-std-msgs

%description
The op3_head_control_module package

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Mon Mar 26 2018 Pyo <pyo@robotis.com> - 0.2.0-0
- Autogenerated by Bloom

* Tue Oct 31 2017 Pyo <pyo@robotis.com> - 0.1.1-0
- Autogenerated by Bloom

* Fri Oct 27 2017 Pyo <pyo@robotis.com> - 0.1.0-1
- Autogenerated by Bloom

* Fri Oct 27 2017 Pyo <pyo@robotis.com> - 0.1.0-0
- Autogenerated by Bloom

