Summary:	Tunnelizes connection via http
Summary(pl):	Tunelowanie po��cze� po http
Summary(pt):	Tuneliza conex�es via http
Name:		httptunnel
Version:	3.3
Release:	2
License:	GPL
Group:		Networking/Daemons
Source0:	ftp://ftp.nocrew.org/pub/nocrew/unix/%{name}-%{version}.tar.gz
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
httptunnel tworzy dwukierunkow� wirtualn� drog� dla danych tunelowan�
przez ��dania HTTP. ��dania mog� by� wysy�ane przez HTTP proxy, je�li
jest taka potrzeba. Program jest przydatny dla u�ytkownik�w za bardzo
restryktywnymi firewallami. Je�eli dost�p do WWW jest przez proxy
HTTP, mo�na u�ywa� httptunnelu i np. telnetu lub PPP, aby po��czy� si�
z komputerem za firewallem.

%description -l pt_BR
httptunnel cria um caminho virtual bidirecional tunelado em
requisi��es HTTP. As requisi��es HTTP podem ser enviadas via um proxy
HTTP se desejado. Isto pode ser �til para usu�rios atr�s de firewalls
restritivos. Se o acesso WWW for permitido pelo proxy HTTP, � poss�vel
usar o httptunnel e, digamos, telnet ou PPP para conectar a um
computador fora do firewall.

httptunnel � escrito e mantido por Lars Brinkhoff. Veja o arquivo
AUTHORS para mais informa��o sobre contribuidores a este pacote.

%description -l sv_SE
httptunnel skapar en virtuell tv�v�gs kommunikationskanal tunnlad i
HTTP-paket. HTTP-paketen kan skickas via en HTTP-proxy om s� �nskas.
Detta kan vara anv�ndbart f�r anv�ndare bakom en restriktiv firewall.
Om webben �r tillg�nglig genom en HTTP-proxy, �r det m�jligt att
anv�nda httptunnel, och exempelvis telnet eller PPP f�r att koppla upp
sig mot en dator utanf�r firewallen.

httptunnel �r skriven och underh�llen av Lars Brinkhoff. Se filen
AUTHORS f�r mer information om vilka som har bidragit till detta
paket.

%prep
%setup  -q
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

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS ChangeLog DISCLAIMER FAQ HACKING NEWS README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/htc
%attr(755,root,root) %{_bindir}/hts
%{_mandir}/man1/*
