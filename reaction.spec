%define _provides_exceptions ^renderer
%define _noautoprov ^renderer

%define		oname	Reaction

Name:		reaction
Version:	1.0
Release:	%mkrel 1
Summary:	First-person shooter based on modified Quake 3 engine
Group:		Games/Arcade
License:	GPLv2
URL:		http://rq3.com/
Source0:	http://download.rq3.com/%{oname}-%{version}-source.tar.gz
Patch0:		reaction-1.0-mdv-custom.patch
BuildRequires:	jpeg-devel
BuildRequires:	mesagl-devel
BuildRequires:	SDL-devel
BuildRequires:	zlib-devel
BuildRequires:	pkgconfig(ogg)
BuildRequires:	pkgconfig(speex)
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	pkgconfig(vorbisfile)
BuildRequires:	imagemagick
Requires:	%{name}-data

%description
Reaction was originally called Reaction Quake 3 which was a "total conversion
mod" for Quake III Arena based on action and realism with a specific emphasis
on action over realism. Reaction is a port of the classic Action Quake 2 (AQ2)
mod. AQ2 still enjoyed great popularity in online gaming even 4 years after it
was initially released and on an "obsolete" game engine as well. Many people
attribute this lasting popularity to both the unique gameplay and the AQ2
community. At the time Reaction Quake 3 was first released, AQ2 was still more
popular than other Q3 realism mods and any other Quake 2 and Quake/QuakeWorld
mods.

Reaction Quake 3 aimed to bring the gameplay of AQ2 to a new, more modern game
engine. This mod is made by AQ2 fans and players specifically for those who
love the fast and furious AQ2 gameplay and also to hopefully expose a new
generation of players to this unique gameplay.

Reaction has already surpassed many facets of the last official release of
Action Quake 2, 1.52, and is catching up to some of the latest AQ2 variants.
Considering that AQ2 has had over 4 years of development time and the bulk
Reaction's teamplay, matchmode, and bot development was done in less than
6 months, this is a pretty exciting project. What started out as a project by
part of the AQ2 community who wanted someone to make "Action Quake 3" has
turned into a well-received and pretty solid and fun standalone game.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
%__mkdir_p ~/tmp
%make V=1

%install
%__rm -rf %{buildroot}

%__mkdir_p %{buildroot}%{_gamesbindir}
%__cp build/release-linux-*/%{oname}.* %{buildroot}%{_gamesbindir}/%{name}
%__cp build/release-linux-*/%{oname}ded.* %{buildroot}%{_gamesbindir}/%{name}-server

%__mkdir_p %{buildroot}%{_libdir}/%{name}
%__cp build/release-linux-*/*.so %{buildroot}%{_libdir}/%{name}/

%__mkdir_p %{buildroot}%{_gamesdatadir}/%{name}
pushd %{buildroot}%{_gamesdatadir}/%{name}
for N in %{buildroot}%{_libdir}/%{name}/*.so
do
%__ln_s %{_libdir}/%{name}/`basename $N` `basename $N`;
done
popd

# create and install icons
for N in 16 32 48 64 128; do convert %{oname}.png -scale ${N}x${N}! $N.png; done
%__install -D 16.png -m 644 %{buildroot}%{_iconsdir}/hicolor/16x16/apps/%{name}.png
%__install -D 32.png -m 644 %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{name}.png
%__install -D 48.png -m 644 %{buildroot}%{_iconsdir}/hicolor/48x48/apps/%{name}.png
%__install -D 64.png -m 644 %{buildroot}%{_iconsdir}/hicolor/64x64/apps/%{name}.png
%__install -D 128.png -m 644 %{buildroot}%{_iconsdir}/hicolor/128x128/apps/%{name}.png

# XDG menu entry
%__mkdir_p %{buildroot}%{_datadir}/applications
%__cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Type=Application
Name=%{oname}
Comment=First-person shooter
Icon=%{name}
Exec=%{_gamesbindir}/%{name}
Terminal=false
Categories=Game;ArcadeGame;
EOF

%clean
%__rm -rf %{buildroot}

%files
%doc COPYING.txt README README-Reaction id-readme.txt
%{_gamesbindir}/%{name}
%{_gamesbindir}/%{name}-server
%{_gamesdatadir}/%{name}
%{_libdir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png

