Name:		texlive-lshort-thai
Version:	55643
Release:	2
Summary:	Introduction to LaTeX in Thai
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/lshort/thai
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-thai.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-thai.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
This is the Thai translation of the Short Introduction to
LaTeX2e.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/lshort-thai/lsh132.pdf
%doc %{_texmfdistdir}/doc/latex/lshort-thai/lsh132.zip
%doc %{_texmfdistdir}/doc/latex/lshort-thai/readme

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
