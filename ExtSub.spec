Summary:	Substract subtitles from VOBs.
Summary(pl):	Wyodrêbnij napisy z VOBów.
Name:		ExtSub
Version:	0.1
Release:	1
License:	GPL
Group:		Applications/Console
Source0:	http://sites.inka.de/risctaker/VOBSub/%{name}.tgz
URL:		http://sites.inka.de/risctaker/VOBSub/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%description -l pl

%prep
%setup -q -n %{name}
#-%{version}.orig -a 1
#%patch0 -p1

%build
%{__make}

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
