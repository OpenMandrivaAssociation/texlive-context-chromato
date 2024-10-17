Name:		texlive-context-chromato
Version:	47085
Release:	2
Summary:	ConTeXt macros for chromatograms
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/context/contrib/context-chromato
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-chromato.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-chromato.doc.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/context/third/chromato
%doc %{_texmfdistdir}/doc/context/third/chromato

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
