# revision 15878
# category Package
# catalog-ctan /info/lshort/thai
# catalog-date 2006-08-27 16:41:02 +0100
# catalog-license pd
# catalog-version 1.32
Name:		texlive-lshort-thai
Version:	1.32
Release:	1
Summary:	Introduction to LaTeX in Thai
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/lshort/thai
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-thai.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-thai.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
This is the Thai translation of the Short Introduction to
LaTeX2e.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/lshort-thai/lsh132.pdf
%doc %{_texmfdistdir}/doc/latex/lshort-thai/lsh132.zip
%doc %{_texmfdistdir}/doc/latex/lshort-thai/readme
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}