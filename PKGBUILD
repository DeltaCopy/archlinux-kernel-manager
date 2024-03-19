# Maintainer: DeltaCopy (fennec)
pkgname=archlinux-kernel-manager
destname="/usr"
licensedir="/usr/share/archlinux-kernel-manager/licenses/"
pkgver=1.0.0
pkgrel=1
pkgdesc="Arch Linux Kernel Manager - Add/Remove Linux kernels"
arch=('x86_64')
url="https://github.com/DeltaCopy/${pkgname}"
license=('GPL3')
depends=('python-gobject' 'polkit-gnome' 'python-requests' 'python-tomlkit')
makedepends=('git')
options=(!strip !emptydirs)
source=("${pkgname}::git+${url}")
sha256sums=('SKIP')
package() {
	install -dm755 ${pkgdir}${_licensedir}${_pkgname}
	install -m644  ${srcdir}/${pkgname}/LICENSE ${pkgdir}${_licensedir}${_pkgname}
    sed -i -e s/'${app_version}'/$pkgver/ $srcdir/${pkgname}/usr/share/${pkgname}/archlinux-kernel-manager.py
	cp -r ${srcdir}/${pkgname}/${destname} ${pkgdir}
}
