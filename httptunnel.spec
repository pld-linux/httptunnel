%define name httptunnel
%define version 3.0.3
%define release 1
%define prefix /usr/local

Name: %{name}
Version: %{version}
Release: %{release}
Summary: Tunnelizes connection via http
Summary(pt_BR): Tuneliza conexões via http
Copyright: GPL
Source: ftp://ftp.nocrew.org/pub/nocrew/unix/%{name}-%{version}.tar.gz
URL: http://www.nocrew.org/software/httptunnel.html
Group: System Environment/Daemons
Group(pt_BR): Ambiente do Sistema/Servidores
Packager: Patola (Cláudio Sampaio) <patola@linuxbr.com.br>
Prefix: %{prefix}

%description
httptunnel creates a bidirectional virtual data path tunnelled in HTTP
requests. The HTTP requests can be sent via an HTTP proxy if so desired. 
This can be useful for users behind restrictive firewalls. If WWW access
is allowed through a HTTP proxy, it's possible to use httptunnel and, say,
telnet or PPP to connect to a computer outside the firewall. 

httptunnel is written and maintained by Lars Brinkhoff. See the file
AUTHORS for more information about contributors to this package. 

%description -l pt_BR
httptunnel cria um caminho virtual bidirecional tunelado em requisições
HTTP. As requisições HTTP podem ser enviadas via um proxy HTTP se desejado.
Isto pode ser útil para usuários atrás de firewalls restritivos. Se o
acesso WWW for permitido pelo proxy HTTP, é possível usar o httptunnel e,
digamos, telnet ou PPP para conectar a um computador fora do firewall.

httptunnel é escrito e mantido por Lars Brinkhoff. Veja o arquivo
AUTHORS para mais informação sobre contribuidores a este pacote.

%description -l sv_SE
httptunnel skapar en virtuell tvåvägs kommunikationskanal tunnlad i
HTTP-paket.  HTTP-paketen kan skickas via en HTTP-proxy om så önskas.
Detta kan vara användbart för användare bakom en restriktiv firewall.
Om webben är tillgänglig genom en HTTP-proxy, är det möjligt att
använda httptunnel, och exempelvis telnet eller PPP för att koppla upp
sig mot en dator utanför firewallen.

httptunnel är skriven och underhållen av Lars Brinkhoff.  Se filen
AUTHORS för mer information om vilka som har bidragit till detta
paket.  

%prep

%setup
touch `find . -type f`

%build
CXXFLAGS="$RPM_OPT_FLAGS" CFLAGS="$RPM_OPT_FLAGS" ./configure \
	--prefix=%{prefix}
if [ $? -eq 0 ]
then
  make
else
  exit 1
fi

%install
make install-strip

%files
/usr/local/bin/htc
/usr/local/bin/hts
/usr/local/man/man1/hts.1
/usr/local/man/man1/htc.1
%doc AUTHORS COPYING ChangeLog DISCLAIMER FAQ HACKING INSTALL NEWS README TODO 
