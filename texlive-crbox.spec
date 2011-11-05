# revision 24414
# category Package
# catalog-ctan /macros/latex/contrib/crbox
# catalog-date 2011-10-26 21:25:52 +0200
# catalog-license lppl
# catalog-version 0.1
Name:		texlive-crbox
Version:	0.1
Release:	1
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
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package implements a \crbox command which produces boxes
with crossing lines at the corners.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/crbox/crbox.sty
%doc %{_texmfdistdir}/doc/latex/crbox/README
%doc %{_texmfdistdir}/doc/latex/crbox/crbox-doc.pdf
%doc %{_texmfdistdir}/doc/latex/crbox/crbox-doc.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
