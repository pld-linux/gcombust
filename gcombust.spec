Summary:	gcombust is a GTK+ frontend for mkisofs and cdrecord
Summary(pl):	gcombust jest nakЁadk╠ na mkisofs i cdrecord napisan╠ z u©yciem Gtk+
Summary(ru):	gcombust - это GTK+ интерфейс к mkisofs и cdrecord
Summary(uk):	gcombust - це GTK+ ╕нтерфейс до mkisofs ╕ cdrecord
Name:		gcombust
Version:	0.1.52
Release:	6
License:	GPL
Group:		X11/Applications
Vendor:		Jonas Munsin <jmunsin@iki.fi>
Source0:	http://www.abo.fi/~jmunsin/gcombust/%{name}-%{version}.tar.gz
# Source0-md5:	2c2455f8fe91cddd7b87bf59916a39e8
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-home_etc.patch
Patch1:		%{name}-po.patch
Patch2:		%{name}-locale_names.patch
Icon:		gcombust.xpm
URL:		http://www.iki.fi/jmunsin/gcombust/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtk+-devel >= 1.2.0
Requires:	cdrecord
Requires:	cdrtools-mkisofs >= 1.10
Requires:	cdlabelgen >= 1.1.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gcombust is a gui for mkisofs and cdrecord Linux. It's written in C
and it uses the GTK+ widget set (currently it's been tested and used
only on Linux and X Window). gcombust is work in progress, the
current (development) release is to be considered beta software. That
means it hasn't been tested very well and that some parts of the code
isn't written.

%description -l pl
Gcombust jest graficznym interfejsem dla linuksowych programСw mkisofs
i cdrecord. ZostaЁ napisany w C i u©ywa zbioru widgetСw GTK+ (jak
dot╠d zostaЁ jedynie przetestowany na Linuksie i X Window). Gcombust
to praca w toku (WIP), za╤ bie©╠ca wersja (rozwojowa) ma status beta.
Oznacza to, ©e nie zostaЁa dobrze przetestowana i brakuje niektСrych
fragmentСw kodu.

%description -l ru
gcombust - это GUI для mkisofs и cdrecord. Он написан на C и
использует набор виджетов GTK+.

%description -l uk
gcombust - це GUI для mkisofs та cdrecord. В╕н написаний на C та
використову╓ наб╕р в╕джет╕в GTK+.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

mv -f po/{no,nb}.po
install %{SOURCE1} .

%build
rm -f missing
%{__gettextize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	Applicationsdir=%{_desktopdir}

install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%find_lang gcombust

%clean
rm -rf $RPM_BUILD_ROOT

%files -f gcombust.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README* THANKS
%attr(755,root,root) %{_bindir}/gcombust
%{_desktopdir}/gcombust.desktop
%{_pixmapsdir}/gcombust.png
