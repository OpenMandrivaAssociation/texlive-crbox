# revision 29803
# category Package
# catalog-ctan /macros/latex/contrib/crbox
# catalog-date 2013-04-04 12:47:47 +0200
# catalog-license lppl
# catalog-version 0.1
Name:		texlive-crbox
Version:	0.1
Release:	10
Summary:	Boxes with crossed corners
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/crbox
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/crbox.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/crbox.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package implements a \crbox command which produces boxes
with crossing lines at the corners.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/crbox/crbox.sty
%doc %{_texmfdistdir}/doc/latex/crbox/README
%doc %{_texmfdistdir}/doc/latex/crbox/crbox-doc.pdf
%doc %{_texmfdistdir}/doc/latex/crbox/crbox-doc.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
