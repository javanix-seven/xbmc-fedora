Name: xbmc
Version: 13.0
Release: 1%{?dist}
Summary: XBMC is an award-winning free and open source (GPL) software media player

License: GPL	
Source0: xbmc-%{version}.tar.gz

Patch0:	 xbmc-13.0-fedora-cpluff.patch

BuildRequires: SDL-devel
BuildRequires: SDL-static
BuildRequires: SDL2-devel
BuildRequires: SDL2_image-devel
BuildRequires: SDL_Pango-devel
BuildRequires: SDL_gfx-devel
BuildRequires: SDL_image-devel
BuildRequires: SDL_mixer-devel
BuildRequires: SDL_net-devel
BuildRequires: SDL_sound-devel
BuildRequires: SDL_ttf-devel
BuildRequires: afpfs-ng-devel
BuildRequires: alsa-lib-devel
BuildRequires: autoconf
BuildRequires: autogen-libopts
BuildRequires: automake
BuildRequires: avahi-devel
BuildRequires: bluez-libs-devel
BuildRequires: boost-atomic
BuildRequires: boost-chrono
BuildRequires: boost-context
BuildRequires: boost-devel
BuildRequires: boost-filesystem
BuildRequires: boost-graph
BuildRequires: boost-iostreams
BuildRequires: boost-locale
BuildRequires: boost-math
BuildRequires: boost-program-options
BuildRequires: boost-python
BuildRequires: boost-random
BuildRequires: boost-regex
BuildRequires: boost-serialization
BuildRequires: boost-signals
BuildRequires: boost-test
BuildRequires: boost-timer
BuildRequires: boost-wave
BuildRequires: bzip2-devel
BuildRequires: cairo-devel
BuildRequires: cmake
BuildRequires: cpp
BuildRequires: dbus-devel
BuildRequires: doxygen
BuildRequires: enca-devel
BuildRequires: expat-devel
BuildRequires: faac-devel
BuildRequires: faad2-devel
BuildRequires: faad2-libs
BuildRequires: flac-devel
BuildRequires: fontconfig-devel
BuildRequires: freetype-devel
BuildRequires: fribidi-devel
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: gettext-common-devel
BuildRequires: gettext-devel
BuildRequires: git
BuildRequires: gl-manpages
BuildRequires: glew-devel
BuildRequires: glib2-devel
BuildRequires: glibc-devel
BuildRequires: glibc-headers
BuildRequires: gnutls-c++
BuildRequires: gnutls-devel
BuildRequires: gperf
BuildRequires: harfbuzz-devel
BuildRequires: jasper-devel
BuildRequires: java
BuildRequires: java-devel
BuildRequires: kernel-headers
BuildRequires: keyutils-libs-devel
BuildRequires: krb5-devel
BuildRequires: lame-devel
BuildRequires: lame-libs
BuildRequires: libGLEW
BuildRequires: libGLEWmx
BuildRequires: libICE-devel
BuildRequires: libSM-devel
BuildRequires: libX11-devel
BuildRequires: libXScrnSaver-devel
BuildRequires: libXau-devel
BuildRequires: libXdamage-devel
BuildRequires: libXext-devel
BuildRequires: libXfixes-devel
BuildRequires: libXft-devel
BuildRequires: libXi-devel
BuildRequires: libXinerama-devel
BuildRequires: libXmu-devel
BuildRequires: libXrandr-devel
BuildRequires: libXrender-devel
BuildRequires: libXt-devel
BuildRequires: libXtst-devel
BuildRequires: libXxf86vm-devel
BuildRequires: libass-devel
BuildRequires: libbluray-devel
BuildRequires: libcap-devel
BuildRequires: libcdio-devel
BuildRequires: libcom_err-devel
BuildRequires: libcrystalhd-devel
BuildRequires: libcurl-devel
BuildRequires: libdca-devel
BuildRequires: libdrm-devel
BuildRequires: libgcrypt-devel
BuildRequires: libgpg-error-devel
BuildRequires: libicu-devel
BuildRequires: libjpeg-turbo-devel
BuildRequires: libmad-devel
BuildRequires: libmicrohttpd-devel
BuildRequires: libmikmod
BuildRequires: libmms-devel
BuildRequires: libmodplug-devel
BuildRequires: libmp4v2
BuildRequires: libmpc
BuildRequires: libmpeg2-devel
BuildRequires: libogg-devel
BuildRequires: libplist-devel
BuildRequires: libpng-devel
BuildRequires: librtmp-devel
BuildRequires: libsamplerate-devel
BuildRequires: libselinux-devel
BuildRequires: libsepol-devel
BuildRequires: libsmbclient-devel
BuildRequires: libssh-devel
BuildRequires: libstdc++-devel
BuildRequires: libtasn1-devel
BuildRequires: libtiff-devel
BuildRequires: libtool
BuildRequires: libusb-devel
BuildRequires: libusbx-devel
BuildRequires: libva-devel
BuildRequires: libvdpau-devel
BuildRequires: libverto-devel
BuildRequires: libvorbis-devel
BuildRequires: libxcb-devel
BuildRequires: libxml2-devel
BuildRequires: lzma-sdk457
BuildRequires: lzo-devel
BuildRequires: lzo-minilzo
BuildRequires: m4
BuildRequires: mariadb
BuildRequires: mariadb-devel
BuildRequires: mariadb-libs
BuildRequires: mesa-libEGL-devel
BuildRequires: mesa-libGL-devel
BuildRequires: mesa-libGLES-devel
BuildRequires: mesa-libGLU-devel
BuildRequires: openssl-devel
BuildRequires: p11-kit-devel
BuildRequires: pango-devel
BuildRequires: patch
BuildRequires: pcre-devel
BuildRequires: perl-B-Lint
BuildRequires: perl-Business-ISBN
BuildRequires: perl-Business-ISBN-Data
BuildRequires: perl-CGI
BuildRequires: perl-CPAN
BuildRequires: perl-Class-ISA
BuildRequires: perl-Compress-Raw-Bzip2
BuildRequires: perl-Compress-Raw-Zlib
BuildRequires: perl-Data-Dumper
BuildRequires: perl-Digest
BuildRequires: perl-Digest-MD5
BuildRequires: perl-Digest-SHA
BuildRequires: perl-Encode-Locale
BuildRequires: perl-Error
BuildRequires: perl-ExtUtils-Install
BuildRequires: perl-ExtUtils-MakeMaker
BuildRequires: perl-ExtUtils-Manifest
BuildRequires: perl-ExtUtils-ParseXS
BuildRequires: perl-FCGI
BuildRequires: perl-File-CheckTree
BuildRequires: perl-File-Listing
BuildRequires: perl-Git
BuildRequires: perl-HTML-Parser
BuildRequires: perl-HTML-Tagset
BuildRequires: perl-HTTP-Cookies
BuildRequires: perl-HTTP-Daemon
BuildRequires: perl-HTTP-Date
BuildRequires: perl-HTTP-Message
BuildRequires: perl-HTTP-Negotiate
BuildRequires: perl-HTTP-Tiny
BuildRequires: perl-IO-Compress
BuildRequires: perl-IO-HTML
BuildRequires: perl-IO-Socket-IP
BuildRequires: perl-IO-Socket-SSL
BuildRequires: perl-LWP-MediaTypes
BuildRequires: perl-Locale-Codes
BuildRequires: perl-Module-Pluggable
BuildRequires: perl-Net-HTTP
BuildRequires: perl-Net-LibIDN
BuildRequires: perl-Net-SSLeay
BuildRequires: perl-Pod-Checker
BuildRequires: perl-Pod-LaTeX
BuildRequires: perl-Pod-Parser
BuildRequires: perl-Pod-Perldoc
BuildRequires: perl-Pod-Plainer
BuildRequires: perl-Pod-Usage
BuildRequires: perl-Sys-Syslog
BuildRequires: perl-TermReadKey
BuildRequires: perl-Test-Harness
BuildRequires: perl-Test-Simple
BuildRequires: perl-Text-ParseWords
BuildRequires: perl-Text-Soundex
BuildRequires: perl-Text-Unidecode
BuildRequires: perl-Thread-Queue
BuildRequires: perl-TimeDate
BuildRequires: perl-URI
BuildRequires: perl-WWW-RobotRules
BuildRequires: perl-XML-LibXML
BuildRequires: perl-XML-NamespaceSupport
BuildRequires: perl-XML-SAX
BuildRequires: perl-XML-SAX-Base
BuildRequires: perl-autodie
BuildRequires: perl-devel
BuildRequires: perl-libwww-perl
BuildRequires: perl-parent
BuildRequires: perl-podlators
BuildRequires: physfs
BuildRequires: pixman-devel
BuildRequires: python-devel
BuildRequires: redhat-lsb
BuildRequires: redhat-lsb-core
BuildRequires: redhat-lsb-cxx
BuildRequires: redhat-lsb-desktop
BuildRequires: redhat-lsb-languages
BuildRequires: redhat-lsb-printing
BuildRequires: redhat-lsb-submod-multimedia
BuildRequires: redhat-lsb-submod-security
BuildRequires: spax
BuildRequires: sqlite-devel
BuildRequires: swig
BuildRequires: sysconftool
BuildRequires: systemtap-sdt-devel
BuildRequires: taglib-devel
BuildRequires: tinyxml-devel
BuildRequires: tre-devel
BuildRequires: vala
BuildRequires: wavpack-devel
BuildRequires: xorg-x11-proto-devel
BuildRequires: xz-devel
BuildRequires: yajl-devel
BuildRequires: zlib-devel
BuildRequires: libxslt-devel
BuildRequires: yasm-devel
BuildRequires: nettle-devel
BuildRequires: /usr/bin/autopoint

