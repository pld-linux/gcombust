%define	name	gcombust
%define	version	0.1.12
%define	release	1
%define	serial	1

Summary:	gcombust is a GTK+ frontend for mksisofs and cdrecord.
Name:		%{name}
Version:	%{version}
Release:	%{release}
Serial:		%{serial}
Copyright:	GPL
Group:		X11/Utilities
URL:		http://www.iki.fi/jmunsin/gcombust
Vendor:		Jonas Munsin <jmunsin@iki.fi>
Source:		%{name}-%{version}.tar.gz
Distribution:	Freshmeat RPMs
Requires:	gtk+ >= 1.2.0, cdrecord, mkisofs, cdlabelgen >= 1.1.3
Packager:	Ryan Weaver <ryanw@infohwy.com>
BuildRoot:	/tmp/%{name}-%{version}

%description
gcombust is a gui for mkisofs and cdrecord Linux. It's written
in C and it uses the GTK+ widget set (currently it's been tested
and used only on Linux and X-Windows). gcombust is work in progress,
the current (development) release is to be considered beta software.
That means it hasn't been tested very well and that some parts of
the code isn't written.

%prep
%setup -q
CFLAGS=$RPM_OPT_FLAGS \
./configure --prefix=/usr

%build
make

%install
if [ -e $RPM_BUILD_ROOT ]; then rm -rf $RPM_BUILD_ROOT; fi
mkdir -p $RPM_BUILD_ROOT/usr/bin
make prefix=$RPM_BUILD_ROOT/usr install-strip

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README README.irix THANKS
/usr/bin/gcombust
