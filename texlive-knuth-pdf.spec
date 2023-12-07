Name:		texlive-knuth-pdf
Version:	67332
Release:	1
Summary:	PDF collection of typeset C/WEB sources in TeX Live
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/knuth-pdf
License:	pd
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/knuth-pdf.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/knuth-pdf.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Here you find a large collection of PDF documents for many
C/WEB programs in TeX Live, both in their original form as
written by their respective authors, and in the changed form as
they are actually used in the TeX Live system. Care has been
taken to keep the section numbering intact, so that you can
study the sources and their changes in parallel. Also included
is the collection of "errata" for Donald Knuth's "Computers &
Typesetting series". Although not all the texts here are
written or maintained by Donald Knuth, it is more convenient
for everything to be collected in one place for reading and
searching. They all stem from the system that Knuth created.
The central entry point is the "index" file, with links to the
individual documents, either in HTML or in PDF format.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/doc/generic/knuth-pdf

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
