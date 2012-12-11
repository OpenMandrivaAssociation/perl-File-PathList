%define upstream_name    File-PathList
%define upstream_version 1.04

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Find a file within a set of paths (like @INC or Java classpaths)
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/File/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(Params::Util)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
Many systems that map generic relative paths to absolute paths do so with a
set of base paths.

For example, perl itself when loading classes first turn a 'Class::Name'
into a path like 'Class/Name.pm', and thens looks through each element of
'@INC' to find the actual file.

To aid in portability, all relative paths are provided as unix-style
relative paths, and converted to the localised version in the process of
looking up the path.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README LICENSE META.yml Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 1.40.0-2mdv2011.0
+ Revision: 655600
- rebuild for updated spec-helper

* Thu Sep 02 2010 Jérôme Quelin <jquelin@mandriva.org> 1.40.0-1mdv2011.0
+ Revision: 575421
- import perl-File-PathList

