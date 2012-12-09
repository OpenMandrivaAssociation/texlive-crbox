# revision 24414
# category Package
# catalog-ctan /macros/latex/contrib/crbox
# catalog-date 2011-10-26 21:25:52 +0200
# catalog-license lppl
# catalog-version 0.1
Name:		texlive-crbox
Version:	0.1
Release:	2
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


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.1-2
+ Revision: 750622
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.1-1
+ Revision: 718164
- texlive-crbox
- texlive-crbox
- texlive-crbox
- texlive-crbox

