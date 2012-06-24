Summary:	A GUI tool to rename and tag MP3 and Ogg/Vorbis files
Summary(pl):	Graficzne narz�dzie do zmiany nazw i znacznik�w plik�w MP3 i Ogg/Vorbis
Name:		cantus_2
Version:	1.99.9
Release:	1
License:	GPL
Group:		X11/Applications/Sound
#Source0Download: http://www.debain.org/?session=&site=project&project=1&cat=downloads
Source0:	http://sam.homeunix.com/software.manicsadness.com-step4/releases/cantus_2/%{name}-%{version}-1.tar.gz
# Source0-md5:	d237af5e217aa13473b8a6b21b2c4d2f
URL:		http://www.debain.org/software/cantus
BuildRequires:	autoconf
#BuildRequires:	gnome-libs-devel >= 1.2.8
BuildRequires:	glib2-devel >= 2.2.0
BuildRequires:	gtk+2-devel >= 2:2.2.0
BuildRequires:	libglade2-devel
BuildRequires:	libogg-devel
BuildRequires:	libvorbis-devel
BuildRequires:	pkgconfig
BuildRequires:	gettext-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
cantus_2 is a suite to rename and tag MP3 and Ogg/Vorbis files. It is
free software, and distributed under the terms of the GPL. It was
written by sam (Samuel Abels, <sam@manicsadness.com>) and implemented
in C using the GTK+ 2.x.

Features:
- define rules for renaming, which you can proceed on a list of files
- mass renaming/tagging of MP3s
- define rules to apply on a queue of MP3 files
- dynamically tagging is implemented, that means, you can generate a
  tag out of the filename and/or directory name
- renaming of files through freedb
- a LOT more

%description -l pl
cantus_2 to zestaw narz�dzi do zmiany nazw i znacznik�w plik�w MP3 i
Ogg/Vorbis. Jest to wolnodost�pne oprogramowanie, rozpowszechniane
na licencji GPL. Zosta�o napisane przez sama (Samuela Abelsa,
<sam@manicsadness.com>) i zaimplementowany w C przy u�yciu GTK+ 2.x.

Mo�liwo�ci:
- definiowanie regu� zmiany nazw, do wykonania na li�cie plik�w
- masowa zmiana nazw i znakowanie plik�w MP3
- definiowanie regu� do wykonania na kolejce plik�w MP3
- zaimplementowane dynamiczne znakowanie, co oznacza, �e mo�na
  generowa� znaczniki na podstawie nazwy pliku i/lub katalogu
- zmiana nazw plik�w poprzez freedb
- WIELE wi�cej.

%prep
%setup -q -n cantus-2-%{version}

%build
#%%{__autoconf}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
	
rm -rf $RPM_BUILD_ROOT%{_prefix}/doc

%find_lang cantus-2

%clean
rm -rf $RPM_BUILD_ROOT

%files -f cantus-2.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/cantus-2
