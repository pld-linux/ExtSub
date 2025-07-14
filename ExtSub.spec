Summary:	Substract subtitles from VOBs
Summary(pl.UTF-8):	Wyodrębnianie napisów z VOBów
Name:		ExtSub
Version:	0.1
Release:	1
License:	GPL
Group:		Applications/Multimedia
Source0:	http://sites.inka.de/risctaker/VOBSub/%{name}.tgz
# Source0-md5:	430edb8011e4a921aae8a1769ac98f36
URL:		http://sites.inka.de/risctaker/VOBSub/
Patch0:		%{name}-flags.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Substract subtitles from VOBs.

%description -l pl.UTF-8
Wyodrębnianie napisów z VOBów.

%prep
%setup -q -n %{name}
%patch -P0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	FLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install ExtSub $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGELOG
%attr(755,root,root) %{_bindir}/*
