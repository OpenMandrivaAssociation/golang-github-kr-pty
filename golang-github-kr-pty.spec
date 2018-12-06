# http://github.com/kr/pty

%global goipath         github.com/kr/pty
%global commit          2c10821df3c3cf905230d078702dfbe9404c9b23


%gometa -i

Name:           %{goname}
Version:        0
Release:        0.38%{?dist}
Summary:        PTY interface for Go
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.yaml
Source2:        glide.yaml

%description
Pty is a Go package for using UNIX pseudo-terminals.

%package devel
Summary:       %{summary}

%description devel
Pty is a Go package for using UNIX pseudo-terminals.

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%prep
%gosetup -q
cp %{SOURCE1} %{SOURCE2} .
%install
%goinstall glide.lock glide.yaml

%check
%gochecks

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files devel -f devel.file-list
%license License
%doc README.md

%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - Forge-specific packaging variables
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jun 17 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.37.git2c10821
- Upload glide files

* Thu Mar 01 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.36.20170307git2c10821
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.35.git2c10821
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Sep 22 2017 Jan Chaloupka <jchaloup@redhat.com> - 0-0.34.git2c10821
- Bump to upstream 2c10821df3c3cf905230d078702dfbe9404c9b23
  related: #1313956

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.33.gitf7ee69f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.32.gitf7ee69f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.31.gitf7ee69f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.30.gitf7ee69f
- https://fedoraproject.org/wiki/Changes/golang1.7

* Thu Mar 03 2016 jchaloup <jchaloup@redhat.com> - 0-0.29.gitf7ee69f
- Fix fedora macro
  resolves: #1313956

* Sat Feb 27 2016 Peter Robinson <pbrobinson@fedoraproject.org> 0-0.28.gitf7ee69f
- Bump to upstream f7ee69f31298ecbe5d2b349c711e2547a617d398 (add aarch64 support)

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.27.git05017fc
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.26.git05017fc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Sep 12 2015 jchaloup <jchaloup@redhat.com> - 0-0.25.git05017fc
- Update to spec-2.1
  related: #1254595

* Wed Aug 12 2015 Fridolin Pokorny <fpokorny@redhat.com> - 0-0.24.git05017fc
- Update spec file to spec-2.0
  resolves: #1254595

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.23.git05017fc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Feb 25 2015 jchaloup <jchaloup@redhat.com> - 0-0.22.git05017fc
- Bump to upstream 05017fcccf23c823bfdea560dcc958a136e54fb7
  related: #1001396

* Thu Jul 31 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.21.git
- do not own dirs owned by golang
- archfulness and defattr for el6 only

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.20.git67e2db2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat May 31 2014 Lokesh Mandvekar <lsm5@redhat.com> 0-0.19.git
- update to commit 67e2db24c8 (required for docker 1.0
https://github.com/dotcloud/docker/issues/5908 )

* Wed Jan 15 2014 Lokesh Mandvekar <lsm5@redhat.com> 0-0.18.git3b1f648
- exclusivearch for el6+

* Wed Jan 15 2014 Lokesh Mandvekar <lsm5@redhat.com> 0-0.17.git3b1f648
- revert golang >= 1.2 version requirement

* Wed Jan 15 2014 Lokesh Mandvekar <lsm5@redhat.com> 0-0.16.git3b1f648
- require golang 1.2 and up

* Wed Oct 16 2013 Lokesh Mandvekar <lsm5@redhat.com> 0-0.15.git3b1f648
- removed double quotes from provides

* Tue Oct 08 2013 Lokesh Mandvekar <lsm5@redhat.com> 0-0.14.git3b1f648
- noarch for f19+ and rhel7+, exclusivearch otherwise

* Mon Oct 07 2013 Lokesh Mandvekar <lsm5@redhat.com> 0-0.13.git3b1f648
- exclusivearch as per golang

* Sun Oct 06 2013 Lokesh Mandvekar <lsm5@redhat.com> 0-0.12.git3b1f648
- excluded for ppc64
- debug_package nil

* Wed Oct 02 2013 Lokesh Mandvekar <lsm5@fedoraproject.org> 0-0.11.git3b1f648
- docker first run error fix

* Sun Sep 22 2013 Matthew Miller <mattdm@fedoraproject.org> 0-0.10.git27435c6
- install just the source code for devel package

* Tue Sep 17 2013 Lokesh Mandvekar <lsm5@redhat.com> 0-0.9.git27435c6
- version format changed
- docdir unversioned

* Mon Sep 16 2013 Lokesh Mandvekar <lsm5@redhat.com> git27435c6-8
- No debuginfo generated, was empty to begin with
- package owns all directories in goipath

* Mon Sep 16 2013 Lokesh Mandvekar <lsm5@redhat.com> git27435c6-7
- only devel package generated
- Provides moved to devel package
- docdir modified

* Wed Sep 11 2013 Lokesh Mandvekar <lsm5@redhat.com> git27435c6-6
- rm from install section removed

* Tue Sep 10 2013 Lokesh Mandvekar <lsm5@redhat.com> git27435c6-5
- cleanup in prep and build as per guidelines

* Tue Sep 10 2013 Lokesh Mandvekar <lsm5@redhat.com> git27435c6-4
- Build under all circumstances
- Go pkg archives handled (thanks to Vincent Batts (vbatts@redhat.com)

* Thu Aug 29 2013 Lokesh Mandvekar <lsm5@redhat.com> 0.0.1-3
- Devel package generated

* Wed Aug 28 2013 Lokesh Mandvekar <lsm5@redhat.com> 0.0.1-2
- Fixed permissions

* Mon Aug 26 2013 Lokesh Mandvekar <lsm5@redhat.com> 0.0.1-1
- Initial fedora package

