%define module	HTML-Prototype
%define name	perl-%{module}
%define version	1.48
%define release %mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Generate HTML and Javascript for the Prototype library
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}/
Source:		http://www.cpan.org/modules/by-module/HTML/%{module}-%{version}.tar.bz2
BuildRequires:  perl(Module::Build)
BuildRequires:	perl(Class::Accessor)
BuildRequires:  perl(HTML::Tree)
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}

%description
Some code generators for Prototype, the famous JavaScript OO library. This
library allows you to do Ajax without writing lots of javascript code. This is
mostly a port of the Ruby on Rails helper tags for JavaScript for use in
Catalyst.

%prep
%setup -q -n %{module}-%{version}
perl -pi -e 'tr/\r//d;' README

%build
%{__perl} ./Build.PL installdirs=vendor
./Build

%check
./Build test

%install
rm -rf %{buildroot}
./Build install destdir=%{buildroot}

%files
%defattr(-,root,root)
%doc README Changes
%{perl_vendorlib}/HTML
%{_mandir}/*/*

%clean
rm -rf %{buildroot}


