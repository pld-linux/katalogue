%define	_rc	rc1
Summary:	An application for indexing your CDs/ZIPs etc
Summary(pl):	Program do katalogowania zawarto�ci p�yt CD/zip�w itp
Name:		katalogue
Version:	0.4
Release:	0.%{_rc}.3
Epoch:		0
License:	GPL
Group:		Applications/Archiving
Source0:	http://katalogue.szluug.org/download/%{name}-%{version}.tar.gz
# Source0-md5:	61723af155b31a869e297bf5fd19130a
Source1:	%{name}.desktop
URL:		http://katalogue.szluug.org
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 3.2
BuildRequires:	qt-devel >= 3.2
Requires:	kdelibs >= 3.2
Requires:	qt >= 3.2
Provides:	katalogue
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Katalogue 0.4 is an application for indexing your CDs/ZIPs etc.

%description -l pl
Katalogue 0.4 jest programem s�u��cym do katalogowania zawarto�ci
no�nik�w CD/ZIP/itp.

%prep
%setup -q
install %{SOURCE1} src

%build
cp -f /usr/share/automake/config.* admin
%configure \
	--with-qt-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	shelldesktopdir=%{_desktopdir}

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*.desktop
%{_iconsdir}/*/*/apps/%{name}.png
%{_datadir}/apps/%{name}
