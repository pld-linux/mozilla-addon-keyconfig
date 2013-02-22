%define		subver	20110522
%define		extension keyconfig
Summary:	The Keyconfig extension allows you to configure keyboard shortcuts
Name:		mozilla-addon-%{extension}
Version:	0.%{subver}
Release:	1
License:	MPL v1.1 or GPL v2+ or LGPL v2.1+
Group:		X11/Applications/Networking
Source0:	http://mozilla.dorando.at/keyconfig/keyconfig-%{subver}.xpi
# Source0-md5:	a886fabc4dd3dba41a104dd5d0f9eccb
URL:		http://kb.mozillazine.org/Keyconfig_extension
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# this comes from install.rdf (<em:id> or <id>)
%define		extension_id	keyconfig@dorando
%define		extensionsdir	%{_prefix}/lib/mozilla/extensions

%description
The Keyconfig extension allows you to configure keyboard shortcuts. It
works with Firefox, Thunderbird, and (probably) Mozilla
Suite/SeaMonkey. Shortcuts defined via a key can be changed.

%prep
%setup -qc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{extensionsdir}/%{extension_id}
cp -a . $RPM_BUILD_ROOT%{extensionsdir}/%{extension_id}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{extensionsdir}/%{extension_id}
%{extensionsdir}/%{extension_id}/chrome.manifest
%{extensionsdir}/%{extension_id}/defaults
%{extensionsdir}/%{extension_id}/install.rdf
%{extensionsdir}/%{extension_id}/components
%{extensionsdir}/%{extension_id}/keyconfig.zip
