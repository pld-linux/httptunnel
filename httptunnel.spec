Summary:	Tunnelizes connection via HTTP
Summary(pl):	Tunelowanie po³±czeñ po HTTP
Summary(pt):	Tuneliza conexões via HTTP
Name:		httptunnel
Version:	3.3
Release:	3
License:	GPL
Group:		Networking/Daemons
Source0:	ftp://ftp.nocrew.org/pub/nocrew/unix/%{name}-%{version}.tar.gz
# Source0-md5:	493cc0f5f21e9955db27ee9cd9a976d5
Source1:	%{name}.init
Source2:	%{name}.sysconfig
Source3:	htc.respawn
Patch0:		%{name}-ac_am_fixes.patch
Patch1:		%{name}-remove_port.patch
URL:		http://www.nocrew.org/software/httptunnel.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
httptunnel creates a bidirectional virtual data path tunnelled in HTTP
requests. The HTTP requests can be sent via an HTTP proxy if so
desired. This can be useful for users behind restrictive firewalls. If
WWW access is allowed through a HTTP proxy, it's possible to use
httptunnel and, say, telnet or PPP to connect to a computer outside
the firewall.

httptunnel is written and maintained by Lars Brinkhoff. See the file
AUTHORS for more information about contributors to this package.

%description -l pl
httptunnel tworzy dwukierunkow± wirtualn± drogê dla danych tunelowan±
przez ¿±dania HTTP. ¯±dania mog± byæ wysy³ane przez HTTP proxy, je¶li
jest taka potrzeba. Program jest przydatny dla u¿ytkowników za bardzo
restrykcyjnymi firewallami. Je¿eli dostêp do WWW jest przez proxy
HTTP, mo¿na u¿ywaæ httptunnelu i np. telnetu lub PPP, aby po³±czyæ siê
z komputerem za firewallem.

%description -l pt_BR
httptunnel cria um caminho virtual bidirecional tunelado em
requisições HTTP. As requisições HTTP podem ser enviadas via um proxy
HTTP se desejado. Isto pode ser útil para usuários atrás de firewalls
restritivos. Se o acesso WWW for permitido pelo proxy HTTP, é possível
usar o httptunnel e, digamos, telnet ou PPP para conectar a um
computador fora do firewall.

httptunnel é escrito e mantido por Lars Brinkhoff. Veja o arquivo
AUTHORS para mais informação sobre contribuidores a este pacote.

%description -l sv_SE
httptunnel skapar en virtuell tvåvägs kommunikationskanal tunnlad i
HTTP-paket. HTTP-paketen kan skickas via en HTTP-proxy om så önskas.
Detta kan vara användbart för användare bakom en restriktiv firewall.
Om webben är tillgänglig genom en HTTP-proxy, är det möjligt att
använda httptunnel, och exempelvis telnet eller PPP för att koppla upp
sig mot en dator utanför firewallen.

httptunnel är skriven och underhållen av Lars Brinkhoff. Se filen
AUTHORS för mer information om vilka som har bidragit till detta
paket.

%package client
Summary:	HTTP tunnel client
Summary(pl):	Klient tunelu HTTP
Group:		Networking/Daemons
Requires:	%{name} = %{version}

%description client
HTTP tunnel client.

%description client -l pl
Klient tunelu HTTP.

%package server
Summary:	HTTP tunnel server
Summary(pl):	Server tunelu HTTP
Group:		Networking/Daemons
Requires(post,preun):	/sbin/chkconfig
Requires:	%{name} = %{version}
Requires:	rc-scripts

%description server
HTTP tunnel server.

%description server -l pl
Server tunelu HTTP.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
rm -rf missing port
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/etc/{rc.d/init.d,sysconfig}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/%{name}
install %{SOURCE2} $RPM_BUILD_ROOT/etc/sysconfig/%{name}
install %{SOURCE3} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%post server
/sbin/chkconfig --add httptunnel
if [ -r /var/lock/subsys/httptunnel ]; then
	/etc/rc.d/init.d/httptunnel restart >&2
else
	echo "Run \"/etc/rc.d/init.d/httptunnel start\" to start HTTP tunnel daemons."
fi


%preun server
if [ "$1" = "0" ]; then
	if [ -r /var/lock/subsys/httptunnel ]; then
		/etc/rc.d/init.d/httptunnel stop >&2
	fi
	/sbin/chkconfig --del httptunnel
fi

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog DISCLAIMER FAQ HACKING NEWS README TODO
%{_mandir}/man1/*

%files client
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/htc
%attr(755,root,root) %{_bindir}/htc.respawn

%files server
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/hts
%attr(754,root,root) /etc/rc.d/init.d/*
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/*
