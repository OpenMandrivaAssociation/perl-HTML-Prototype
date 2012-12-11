%define upstream_name	 HTML-Prototype
%define upstream_version 1.48

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Generate HTML and Javascript for the Prototype library
License:	Artistic/GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/HTML/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:  perl(Module::Build)
BuildRequires:	perl(Class::Accessor)
BuildRequires:  perl(HTML::Tree)
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
Some code generators for Prototype, the famous JavaScript OO library. This
library allows you to do Ajax without writing lots of javascript code. This is
mostly a port of the Ruby on Rails helper tags for JavaScript for use in
Catalyst.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
perl -pi -e 'tr/\r//d;' README

%build
%{__perl} ./Build.PL installdirs=vendor
./Build

%check
./Build test

%install
rm -rf %{buildroot}
./Build install destdir=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README Changes
%{perl_vendorlib}/HTML
%{_mandir}/*/*


%changelog
* Wed Jul 29 2009 J√©r√¥me Quelin <jquelin@mandriva.org> 1.480.0-1mdv2010.0
+ Revision: 403257
- rebuild using %%perl_convert_version

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 1.48-3mdv2009.0
+ Revision: 241476
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue May 01 2007 Olivier Thauvin <nanardon@mandriva.org> 1.48-1mdv2008.0
+ Revision: 20123
- 1.48


* Tue Aug 29 2006 guillomovitch
+ 2006-08-29 10:19:23 (58585)
- new version

* Thu Aug 03 2006 Nicolas LÈcureuil <neoclust@mandriva.org>
+ 2006-08-03 15:02:10 (43219)
- import perl-HTML-Prototype-1.45-1mdv2007.0

* Fri Jun 02 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.45-1mdv2007.0
- New release 1.45
- better sources URL
- spec cleanup

* Fri Feb 10 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.43-1mdk
- New release 1.43

* Wed Jan 25 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.41-1mdk
- New release 1.41

* Mon Dec 19 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.36-1mdk
- New release 1.36
- spec cleanup
- fix directory ownership
- fix doc file encoding

* Mon Oct 10 2005 Nicolas LÈcureuil <neoclust@mandriva.org> 1.35-3mdk
- Fix BuildRequires

* Fri Sep 30 2005 Nicolas LÈcureuil <neoclust@mandriva.org> 1.35-2mdk
- Buildrequires fix

* Wed Sep 21 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.35-1mdk
- 1.35
- rpmbuildupdate aware

* Tue Aug 16 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.32-1mdk
- 1.32

* Wed May 04 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.23-1mdk
- First Mandriva release

