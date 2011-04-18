%define upstream_name    File-PathList
%define upstream_version 1.04

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Find a file within a set of paths (like @INC or Java classpaths)
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/File/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Spec)
BuildRequires: perl(Params::Util)
BuildRequires: perl(Test::More)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README LICENSE META.yml Changes
%{_mandir}/man3/*
%perl_vendorlib/*


