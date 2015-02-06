%define _enable_debug_packages %{nil}
%define debug_package %{nil}
%define svnrel r35

Name:		cpulimit
Version:	1.1
Release:	9
Summary:	CPU Usage Limiter
URL:		http://cpulimit.sourceforge.net/
Source0:	cpulimit-%{version}.%{svnrel}.tar.gz
License:	GPLv2+
Group:		Monitoring

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
mkdir -p %{buildroot}%{_bindir}
cp -p %{name} %{buildroot}%{_bindir}/%{name}


%files
%doc README
%{_bindir}/%{name}

