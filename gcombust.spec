Summary:	gcombust is a GTK+ frontend for mksisofs and cdrecord.
Name:		gcombust
Version:	0.1.25
Release:	1
Copyright:	GPL
Group:		Applications/Archiving
URL:		http://www.iki.fi/jmunsin/gcombust
Vendor:		Jonas Munsin <jmunsin@iki.fi>
Source:		%{name}-%{version}.tar.gz
Patch:		gcombust-opt.patch
Requires:	gtk+ >= 1.2.0, cdrecord, mkisofs, cdlabelgen >= 1.1.3
BuildRoot:	/tmp/%{name}-%{version}

%define		_prefix		/usr/X11R6
%define		_mandir		/usr/X11R6/man

%description
gcombust is a gui for mkisofs and cdrecord Linux. It's written
in C and it uses the GTK+ widget set (currently it's been tested
and used only on Linux and X-Windows). gcombust is work in progress,
the current (development) release is to be considered beta software.
That means it hasn't been tested very well and that some parts of
the code isn't written.

%prep
%setup -q
%patch -p0

%build
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/pixmaps}

make install-strip DESTDIR=$RPM_BUILD_ROOT

install %{name}.xpm $RPM_BUILD_ROOT%{_datadir}/pixmaps

gzip -9nf AUTHORS ChangeLog NEWS README* THANKS

%find_lang gcombust

%clean
rm -rf $RPM_BUILD_ROOT

%files -f gcombust.lang
%defattr(644,root,root,755)
%doc {AUTHORS,ChangeLog,NEWS,README*,THANKS}.gz
%attr(755,root,root) %{_bindir}/gcombust
%{_datadir}/pixmaps/gcombust.xpm
