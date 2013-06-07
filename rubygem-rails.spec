# Generated from rails-1.2.5.gem by gem2rpm -*- rpm-spec -*-
%global gemname rails

%global gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%global geminstdir %{gemdir}/gems/%{gemname}-%{version}

%global rubyabi 1.8

Summary: Web-application framework
Name: rubygem-%{gemname}
Epoch: 1
Version: 3.2.13
Release: 1%{?dist}
Group: Development/Languages
License: MIT
URL: http://www.rubyonrails.org
Source0: http://rubygems.org/downloads/rails-%{version}.gem
Requires: ruby(rubygems) >= 1.3.4
Requires: rubygem(activesupport) = %{version}
Requires: rubygem(activerecord) = %{version}
Requires: rubygem(actionpack) = %{version}
Requires: rubygem(actionmailer) = %{version}
Requires: rubygem(activeresource) = %{version}
Requires: rubygem(railties) = %{version}
Requires: rubygem(bundler) >= 1.0
Requires: ruby(abi) = %{rubyabi}

BuildRequires: rubygems

BuildArch: noarch
Provides: rubygem(%{gemname}) = %{version}

%description
Rails is a framework for building web-application using CGI, FCGI, mod_ruby,
or WEBrick on top of either MySQL, PostgreSQL, SQLite, DB2, SQL Server, or
Oracle with eRuby- or Builder-based templates.


%prep

%build

%install
mkdir -p %{buildroot}%{gemdir}
gem install --local --install-dir %{buildroot}%{gemdir} \
            --bindir %{buildroot}%{_bindir} \
            -V --no-rdoc --no-ri \
            --force %{SOURCE0}

# Remove backup files
find %{buildroot}/%{geminstdir} -type f -name "*~" -delete

# Don't delete zero-length files (bug 496480)
#find %{buildroot}/%{geminstdir} -type f -size 0c -exec rm -rvf {} \;

# Fix anything executable that does not have a shebang
for file in `find %{buildroot}/%{geminstdir} -type f -perm /a+x`; do
    [ -z "`head -n 1 $file | grep \"^#!/\"`" ] && chmod -v 644 $file
done

# For sure...
find %{buildroot} -name \*.gem | xargs chmod 0644

# Find files with a shebang that do not have executable permissions
for file in `find %{buildroot}/%{geminstdir} -type f ! -perm /a+x -name "*.rb"`; do
    [ ! -z "`head -n 1 $file | grep \"^#!/\"`" ] && chmod -v 755 $file
done

# Find files that have non-standard-executable-perm
find %{buildroot}/%{geminstdir} -type f -perm /g+wx -exec chmod -v g-w {} \;

# Find files that are not readable
find %{buildroot}/%{geminstdir} -type f ! -perm /go+r -exec chmod -v go+r {} \;

%files
%defattr(-, root, root, -)
%dir %{geminstdir}
%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec

#_mx %{geminstdir}/bin
#_mx %{_bindir}/rails

%changelog
* Fri Jun 07 2013 Sergey Mihailov <sergey.mihailov@gmail.com> - 3.2.13-1
- Update release

* Tue Jul 17 2012 Miroslav Suchý <msuchy@redhat.com> 3.0.10-4
- upgrading to rubygem-rails 3.0.10 (msuchy@redhat.com)

* Tue Jul 17 2012 Miroslav Suchý <msuchy@redhat.com> 3.0.3-3
- downgrade rail to 3.0.3

* Fri Jun 29 2012 Miroslav Suchý <msuchy@redhat.com> 3.0.10-2
- rebuild

* Mon Aug 22 2011 Vít Ondruch <vondruch@redhat.com> - 1:3.0.10-1
- Update to Rails 3.0.10

* Thu Jul 07 2011 Vít Ondruch <vondruch@redhat.com> - 1:3.0.9-1
- Update to Rails 3.0.9

* Tue Mar 29 2011 Vít Ondruch <vondruch@redhat.com> - 1:3.0.5-2
- Cleanup

* Tue Mar 29 2011 Vít Ondruch <vondruch@redhat.com> - 1:3.0.5-1
- Updated to Rails 3.0.5

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 10 2011 Mohammed Morsi <mmorsi@redhat.com> - 1:3.0.3-1
- Update to rails 3

* Mon Aug 09 2010 Mohammed Morsi <mmorsi@redhat.com> - 1:2.3.8-1
- Update to 2.3.8

* Thu Jan 28 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1:2.3.5-1
- Update to 2.3.5

* Wed Oct  7 2009 David Lutterkort <lutter@redhat.com> - 1:2.3.4-2
- Bump Epoch to ensure upgrade path from F-11

* Sun Sep 20 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.3.4-1
- Update to 2.3.4

* Fri Jul 31 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.3.3-2
- Restore some changes

* Sun Jul 26 2009 Jeroen van Meeuwen <j.van.meeuwen@ogd.nl> - 2.3.3-1
- New upstream version

* Wed Jul 24 2009 Scott Seago <sseago@redhat.com> - 2.3.2-3
- Remove the 'delete zero length files' bit, as some of these are needed.

* Wed May  6 2009 David Lutterkort <lutter@redhat.com> - 2.3.2-2
- Fix replacement of shebang lines; broke scripts/generate (bz 496480)

* Mon Mar 16 2009 Jeroen van Meeuwen <j.van.meeuwen@ogd.nl> - 2.3.2-1
- New upstream version

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Dec 23 2008 David Lutterkort <lutter@redhat.com> - 2.2.2-1
- New version

* Tue Sep 16 2008 David Lutterkort <dlutter@redhat.com> - 2.1.1-2
- require rubygems >= 1.1.1; the rails code checks that at runtime

* Tue Sep 16 2008 David Lutterkort <dlutter@redhat.com> - 2.1.1-1
- New version (fixes CVE-2008-4094)

* Thu Jul 31 2008 Michael Stahnke <stahnma@fedoraproject.org> - 2.1.0-1
- New Upstream

* Tue Apr  8 2008 David Lutterkort <dlutter@redhat.com> - 2.0.2-2
- Fix dependency

* Mon Apr 07 2008 David Lutterkort <dlutter@redhat.com> - 2.0.2-1
- New version

* Mon Dec 10 2007 David Lutterkort <dlutter@redhat.com> - 2.0.1-1
- New version
- No dependency on actionwebservce anymore, depend on activeresource instead

* Thu Nov 29 2007 David Lutterkort <dlutter@redhat.com> - 1.2.6-1
- Don't copy files into _docdir, mark them as doc in the geminstdir

* Tue Nov 13 2007 David Lutterkort <dlutter@redhat.com> - 1.2.5-2
- Fix buildroot

* Tue Oct 30 2007 David Lutterkort <dlutter@redhat.com> - 1.2.5-1
- Initial package
