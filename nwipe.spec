Summary:	A secure disk eraser
Name:		nwipe
Version:	0.35
Release:	1
License:	GPLv2
Group:		File tools
URL:		https://github.com/martijnvanbrummelen/nwipe
Source0:	https://github.com/martijnvanbrummelen/nwipe/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(libconfig)
BuildRequires:	pkgconfig(libparted)
BuildRequires:	pkgconfig(ncurses)

Requires:	hdparm
# optional
# used to determine the bus type, i.e. ATA, USB etc
Recommends:	coreutils
# used to provides SMBIOS/DMI host data to stdout or the log file
Recommends:	dmidecode
# used to obtains serial number information for supported USB to IDE/SATA adapters
Recommends:	smartmontools

%description
nwipe is a program that will securely erase the entire contents of disks. It
can wipe a single drive or multiple disks simultaneously. It can operate as
both a command line tool without a GUI or with a ncurses GUI.

nwipe is a fork of the dwipe command originally used by Darik's Boot and Nuke
(DBAN). nwipe was created out of a need to run the DBAN dwipe command outside
of DBAN, in order to allow its use with any host distribution, thus giving better
hardware support.

%files
%license COPYING
%doc CHANGELOG.md README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*

#---------------------------------------------------------------------------

%prep
%autosetup -p1

%build
autoreconf -fiv
%configure
%make_build

%install
%make_install 

