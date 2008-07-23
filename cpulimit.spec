%define name	cpulimit
%define version	1.1
%define release %mkrel 3

Name:		%name
Version:	%version
Release:	%release
Summary:	CPU Usage Limiter
URL:		http://cpulimit.sourceforge.net/
Source:		cpulimit-%{version}.tar.gz
License:	GPL
Group:		Monitoring
BuildRoot:	%{_tmppath}/%{name}-root
%description
cpulimit is a simple program that attempts to limit the cpu usage of a
process (expressed in percentage, not in cpu time). This is useful to
control batch jobs, when you don't want they eat too much cpu. It does
not act on the nice value or other scheduling priority stuff, but on
the real cpu usage. Also, it is able to adapt itself to the overall
system load, dynamically and quickly.

%prep
%setup -q

%build
%make

%install
%{__mkdir} -p $RPM_BUILD_ROOT%{_bindir}
%{__cp} -p %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
%{__rm} -Rf $RPM_BUILD_ROOT

%files
%{_bindir}/%{name}
