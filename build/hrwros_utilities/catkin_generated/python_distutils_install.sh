#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/romo18/ros_projects/hrwros_ws/src/hrwros_utilities"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/romo18/ros_projects/hrwros_ws/install/lib/python2.7/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/romo18/ros_projects/hrwros_ws/install/lib/python2.7/dist-packages:/home/romo18/ros_projects/hrwros_ws/build/lib/python2.7/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/romo18/ros_projects/hrwros_ws/build" \
    "/usr/bin/python2" \
    "/home/romo18/ros_projects/hrwros_ws/src/hrwros_utilities/setup.py" \
     \
    build --build-base "/home/romo18/ros_projects/hrwros_ws/build/hrwros_utilities" \
    install \
    --root="${DESTDIR-/}" \
    --install-layout=deb --prefix="/home/romo18/ros_projects/hrwros_ws/install" --install-scripts="/home/romo18/ros_projects/hrwros_ws/install/bin"
