#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v26
# autospec commit: 99a7985
#
Name     : R-spatstat.explore
Version  : 3.4.3
Release  : 25
URL      : https://ftp.osuosl.org/pub/cran/src/contrib/spatstat.explore_3.4-3.tar.gz
Source0  : https://ftp.osuosl.org/pub/cran/src/contrib/spatstat.explore_3.4-3.tar.gz
Summary  : Exploratory Data Analysis for the 'spatstat' Family
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-spatstat.explore-lib = %{version}-%{release}
Requires: R-abind
Requires: R-goftest
Requires: R-spatstat.data
Requires: R-spatstat.geom
Requires: R-spatstat.random
Requires: R-spatstat.sparse
Requires: R-spatstat.univar
Requires: R-spatstat.utils
BuildRequires : R-abind
BuildRequires : R-goftest
BuildRequires : R-spatstat.data
BuildRequires : R-spatstat.geom
BuildRequires : R-spatstat.random
BuildRequires : R-spatstat.sparse
BuildRequires : R-spatstat.univar
BuildRequires : R-spatstat.utils
BuildRequires : buildreq-R

%description
spatial data, mainly spatial point patterns,
	     in the 'spatstat' family of packages.
	     (Excludes analysis of spatial data on a linear network,
	     which is covered by the separate package 'spatstat.linnet'.)
	     Methods include quadrat counts, K-functions and their simulation envelopes, nearest neighbour distance and empty space statistics, Fry plots, pair correlation function, kernel smoothed intensity, relative risk estimation with cross-validated bandwidth selection, mark correlation functions, segregation indices, mark dependence diagnostics, and kernel estimates of covariate effects. Formal hypothesis tests of random pattern (chi-squared, Kolmogorov-Smirnov, Monte Carlo, Diggle-Cressie-Loosmore-Ford, Dao-Genton, two-stage Monte Carlo) and tests for covariate effects (Cox-Berman-Waller-Lawson, Kolmogorov-Smirnov, ANOVA) are also supported.

%package lib
Summary: lib components for the R-spatstat.explore package.
Group: Libraries

%description lib
lib components for the R-spatstat.explore package.


%prep
%setup -q -n spatstat.explore
pushd ..
cp -a spatstat.explore buildavx2
popd
pushd ..
cp -a spatstat.explore buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1747866158

%install
export SOURCE_DATE_EPOCH=1747866158
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/spatstat.explore/CITATION
/usr/lib64/R/library/spatstat.explore/DESCRIPTION
/usr/lib64/R/library/spatstat.explore/INDEX
/usr/lib64/R/library/spatstat.explore/Meta/Rd.rds
/usr/lib64/R/library/spatstat.explore/Meta/features.rds
/usr/lib64/R/library/spatstat.explore/Meta/hsearch.rds
/usr/lib64/R/library/spatstat.explore/Meta/links.rds
/usr/lib64/R/library/spatstat.explore/Meta/nsInfo.rds
/usr/lib64/R/library/spatstat.explore/Meta/package.rds
/usr/lib64/R/library/spatstat.explore/NAMESPACE
/usr/lib64/R/library/spatstat.explore/NEWS
/usr/lib64/R/library/spatstat.explore/R/spatstat.explore
/usr/lib64/R/library/spatstat.explore/R/spatstat.explore.rdb
/usr/lib64/R/library/spatstat.explore/R/spatstat.explore.rdx
/usr/lib64/R/library/spatstat.explore/doc/packagesizes.txt
/usr/lib64/R/library/spatstat.explore/help/AnIndex
/usr/lib64/R/library/spatstat.explore/help/aliases.rds
/usr/lib64/R/library/spatstat.explore/help/macros/defns.Rd
/usr/lib64/R/library/spatstat.explore/help/paths.rds
/usr/lib64/R/library/spatstat.explore/help/spatstat.explore.rdb
/usr/lib64/R/library/spatstat.explore/help/spatstat.explore.rdx
/usr/lib64/R/library/spatstat.explore/html/00Index.html
/usr/lib64/R/library/spatstat.explore/html/R.css
/usr/lib64/R/library/spatstat.explore/info/packagesizes.txt
/usr/lib64/R/library/spatstat.explore/tests/funky.tab
/usr/lib64/R/library/spatstat.explore/tests/testsAtoC.R
/usr/lib64/R/library/spatstat.explore/tests/testsD.R
/usr/lib64/R/library/spatstat.explore/tests/testsEtoF.R
/usr/lib64/R/library/spatstat.explore/tests/testsGtoJ.R
/usr/lib64/R/library/spatstat.explore/tests/testsK.R
/usr/lib64/R/library/spatstat.explore/tests/testsL.R
/usr/lib64/R/library/spatstat.explore/tests/testsM.R
/usr/lib64/R/library/spatstat.explore/tests/testsNtoO.R
/usr/lib64/R/library/spatstat.explore/tests/testsP1.R
/usr/lib64/R/library/spatstat.explore/tests/testsP2.R
/usr/lib64/R/library/spatstat.explore/tests/testsQ.R
/usr/lib64/R/library/spatstat.explore/tests/testsR1.R
/usr/lib64/R/library/spatstat.explore/tests/testsR2.R
/usr/lib64/R/library/spatstat.explore/tests/testsS.R
/usr/lib64/R/library/spatstat.explore/tests/testsT.R
/usr/lib64/R/library/spatstat.explore/tests/testsUtoZ.R

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/R/library/spatstat.explore/libs/spatstat.explore.so
/V4/usr/lib64/R/library/spatstat.explore/libs/spatstat.explore.so
/usr/lib64/R/library/spatstat.explore/libs/spatstat.explore.so
