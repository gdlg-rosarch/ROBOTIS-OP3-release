# Script generated with Bloom
pkgdesc="ROS - ROS packages for the robotis_op3 (meta package)"
url='http://wiki.ros.org/robotis_op3'

pkgname='ros-kinetic-robotis-op3'
pkgver='0.2.1_1'
pkgrel=1
arch=('any')
license=('Apache 2.0'
)

makedepends=('ros-kinetic-catkin'
)

depends=('ros-kinetic-cm-740-module'
'ros-kinetic-op3-action-module'
'ros-kinetic-op3-balance-control'
'ros-kinetic-op3-base-module'
'ros-kinetic-op3-direct-control-module'
'ros-kinetic-op3-head-control-module'
'ros-kinetic-op3-kinematics-dynamics'
'ros-kinetic-op3-localization'
'ros-kinetic-op3-manager'
'ros-kinetic-op3-online-walking-module'
'ros-kinetic-op3-walking-module'
'ros-kinetic-open-cr-module'
)

conflicts=()
replaces=()

_dir=robotis_op3
source=()
md5sums=()

prepare() {
    cp -R $startdir/robotis_op3 $srcdir/robotis_op3
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

