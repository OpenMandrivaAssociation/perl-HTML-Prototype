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
