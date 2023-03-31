Name:		texlive-crbox
Version:	29803
Release:	2
Summary:	Boxes with crossed corners
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/crbox
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/crbox.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/crbox.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
