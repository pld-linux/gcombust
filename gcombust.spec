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

%changelog
* Wed May 12 1999 Ryan Weaver <ryanw@infohwy.com>
  [gcombust-0.1.12-1]
- Version 0.1.12 May 12 1999
- now adds '' around audio files too (broke on filenames with spaces etc. before)
  note that the command generating is still buggy by design, it will brake on
  filenames containing ' and other special characters
- suport for fs= option (and CDR_FIFOSIZE)

* Mon Mar 29 1999 Ryan Weaver <ryanw@infohwy.com>
  [gcombust-0.1.11-1]
- Version 0.1.11 Mar 29 1999
- BUGFIXES:
- cd-rw info progressbar should print some more info now :)
  (untested, please send me some output from a cdrecord blank=...
  session if I didn't get it right this time either)
- NEWS:
- support for making bootable cds - it's maybe a bit clumsy though
- now requires gtk 1.2.x
- now requires cdlabelgen 1.1.3 (WYSIWYG attempt dumped in favor for
  more intelligent cdlabelgen :)
- small code reorganization and it doesn't build with gcc -g as default
  anymore (still a good idea to strip it though)
- load/save image/audio selections (audio selections only works with
  pure audio cd selections)

* Mon Mar 22 1999 Ryan Weaver <ryanw@infohwy.com>
  [gcombust-0.1.10-1]
- Version 0.1.10 Mar 19 1999
- BUGFIXES:
- now compiles with gtk 1.2.0 again, if you have gtk 1.2.0
  change the GCOM_GTK_VER in src/globals.h to 12 (default is
  gtk 1.0.x, with GCOM_GTK_VER set to 10) - gtk 1.0.x support
  will be dropped soon, I'm getting sick of testing against two
  different versions for every release

- Version 0.1.9 Mar 19 1999
- BUGFIXES:
- CDR_DEVICE=1,0 works
- added lot's of error checks in contractions.c
- small g_list bug fixed (hopefully)
- quotes volume IDs
- contractions.c: iso<->cdr close-mixup in p_open_r_err_in
- NEWS:
- prints out all unprocessed output from mkisofs/cdrecord
  to textboxes, added MB burned + fifo label
- blank=... for cd-rw (untested as I don't have a cd-rw drive)
- started on the menus
- printing labels using cdlabelgen 0.70
  (http://www.red-bean.com/~bwf/software/cdlabelgen/)
  the printwindow tries to match (WYSIWYG) what cdlabelgen can handle

* Mon Mar  8 1999 Ryan Weaver <ryanw@infohwy.com>
  [gcombust-0.1.8-1]
- Version 0.1.8 Mar 08 1999
- BUGFIXES:
- some systems had compilation problems (basename missing, and
  swab nameclash)
- fixed execl() problem that made gcombust quite useless on
  some systems (rh 5.1?)

* Thu Mar  4 1999 Ryan Weaver <ryanw@infohwy.com>
  [gcombust-0.1.7-1]
- Version 0.1.7 Mar 04 1999
- BUGFIXES:
- dao could only be used with audio cds
- try harder option would produce negative values sometimes
- NEWS:
- remade audio cd creation interface

* Fri Feb 26 1999 Ryan Weaver <ryanw@infohwy.com>
  [gcombust-0.1.6-1]
- Version 0.1.6 Feb 26 1999
- forgot to make cdrecord parsing and info window routines aware of audio cds
  in yesterdays release, fixed that
- added -swab and -dao option
- added (un)select all

* Thu Feb 25 1999 Ryan Weaver <ryanw@infohwy.com>
  [gcombust-0.1.5-1]
- Version 0.1.5 Feb 25 1999
- added option to make audio (CD-DA) or mixed mode cds
- fixed small bug leaving progresswindow open when trying to run cdrecord
  without root access and not using any image
- fixed gtk1.1.x problems

- Version 0.1.4 Feb 24 1999
- small layout changes to start burning button and stop button, added 6x button
- added a "try harder" option to the bin packing algoritm
- removed some unused code
- fixed a small bug that could crash gcombust if you had several
  "abort?" windows open

* Tue Feb 23 1999 Ryan Weaver <ryanw@infohwy.com>
  [gcombust-0.1.3-1]
- Initial RPM build.
