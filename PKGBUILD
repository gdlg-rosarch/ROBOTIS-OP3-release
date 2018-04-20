# Script generated with Bloom
pkgdesc="ROS - The op3_manager package"
url='http://wiki.ros.org/op3_manager'

pkgname='ros-kinetic-op3-manager'
pkgver='0.2.1_1'
pkgrel=1
arch=('any')
license=('Apache 2.0'
)

makedepends=('ros-kinetic-catkin'
'ros-kinetic-cmake-modules'
'ros-kinetic-dynamixel-sdk'
'ros-kinetic-op3-action-module'
'ros-kinetic-op3-action-module-msgs'
'ros-kinetic-op3-balance-control'
'ros-kinetic-op3-base-module'
'ros-kinetic-op3-direct-control-module'
'ros-kinetic-op3-head-control-module'
'ros-kinetic-op3-kinematics-dynamics'
'ros-kinetic-op3-online-walking-module'
'ros-kinetic-op3-online-walking-module-msgs'
'ros-kinetic-op3-walking-module'
'ros-kinetic-op3-walking-module-msgs'
'ros-kinetic-open-cr-module'
'ros-kinetic-robotis-controller'
'ros-kinetic-robotis-controller-msgs'
'ros-kinetic-robotis-device'
'ros-kinetic-robotis-framework-common'
'ros-kinetic-robotis-math'
'ros-kinetic-roscpp'
)

depends=('ros-kinetic-cmake-modules'
'ros-kinetic-dynamixel-sdk'
'ros-kinetic-op3-action-module'
'ros-kinetic-op3-action-module-msgs'
'ros-kinetic-op3-balance-control'
'ros-kinetic-op3-base-module'
'ros-kinetic-op3-direct-control-module'
'ros-kinetic-op3-head-control-module'
'ros-kinetic-op3-kinematics-dynamics'
'ros-kinetic-op3-localization'
'ros-kinetic-op3-online-walking-module'
'ros-kinetic-op3-online-walking-module-msgs'
'ros-kinetic-op3-walking-module'
'ros-kinetic-op3-walking-module-msgs'
'ros-kinetic-open-cr-module'
'ros-kinetic-robotis-controller'
'ros-kinetic-robotis-controller-msgs'
'ros-kinetic-robotis-device'
'ros-kinetic-robotis-framework-common'
'ros-kinetic-robotis-math'
'ros-kinetic-roscpp'
)

conflicts=()
replaces=()

_dir=op3_manager
source=()
md5sums=()

prepare() {
    cp -R $startdir/op3_manager $srcdir/op3_manager
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

