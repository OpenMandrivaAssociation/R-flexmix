%global packname  flexmix
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          2.3_6
Release:          1
Summary:          Flexible Mixture Modeling
Group:            Sciences/Mathematics
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_2.3-6.tar.gz
Requires:         R-lattice R-modeltools R-multcomp R-methods R-stats R-stats4
Requires:         R-MASS R-codetools R-diptest R-ellipse R-gclus R-grid R-lme4
Requires:         R-mgcv R-mlbench R-mvtnorm R-nnet 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-lattice
BuildRequires:    R-modeltools R-multcomp R-methods R-stats R-stats4 
BuildRequires:    R-MASS R-codetools R-diptest R-ellipse R-gclus R-grid
BuildRequires:    R-lme4 R-mgcv R-mlbench R-mvtnorm R-nnet

%description
FlexMix implements a general framework for finite mixtures of regression
models using the EM algorithm.  FlexMix provides the E-step and all data
handling, while the M-step can be supplied by the user to easily define
new models. Existing drivers implement mixtures of standard linear models,
generalized linear models and model-based clustering.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/help
