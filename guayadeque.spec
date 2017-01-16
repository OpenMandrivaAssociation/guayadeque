%define _disable_lto 1

%define	gstapi	1.0

Summary:	Music Player with the aims to be intuitive, easy to use and fast
Name:		guayadeque
Version:	0.4.5
Release:	1
Group:		Sound
License:	GPLv2+
Url:		http://www.guayadeque.org
Source0:	http://github.com/anonbeat/guayadeque/release/%{name}-%{version}.tar.gz
#Patch1:		guayadeque-0.3.7-clang.patch

BuildRequires:	cmake 
BuildRequires:	desktop-file-utils
BuildRequires:	imagemagick
BuildRequires:	libmp4v2-devel
BuildRequires:	wxgtku3.0-devel
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(flac)
BuildRequires:	pkgconfig(gstreamer-%{gstapi})
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(libgpod-1.0)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	pkgconfig(taglib)
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
%setup -q
%apply_patches

# deleting Unity parts in guayadeque.desktop files
sed -i '18,38d' defconfig/guayadeque.desktop

%build
#remove build script conflicting with build/ folder used by cmake
rm -f ./build
%cmake
%make

%install
%makeinstall_std -C build

desktop-file-install \
	--vendor="" \
	--remove-category="Application" \
	--remove-key="Encoding" \
	--dir %{buildroot}%{_datadir}/applications \
	%{buildroot}%{_datadir}/applications/%{name}.desktop

%find_lang %{name}

%files -f %{name}.lang
%doc README changelog LICENSE
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/appdata/guayadeque.appdata.xml

