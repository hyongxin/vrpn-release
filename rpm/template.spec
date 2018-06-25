Name:           ros-melodic-vrpn
Version:        7.34.0
Release:        0%{?dist}
Summary:        ROS vrpn package

Group:          Development/Libraries
License:        BSL1.0
URL:            https://github.com/vrpn/vrpn/wiki
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-melodic-catkin
BuildRequires:  cmake

%description
The VRPN is a library and set of servers that interfaces with virtual-reality
systems, such as VICON, OptiTrack, and others.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/melodic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/melodic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/melodic

%changelog
* Mon Jun 25 2018 Paul Bovbel <paul@bovbel.com> - 7.34.0-0
- Autogenerated by Bloom

* Mon Jun 25 2018 Paul Bovbel <paul@bovbel.com> - 7.33.1-0
- Autogenerated by Bloom

