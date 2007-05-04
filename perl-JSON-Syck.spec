#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	JSON
%define	pnam	Syck
Summary:	JSON::Syck - JSON is YAML
#Summary(pl.UTF-8):	
Name:		perl-JSON-Syck
Version:	0.07
Release:	1
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/M/MI/MIYAGAWA/JSON-Syck-0.07.tar.gz
# Source0-md5:	b6a3d39bbec98100fc9433e41ebc773b
# generic URL, check or change before uncommenting
#URL:		http://search.cpan.org/dist/JSON-Syck/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
JSON::Syck is a syck implementatoin of JSON parsing and
generation. Because JSON is YAML
(http://redhanded.hobix.com/inspect/yamlIsJson.html), using syck
gives you the fastest and most memory efficient parser and dumper for
JSON data representation.



# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
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
%doc Changes
%{perl_vendorarch}/JSON/*.pm
%dir %{perl_vendorarch}/auto/JSON/Syck
%{perl_vendorarch}/auto/JSON/Syck/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/JSON/Syck/*.so
%{_mandir}/man3/*
