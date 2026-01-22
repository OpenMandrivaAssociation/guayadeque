%define _disable_lto 1

%define	gstapi	1.0

Summary:	Music Player with the aims to be intuitive, easy to use and fast
Name:		guayadeque
Version:	0.7.5
Release:	2
Group:		Sound
License:	GPLv2+
Url:		https://www.guayadeque.org
#Source0:	http://github.com/anonbeat/guayadeque/release/%{name}-%{version}.tar.gz
Source0:	https://github.com/thothix/guayadeque/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  make
BuildRequires:	cmake
BuildRequires:	gettext
BuildRequires:	desktop-file-utils
BuildRequires:	imagemagick
BuildRequires:	pkgconfig(mp4v2)
BuildRequires:	wxgtku3.2-devel
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(flac)
BuildRequires:	pkgconfig(gstreamer-%{gstapi})
BuildRequires:	pkgconfig(gstreamer-pbutils-1.0)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(libgpod-1.0)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	pkgconfig(wxsqlite3)
BuildRequires:	pkgconfig(taglib)
BuildRequires:	pkgconfig(jsoncpp)
Requires:	gstreamer%{gstapi}-plugins-base
Requires:	gstreamer%{gstapi}-plugins-good
Requires:	gstreamer%{gstapi}-plugins-ugly

%description
Guayadeque is a music management program designed for all music enthusiasts.
It is Full Featured Linux media player that can easily manage large collections
and uses the Gstreamer media framework. 
Some of Guayadeque Features

- Play mp3, ogg, flac, wma, wav, mpc, mp4, ape, ...
- Configurable cross fader engine
- Configurable Silence detector to avoid listening to silence between tracks
- Read and write tags in all supported formats
- Allow to catalog your music using labels
  Any track, artist or album can have as many labels you want
- Smart play mode that add tracks that fit your music taste
- Ability to download covers manually or automatically
- Suggest music using last.fm service
- Allow fast access to any music file by genre, artist, album, etc
- Play and Record shoutcast radios

%prep
%autosetup -p1

# Remove due conflicting with system build.
rm -f ./build*

%build
%cmake
%make_build

%install
%make_install -C build

#desktop-file-install \
#	--vendor="" \
#	--remove-category="Application" \
#	--remove-key="Encoding" \
#	--dir %{buildroot}%{_datadir}/applications \
#	%{buildroot}%{_datadir}/applications/%{name}.desktop

%find_lang %{name}

%files -f %{name}.lang
%doc README LICENSE
%{_bindir}/%{name}
%{_datadir}/applications/org.guayadeque.Guayadeque.desktop
%{_datadir}/metainfo/org.guayadeque.Guayadeque.metainfo.xml
%{_datadir}/guayadeque/
%{_iconsdir}/hicolor/*x*/apps/guayadeque.png
