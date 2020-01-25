#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	JSON
%define	pnam	Syck
Summary:	JSON::Syck - JSON is YAML
Summary(pl.UTF-8):	JSON::Syck - JSON to YAML
Name:		perl-JSON-Syck
Version:	0.07
Release:	2
License:	BSD or D&R (see COPYING)
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/M/MI/MIYAGAWA/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b6a3d39bbec98100fc9433e41ebc773b
URL:		http://search.cpan.org/dist/JSON-Syck/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
JSON::Syck is a syck implementation of JSON parsing and
generation. Because JSON is YAML
(http://redhanded.hobix.com/inspect/yamlIsJson.html), using syck
gives you the fastest and most memory efficient parser and dumper for
JSON data representation.

%description -l pl.UTF-8
JSON::Syck to implementacja syck analizy i generowania JSON. Ponieważ
JSON to YAML
(http://redhanded.hobix.com/inspect/yamlIsJson.html), wykorzystanie
sycka daje najszybszy i najbardziej wydajny pamięciowo analizator i
dumper dla reprezentacji danych JSON.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING Changes
%{perl_vendorarch}/JSON/*.pm
%dir %{perl_vendorarch}/auto/JSON/Syck
%attr(755,root,root) %{perl_vendorarch}/auto/JSON/Syck/*.so
%{_mandir}/man3/*
