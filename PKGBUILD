# Script generated with Bloom
pkgdesc="ROS - The op3_direct_control_module package"
url='http://wiki.ros.org/op3_direct_control_module'

pkgname='ros-kinetic-op3-direct-control-module'
pkgver='0.2.1_1'
pkgrel=1
arch=('any')
license=('Apache 2.0'
)

makedepends=('boost'
'eigen3'
'ros-kinetic-catkin'
'ros-kinetic-cmake-modules'
'ros-kinetic-op3-kinematics-dynamics'
'ros-kinetic-robotis-controller-msgs'
'ros-kinetic-robotis-device'
'ros-kinetic-robotis-framework-common'
'ros-kinetic-robotis-math'
'ros-kinetic-roscpp'
'ros-kinetic-sensor-msgs'
'ros-kinetic-std-msgs'
)

depends=('boost'
'eigen3'
'ros-kinetic-cmake-modules'
'ros-kinetic-op3-kinematics-dynamics'
'ros-kinetic-robotis-controller-msgs'
'ros-kinetic-robotis-device'
'ros-kinetic-robotis-framework-common'
'ros-kinetic-robotis-math'
'ros-kinetic-roscpp'
'ros-kinetic-sensor-msgs'
'ros-kinetic-std-msgs'
)

conflicts=()
replaces=()

_dir=op3_direct_control_module
source=()
md5sums=()

prepare() {
    cp -R $startdir/op3_direct_control_module $srcdir/op3_direct_control_module
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

