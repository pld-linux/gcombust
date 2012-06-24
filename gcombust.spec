Summary:	gcombust is a GTK+ frontend for mkisofs and cdrecord
Summary(pl):	gcombust jest nak�adk� na mkisofs i cdrecord napisan� z u�yciem Gtk+
Summary(ru):	gcombust - ��� GTK+ ��������� � mkisofs � cdrecord
Summary(uk):	gcombust - �� GTK+ ��������� �� mkisofs � cdrecord
Name:		gcombust
Version:	0.1.52
Release:	2
License:	GPL
Group:		X11/Applications
Vendor:		Jonas Munsin <jmunsin@iki.fi>
Source0:	http://www.abo.fi/~jmunsin/gcombust/%{name}-%{version}.tar.gz
# Source0-md5:	2c2455f8fe91cddd7b87bf59916a39e8
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch1:		%{name}-home_etc.patch
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
Gcombust jest graficznym interfejsem dla linuksowych program�w mkisofs
i cdrecord. Zosta� napisany w C i uzywa zbioru widget�w GTK+ (jak
dot�d zosta� jedynie przetestowany na Linuksie i X Window). Gcombust
to praca w toku (WIP), za� bie��ca wersja (rozwojowa) ma status beta.
Oznacza to, �e nie zosta�a dobrze przetestowana i brakuje niekt�rych
fragment�w kodu.

%description -l ru
gcombust - ��� GUI ��� mkisofs � cdrecord. �� ������� �� C �
���������� ����� �������� GTK+.

%description -l uk
gcombust - �� GUI ��� mkisofs �� cdrecord. ��� ��������� �� C ��
����������դ ��¦� צ���Ԧ� GTK+.

%prep
%setup -q
%patch1 -p1

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
	Applicationsdir=%{_applnkdir}/Utilities/CD-RW

install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%find_lang gcombust

%clean
rm -rf $RPM_BUILD_ROOT

%files -f gcombust.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README* THANKS
%attr(755,root,root) %{_bindir}/gcombust
%{_applnkdir}/Utilities/CD-RW/gcombust.desktop
%{_pixmapsdir}/gcombust.png
