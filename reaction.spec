%if %{_use_internal_dependency_generator}
%define _noautoprov ^renderer(.*)
%else
%define _provides_exceptions ^renderer
%endif

%define		oname	Reaction

Name:		reaction
Version:	1.0
Release:	3
Summary:	First-person shooter based on modified Quake 3 engine
Group:		Games/Arcade
License:	GPLv2
URL:		http://rq3.com/
Source0:	http://download.rq3.com/%{oname}-%{version}-source.tar.gz
Patch0:		reaction-1.0-mdv-custom.patch
BuildRequires:	jpeg-devel
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(zlib)
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
mkdir -p ~/tmp
%make V=1

%install
mkdir -p %{buildroot}%{_gamesbindir}
cp build/release-linux-*/%{oname}.* %{buildroot}%{_gamesbindir}/%{name}
cp build/release-linux-*/%{oname}ded.* %{buildroot}%{_gamesbindir}/%{name}-server

mkdir -p %{buildroot}%{_libdir}/%{name}
cp build/release-linux-*/*.so %{buildroot}%{_libdir}/%{name}/

mkdir -p %{buildroot}%{_gamesdatadir}/%{name}
pushd %{buildroot}%{_gamesdatadir}/%{name}
for N in %{buildroot}%{_libdir}/%{name}/*.so
do
ln -s %{_libdir}/%{name}/`basename $N` `basename $N`;
done
popd

# create and install icons
for N in 16 32 48 64 128; do convert %{oname}.png -scale ${N}x${N}! $N.png; done
install -D 16.png -m 644 %{buildroot}%{_iconsdir}/hicolor/16x16/apps/%{name}.png
install -D 32.png -m 644 %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{name}.png
install -D 48.png -m 644 %{buildroot}%{_iconsdir}/hicolor/48x48/apps/%{name}.png
install -D 64.png -m 644 %{buildroot}%{_iconsdir}/hicolor/64x64/apps/%{name}.png
install -D 128.png -m 644 %{buildroot}%{_iconsdir}/hicolor/128x128/apps/%{name}.png

# XDG menu entry
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Type=Application
Name=%{oname}
Comment=First-person shooter
Icon=%{name}
Exec=%{_gamesbindir}/%{name}
Terminal=false
Categories=Game;ArcadeGame;
EOF

%files
%doc COPYING.txt README README-Reaction id-readme.txt
%{_gamesbindir}/%{name}
%{_gamesbindir}/%{name}-server
%{_gamesdatadir}/%{name}
%{_libdir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png



%changelog
* Tue Apr 03 2012 Andrey Bondrov <abondrov@mandriva.org> 1.0-1mdv2011.0
+ Revision: 788912
- Create missing ~/tmp at build time to fix build in 2011
- Use verbose build

* Mon Apr 02 2012 Andrey Bondrov <abondrov@mandriva.org> 1.0-1
+ Revision: 788807
- imported package reaction

