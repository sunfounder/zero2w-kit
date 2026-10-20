@ECHO OFF

pushd %~dp0

REM Command file for Sphinx documentation
REM The English documentation is the master copy and lives in source\.
REM Translations live on separate branches (docs-cn, docs-de, ...).

if "%SPHINXBUILD%" == "" (
	set SPHINXBUILD=sphinx-build
)
set SOURCEDIR=source
set BUILDDIR=build

if "%1" == "" goto help

%SPHINXBUILD% -M %1 %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O%
goto end

:help
%SPHINXBUILD% -M help %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O%
echo.
echo.Usage: make.bat html
echo.       make.bat clean

:end
popd
