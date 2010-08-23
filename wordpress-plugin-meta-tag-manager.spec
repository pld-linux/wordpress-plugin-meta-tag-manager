%define		plugin	meta-tag-manager
Summary:	Meta Tag Manager plugin for Wordpress
Name:		wordpress-plugin-meta-tag-manager
Version:	1.1
Release:	1
License:	GPL
Group:		Applications/Publishing
URL:		http://netweblogic.com/wordpress/plugins/meta-tag-manager
# Use DF or something. On each download it has new md5.
# Source0:	http://downloads.wordpress.org/plugin/meta-tag-manager.zip
Source0:	http://execve.pl/PLD/meta-tag-manager.zip#/meta-tag-manager-%{version}.zip
# Source0-md5:	0b41eea3cb24b537bf51e52adfd34b66
BuildRequires:	js
BuildRequires:	unzip
BuildRequires:	yuicompressor
Requires:	wordpress >= 2.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		wordpressdir	%{_datadir}/wordpress
%define		pluginssubdir	wp-content/plugins
%define		pluginsdir		%{wordpressdir}/%{pluginssubdir}
%define		plugindir		%{pluginsdir}/%{plugin}

%description
Simple plugin which allows you to add custom meta tags that will show
across all pages on your blog or on the homepage only.

%prep
%setup -q -n %{plugin}

mkdir build

%build
yuicompressor mtm_script.js > build/mtm_script.js
js -C -f build/mtm_script.js

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a *.php *.mo *.po $RPM_BUILD_ROOT%{plugindir}
cp -a build/* $RPM_BUILD_ROOT%{plugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc readme.txt
%{plugindir}
