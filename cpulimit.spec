%define name	cpulimit
%define version	1.1
%define release %mkrel 7
%define svnrel r35

Name:		%name
Version:	%version
Release:	%release
Summary:	CPU Usage Limiter
URL:		http://cpulimit.sourceforge.net/
Source:		cpulimit-%{version}.%{svnrel}.tar.gz
License:	GPLv2+
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
%{__rm} -Rf $RPM_BUILD_ROOT
%{__mkdir} -p $RPM_BUILD_ROOT%{_bindir}
%{__cp} -p %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
%{__rm} -Rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README
%{_bindir}/%{name}


%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 1.1-7mdv2011.0
+ Revision: 610170
- rebuild

* Wed Mar 10 2010 Michael Scherer <misc@mandriva.org> 1.1-6mdv2010.1
+ Revision: 517594
- add a README file in documentation

* Wed Nov 11 2009 Stéphane Téletchéa <steletch@mandriva.org> 1.1-5mdv2010.1
+ Revision: 464398
- Update to latest svn release, should fix segfault issues
- Fixed license tag

* Wed Sep 02 2009 Thierry Vignaud <tv@mandriva.org> 1.1-4mdv2010.0
+ Revision: 425249
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 1.1-3mdv2009.0
+ Revision: 243724
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.1-1mdv2008.1
+ Revision: 136345
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Jul 27 2007 Nicolas Vigier <nvigier@mandriva.com> 1.1-1mdv2008.0
+ Revision: 56274
- Import cpulimit

