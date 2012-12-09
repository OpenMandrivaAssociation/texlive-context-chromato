# revision 23167
# category ConTeXt
# catalog-ctan /macros/context/contrib/context-chromato
# catalog-date 2006-08-27 16:41:02 +0100
# catalog-license gpl
# catalog-version undef
Name:		texlive-context-chromato
Version:	20060827
Release:	2
Summary:	ConTeXt macros for chromatograms
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/context/contrib/context-chromato
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-chromato.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-chromato.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires(post):	texlive-context

%description
The module provides macros for drawing chromatograms.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/context/third/chromato/t-chromato.tex
%doc %{_texmfdistdir}/doc/context/third/chromato/chromato-demo.pdf
%doc %{_texmfdistdir}/doc/context/third/chromato/chromato-doc.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 20060827-2
+ Revision: 750490
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20060827-1
+ Revision: 718125
- texlive-context-chromato
- texlive-context-chromato
- texlive-context-chromato
- texlive-context-chromato

