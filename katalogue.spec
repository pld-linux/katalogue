Summary:	An application for indexing your CDs/ZIPs etc
Summary(pl):	Program do katalogowania zawarto¶ci p³yt CD/zipów itp
Name:		katalogue
Version:	0.4
%define	_rc	rc1
Release:	0.%{_rc}.1
Epoch:		0
License:	GPL
Group:		X11/Applications/File
Source0:	http://katalogue.szluug.org/download/%{name}-%{version}.tar.gz
# Source0-md5:	61723af155b31a869e297bf5fd19130a
URL:		http://katalogue.szluug.org
BuildRequires:	kdelibs-devel >= 3.2
BuildRequires:	qt-devel >= 3.2
Requires:	qt >= 3.2
Requires:	kdelibs >= 3.2
Provides:	katalogue
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Katalogue 0.4 is an application for indexing your CDs/ZIPs etc.

%description -l pl
Katalogue 0.4 jest programem s³u¿±cym do kataloagowania zawarto¶ci dowolonego katalogu.

%prep
%setup -q -n %{name}-%{version} -a 0

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/*

$Log: katalogue.spec,v $
Revision 1.1  2005-03-15 14:50:08  spider
- init
- spec done by Maciej Kasprzyk
- cosmetics
