Summary:	gcombust is a GTK+ frontend for mksisofs and cdrecord
Summary(pl):	gcombust jest nak��dk� na mksisofs and cdrecord nzpisan� z u�yciem Gtk+
Name:		gcombust
Version:	0.1.45
Release:	1
License:	GPL
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Vendor:		Jonas Munsin <jmunsin@iki.fi>
Source0:	http://www.abo.fi/~jmunsin/gcombust/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Patch1:		%{name}-home_etc.patch
Icon:		gcombust.xpm
URL:		http://www.iki.fi/jmunsin/gcombust/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtk+-devel >= 1.2.0
Requires:	cdrecord
Requires:	mkisofs >= 1.13
Requires:	cdlabelgen >= 1.1.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
gcombust is a gui for mkisofs and cdrecord Linux. It's written in C
and it uses the GTK+ widget set (currently it's been tested and used
only on Linux and X-Windows). gcombust is work in progress, the
current (development) release is to be considered beta software. That
means it hasn't been tested very well and that some parts of the code
isn't written.

%description -l pl
Gcombust jest graficznym interfejsem dla linuksowych program�w mkisofs
i cdrecord. Zosta� napisany w C i uzywa zbioru widget�w GTK+ (jak
dot�d zosta� jedynie przetestowany na Linuksie i X-Windows). Gcombust
to praca w toku (WIP), za� bie��ca wersja (rozwojowa) ma status beta.
Oznacza to, �e nie zosta�a dobrze przetestowana i brakuje niekt�rych
fragment�w kodu.

%prep
%setup -q
%patch1 -p1

install %{SOURCE1} .

%build
gettextize --copy --force
aclocal
autoconf
automake -a -c
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	Applicationsdir=%{_applnkdir}/Utilities/CD-RW

gzip -9nf AUTHORS ChangeLog NEWS README* THANKS

%find_lang gcombust

%clean
rm -rf $RPM_BUILD_ROOT

%files -f gcombust.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/gcombust
%{_applnkdir}/Utilities/CD-RW/gcombust.desktop
%{_pixmapsdir}/gcombust.xpm