%description
XBMC is an award-winning free and open source (GPL) software media player and entertainment hub that can be installed on Linux

%prep
%setup -q

# Patch configure file so that cpluff gets 'autogen'ed first.
%patch0 -p1

%build
%configure --disable-dvdcss --disable-afpclient --disable-mysql --disable-webserver --disable-optical-drive --disable-rsxs

make V=0 DESTDIR=$RPM_BUILD_ROOT

%install
make V=0 DESTDIR=$RPM_BUILD_ROOT install

%files
%exclude %{_prefix}/share/applications/xbmc.desktop
%exclude %{_prefix}/share/xsessions/XBMC.desktop

%{_bindir}/xbmc
%{_bindir}/xbmc-standalone

%dir %{_includedir}/xbmc
%{_includedir}/xbmc/*

%dir %{_libdir}/xbmc
%{_libdir}/xbmc/*

%dir %{_prefix}/share/doc/xbmc
%{_prefix}/share/doc/xbmc/*

%{_prefix}/share/icons/hicolor/256x256/apps/xbmc.png
%{_prefix}/share/icons/hicolor/48x48/apps/xbmc.png

%dir %{_prefix}/share/xbmc
%{_prefix}/share/xbmc/*

%changelog
* Sat Feb 08 2014 javanix.seven <javanix.seven@gmail.com> 13.0-1
- Initial working build.
