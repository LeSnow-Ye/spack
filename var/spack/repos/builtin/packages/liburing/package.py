# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class Liburing(AutotoolsPackage):
    """This is the io_uring library, liburing. liburing provides helpers
    to setup and teardown io_uring instances, and also a simplified interface
    for applications that don't need (or want) to deal with the full kernel
    side implementation."""

    homepage = "https://github.com/axboe/liburing"
    url = "https://github.com/axboe/liburing/archive/refs/tags/liburing-2.3.tar.gz"
    git = "https://github.com/axboe/liburing.git"

    license("LGPL-2.1-or-later OR MIT")

    version("master", branch="master")
    version("2.9", sha256="897b1153b55543e8b92a5a3eb9b906537a5fedcf8afaf241f8b8787940c79f8d")
    version("2.3", sha256="60b367dbdc6f2b0418a6e0cd203ee0049d9d629a36706fcf91dfb9428bae23c8")

    depends_on("c", type="build")
    depends_on("cxx", type="build")  # only for tests, built automatically.

    requires("platform=linux")
