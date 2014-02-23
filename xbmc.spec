Name: xbmc
Version: 13.0
Release: 1%{?dist}
Summary: XBMC is an award-winning free and open source (GPL) software media player

License: GPL	
Source0: xbmc.tar.gz

BuildRequires: /usr/bin/autopoint

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
BuildRequires: ffmpeg-devel
BuildRequires: ffmpeg
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
BuildRequires: libxslt-devel
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
BuildRequires: nasm
BuildRequires: nettle-devel
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
BuildRequires: yasm-devel
BuildRequires: zlib-devel

%description
XBMC is an award-winning free and open source (GPL) software media player and entertainment hub that can be installed on Linux

%prep
%setup -q -n %{name}

./bootstrap

./configure \
	    --prefix=%{_prefix} \
   	    --bindir=%{_bindir} \
	    --includedir=%{_includedir} \
	    --libdir=%{_libdir} \
	    --datadir=%{_datadir} \
	    --with-lirc-device=/var/run/lirc/lircd \
	    --enable-goom \
	    --enable-external-libraries \
	    --disable-ssh \
	    --disable-dvdcss \
	    --disable-optimizations \
	    --disable-debug \
	    --disable-mysql \
	    CPPFLAGS="-I/usr/include/ffmpeg" \
	    CFLAGS="$RPM_OPT_FLAGS -fPIC -I/usr/include/afpfs-ng/ -I/usr/include/ffmpeg -I/usr/include/samba-4.0/ -D__STDC_CONSTANT_MACROS" \
	    CXXFLAGS="$RPM_OPT_FLAGS -fPIC -I/usr/include/afpfs-ng/ -I/usr/include/ffmpeg -I/usr/include/samba-4.0/ -D__STDC_CONSTANT_MACROS" \
	    LDFLAGS="-fPIC" \
	    LIBS="$LIBS" \
	    ASFLAGS=-fPIC

%build
make -j2 V=0 DESTDIR=$RPM_BUILD_ROOT

%install
make -j2 V=0 DESTDIR=$RPM_BUILD_ROOT install

%files
%{_bindir}/xbmc
%{_bindir}/xbmc-standalone
%{_libdir}/xbmc/addons/library.xbmc.addon/libXBMC_addon-x86_64-linux.so
%{_libdir}/xbmc/addons/library.xbmc.gui/libXBMC_gui-x86_64-linux.so
%{_libdir}/xbmc/addons/library.xbmc.pvr/libXBMC_pvr-x86_64-linux.so
%{_libdir}/xbmc/addons/screensaver.rsxs.euphoria/Euphoria.xbs
%{_libdir}/xbmc/addons/screensaver.rsxs.plasma/Plasma.xbs
%{_libdir}/xbmc/addons/screensaver.rsxs.solarwinds/Solarwinds.xbs
%{_libdir}/xbmc/addons/visualization.glspectrum/opengl_spectrum.vis
%{_libdir}/xbmc/addons/visualization.goom/Goom.vis
%{_libdir}/xbmc/addons/visualization.projectm/projectM.vis
%{_libdir}/xbmc/addons/visualization.waveform/Waveform.vis
%{_libdir}/xbmc/system/ImageLib-x86_64-linux.so
%{_libdir}/xbmc/system/hdhomerun-x86_64-linux.so
%{_libdir}/xbmc/system/libcpluff-x86_64-linux.so
%{_libdir}/xbmc/system/libexif-x86_64-linux.so
%{_libdir}/xbmc/system/players/dvdplayer/libdvdnav-x86_64-linux.so
%{_libdir}/xbmc/system/players/paplayer/adpcm-x86_64-linux.so
%{_libdir}/xbmc/system/players/paplayer/libsidplay2-x86_64-linux.so
%{_libdir}/xbmc/system/players/paplayer/nosefart-x86_64-linux.so
%{_libdir}/xbmc/system/players/paplayer/stsoundlibrary-x86_64-linux.so
%{_libdir}/xbmc/system/players/paplayer/timidity-x86_64-linux.so
%{_libdir}/xbmc/system/players/paplayer/vgmstream-x86_64-linux.so
%{_libdir}/xbmc/xbmc-xrandr
%{_libdir}/xbmc/xbmc.bin
%{_datarootdir}/applications/xbmc.desktop
%{_datarootdir}/doc/xbmc/LICENSE.GPL
%{_datarootdir}/doc/xbmc/README.linux
%{_datarootdir}/doc/xbmc/copying.txt
%{_datarootdir}/icons/hicolor/256x256/apps/xbmc.png
%{_datarootdir}/icons/hicolor/48x48/apps/xbmc.png
%{_datarootdir}/xbmc/*
%{_datarootdir}/xsessions/XBMC.desktop

%changelog
* Sat Feb 08 2014 javanix.seven <javanix.seven@gmail.com> 13.0-1
- Initial working build.
