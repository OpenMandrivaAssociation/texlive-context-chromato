# revision 23167
# category ConTeXt
# catalog-ctan /macros/context/contrib/context-chromato
# catalog-date 2006-08-27 16:41:02 +0100
# catalog-license gpl
# catalog-version undef
Name:		texlive-context-chromato
Version:	20060827
Release:	1
Summary:	ConTeXt macros for chromatograms
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/context/contrib/context-chromato
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-chromato.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-chromato.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Requires:	texlive-context
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Requires(post):	texlive-context.bin

%description
The module provides macros for drawing chromatograms.

%pre
    %_texmf_mtxrun_pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mtxrun_post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mtxrun_pre
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mtxrun_post
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/context/third/chromato/t-chromato.tex
%doc %{_texmfdistdir}/doc/context/third/chromato/chromato-demo.pdf
%doc %{_texmfdistdir}/doc/context/third/chromato/chromato-doc.pdf
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
