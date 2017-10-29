# Lista dos 20 principais comandos do Terminal do Linux

ssh
Permite logar o usuário num servidor de protocolo ssh. Trata-se de uma conexão segura, da qual você pode entrar e sair com facilidade.

exit
Termina o Shell. Funciona como o “esc”. Para que nenhum outro usuário entre no seu sistema.

apropos
Mostra todos os comando e teclas com a devida descrição. Se esqueceu ou é novo pelo Linux, esse é um dos comandos que irá te auxiliar. É possível encontrar todos os comandos nessa tela.

cal
Mostra o calendário do mês corrente.Útil para quem trabalha precisando acessar calendários.

cd
O comando “cd” é usado para acessar e mudar de diretório corrente. Muito utilizado para a navegação entre as pastas.

cp
Copia o arquivo, tal como o CTRL+C. Facilita muito para quem precisa abrir e fechar arquivos ou copiá-los para outra tela.

date
Mostra na tela a data e horário atualizados.Usado para quem esquece a data do dia, assim como para quem tem mania de verificar as horas a todo momento.

ls
Mostra arquivos que estão na pasta em que o usuário está naquele momento.
Há variações, como exemplo ls -l, que obtem informações mais detalhadas dos arquivos.

mkdir
Serve para criar diretórios. Geralmente na pasta onde o usuário está utilizando.

mv
Move os arquivos de um local para outro. Também utilizado para renomear arquivos.

pwd
Mostra a pasta atual que o usuário está no momento, auxilia no momento de salvar ou criar novos arquivos.

rm
Serve para remover arquivos. Use com cuidado, pois caso remova um documento será irreversível.

rmdir
Serve para remover diretórios vazios. Existe a variação rm: rm –r, da qual é possível remover diretório que não estejam vazios.

cat
Mostra o que tem dentro do arquivo. Funciona para exibir ou ler um documento.

file
Serve para informar qual é o tipo de arquivo digitado como parâmetro (texto, imagem, etc)

clear
Limpa a tela do terminal. Funciona como o CTRL+L.

man
Mostra função de determinado comando. Muito útil para iniciantes, já que mostra o que faz cada tipo.Para sair do man pressione o tecla “q”.

who
Mostra os usuários logados no sistema naquele momento.

wc
Mostra a quantidade de linhas, palavras e caracteres de um arquivo.

whoami
Mostra o nome do usuário que está logado no sistema.

# Comandos de Controlo e Acesso

exit	Terminar a sessão, ou seja, a shell (mais ajuda digitando man sh ou man csh)
logout	Deslogar, ou seja, terminar a sessão actual, mas apenas na C shell e na bash shell
passwd	Mudar a password do nosso utilizador
rlogin	Logar de forma segura noutro sistema Unix/Linux
ssh	Sessão segura, vem de secure shell, e permite-nos logar num servidor através do protocolo ssh
slogin	Versão segura do rlogin
yppasswd	Mudar a password do nosso utilizador nas páginas amarelas (yellow pages)

# Comandos de Comunicações

mail	Enviar e receber emails
mesg	Permitir ou negar mensagens de terminal e pedidos de conversação (talk requests)
pine	Outra forma de enviar e receber emails, uma ferramenta rápida e prática
talk	Falar com outros utilizadores que estejam logados no momento
write	Escrever para outros utilizadores que estejam logados no momento

# Comandos de Ajuda e Documentação

apropos	Localiza comandos por pesquisa de palavra-chave
find	Localizar ficheiros, como por exemplo: find . -name *.txt -print, para pesquisa de ficheiros de texto por entre os ficheiros da directoria actual
info	Lança o explorador de informações
man	Manual muito completo, pesquisa informação acerca de todos os comandos que necessitemos de saber, como por exemplo man find
whatis	Descreve o que um determinado comando é
whereis	Localizar a página de ajuda (man page), código fonte, ou ficheiros binários, de um determinado programa

# Comandos de Edição de Texto

emacs	Editor de texto screen-oriented
pico	Editor de texto screen-oriented, também chamado de nano
sed	Editor de texto stream-oriented
vi	Editor de texto full-screen
vim	Editor de texto full-screen melhorado (vi improved)

# Comandos de Gestão de Ficheiros e Directorias

cd	Mudar de directoria actual, como por exemplo cd directoria, cd .., cd /
chmod	Mudar a protecção de um ficheiro ou directoria, como por exemplo chmod 777, parecido com o attrib do MS-DOS
chown	Mudar o dono ou grupo de um ficheiro ou directoria, vem de change owner
chgrp	Mudar o grupo de um ficheiro ou directoria
cmp	Compara dois ficheiros
comm	Selecciona ou rejeita linhas comuns a dois ficheiros seleccionados
cp	Copia ficheiros, como o copy do MS-DOS
crypt	Encripta ou Desencripta ficheiros (apenas CCWF)
diff	Compara o conteúdo de dois ficheiros ASCII
file	Determina o tipo de ficheiro
grep	Procura um ficheiro por um padrão, sendo um filtro muito útil e usado, por exemplo um cat a.txt | grep ola irá mostrar-nos apenas as linhas do ficheiro a.txt que contenham a palavra “ola”
gzip	Comprime ou expande ficheiros
ln	Cria um link a um ficheiro
ls	Lista o conteúdo de uma directoria, semelhante ao comando dir no MS-DOS
lsof	Lista os ficheiros abertos, vem de list open files
mkdir	Cria uma directoria, vem de make directory”
mv	Move ou renomeia ficheiros ou directorias
pwd	Mostra-nos o caminho por inteiro da directoria em que nos encontramos em dado momento, ou seja a pathname
quota	Mostra-nos o uso do disco e os limites
rm	Apaga ficheiros, vem de remove, e é semelhante ao comando del no MS-DOS, é preciso ter cuidado com o comando rm * pois apaga tudo sem confirmação por defeito
rmdir	Apaga directorias, vem de remove directory
stat	Mostra o estado de um ficheiro, útil para saber por exemplo a hora e data do último acesso ao mesmo
sync	Faz um flush aos buffers do sistema de ficheiros, sincroniza os dados no disco com a memória, ou seja escreve todos os dados presentes nos buffers da memória para o disco
sort	Ordena, une ou compara texto, podendo ser usado para extrair informações dos ficheiros de texto ou mesmo para ordenar dados de outros comandos como por exemplo listar ficheiros ordenados pelo nome
tar	Cria ou extrai arquivos, muito usado como programa de backup ou compressão de ficheiros
tee	Copia o input para um standard output e outros ficheiros
tr	Traduz caracteres
umask	Muda as protecções de ficheiros por defeito
uncompress	Restaura um ficheiro comprimido
uniq	Reporta ou apaga linhas repetidas num ficheiro
wc	Conta linhas, palavras e mesmo caracteres num ficheiro

# Exibição ou Impressão de Ficheiros

cat	Mostra o conteúdo de um ficheiro, como o comando type do MD-DOS, e é muito usado também para concatenar ficheiros, como por exemplo fazendo cat a.txt b.txt > c.txt” para juntar o ficheiro a.txt e b.txt num único de nome c.txt
fold	Encurta, ou seja, faz um fold das linhas longas para caberem no dispositivo de output
head	Mostra as primeiras linhas de um ficheiro, como por exemplo com head -10 a.txt, ou usado como filtro para mostrar apenas os primeiros x resultados de outro comando
lpq	Examina a spooling queue da impressora
lpr	Imprime um ficheiro
lprm	Remove jobs da spooling queue da impressora
more	Mostra o conteúdo de um ficheiro, mas apenas um ecrã de cada vez, ou mesmo output de outros comandos, como por exemplo ls | more
less	Funciona como o more, mas com menos features, menos características e potenciais usos
page	Funciona de forma parecida com o comando more, mas exibe os ecrãs de forma invertida ao comando more
pr	Pagina um ficheiro para posterior impressão
tail	Funciona de forma inversa ao comando head, mostra-nos as últimas linhas de um ficheiro ou mesmo do output de outro comando, quando usado como filtro
zcat	Mostra-nos um ficheiro comprimido
xv	Serve para exibir, imprimir ou mesmo manipular imagens
gv	Exibe ficheiros ps e pdf
xpdf	Exibe ficheiros pdf, usa o gv

# Comandos de Transferência de Ficheiros

ftp	Vem de file transfer protocol, e permite-nos, usando o protocolo de transferência de ficheiros ftp, transferir ficheiros entre vários hosts de uma rede, como aceder a um servidor de ftp para enviar ou puxar ficheiros
rsync	Sincroniza de forma rápida e flexível dados entre dois computadores
scp	Versão segura do rcp

# Comandos de Notícias ou Rede

netstat	Mostra o estado da rede
rsh	Corre umam shell em outros sistemas UNIX
ssh	Versão segura do rsh
nmap	Poderoso port-scan, para visualizarmos portas abertas num dado host
ifconfig	Visualizar os ips da nossa máquina, entre outras funções relacionadas com ips
ping	Pingar um determinado host, ou seja, enviar pacotes icmp para um determinado host e medir tempos de resposta, entre outras coisas
Comandos de Controlo de Processos
kill	Mata um processo, como por exemplo kill -kill 100 ou kill -9 100 ou kill -9 %1
bg	Coloca um processo suspenso em background
fg	Ao contrário do comando bg, o fg traz de volta um processo ao foreground
jobs	Permite-nos visualizar jobs em execução, quando corremos uma aplicação em background, poderemos ver esse job com este comando, e termina-lo com um comando kill -9 %1, se for o job número 1, por exemplo
top	Lista os processos que mais cpu usam, útil para verificar que processos estão a provocar um uso excessivo de memória, e quanta percentagem de cpu cada um usa em dado momento
^y	Suspende o processo no próximo pedido de input
^z	Suspende o processo actual

# Comandos de Informação de Estado

clock	Define a hora do processador
date	Exibe a data e hora
df	Exibe um resumo do espaço livre em disco
du	Exibe um resumo do uso do espaço em disco
env	Exibe as variáveis de ambiente
finger	Pesquisa informações de utilizadores
history	Lista os últimos comandos usados, muito útil para lembrar também de que comandos foram usados para fazer determinada acção no passado ou o que foi feito em dada altura
last	Indica o último login de utilizadores
lpq	Examina a spool queue
manpath	Mostra a path de procura para as páginas do comando man
printenv	Imprime as variáveis de ambiente
ps	Lista a lista de processos em execução, útil para saber o pid de um processo para o mandar abaixo com o comando kill, entre outras coisas
pwd	Mostra-nos o caminho por inteiro da directoria em que nos encontramos em dado momento, ou seja a pathname
set	Define variáveis da sessão, ou seja, da shell, na C shell, na bash ou na ksh
spend	Lista os custos ACITS UNIX até à data
time	Mede o tempo de execução de programas
uptime	Diz-nos há quanto tempo o sistema está funcional, quando foi ligado e o seu uptime
w	Mostra-nos quem está no sistema ou que comando cada job está a executar
who	Mostra-nos quem está logado no sistema
whois	Serviço de directório de domínios da Internet, permite-nos saber informações sobre determinados domínios na Internet, quando um domínio foi registado, quando expira, etc
whoami	Diz-nos quem é o dono da shell

# Comandos de Processamento de Texto

abiword	Processador de Texto Open Source
addbib	Cria ou modifica bases de dados bibliográficas
col	Reverte o filtro a line feeds
diction	Identifica sentenças com palavras
diffmk	Marca diferenças entre ficheiros
dvips	Converte ficheiros TeX DVI em ficheiros PostScript
explain	Explica frases encontradas pelo programa diction
grap	Preprocessador pic para desenhar gráficos, usado em tarefas elementares de análises de dados
hyphen	Encontra palavras com hífenes
ispell	Verifica a ortografia de forma interactiva
latex	Formata texto em LaTeX, que é baseado no TeX
pdfelatex	Para documentos LaTeX em formato pdf
latex2html	Converter LaTeX para html
lookbib	Encontra referências bibliográficas
macref	Cria uma referência cruzada listando ficheiros de macros nroff/troff
ndx	Cria uma página de indexação para um documento
neqn	Formata matemáticas com nroff
nroff	Formata texto para exibição simples
pic	Produz simples imagens para troff input
psdit	Filtra um output troff para a Apple LaserWriter
ptx	Cria uma indexação permutada mas não em CCWF
refer	Insere referências de bases de dados bibliográficas
roffbib	Faz o run off de uma base de dados bibliográfica
sortbib	Ordena uma base de dados bibliográfica
spell	Encontra erros de ortografia
style	Analisa as características superficiais de um documento
tbl	Formata tabelas para nroff/troff
tex	Formata texto
tpic	Converte ficheiros pic source em comandos TeX
wget	Permite-nos fazer o download completo de páginas web, com todos os ficheiros, de forma fácil e não interactiva, sem exigir por isso presença do utilizador, respeitando também o ficheiro robots.txt

# Web

html2ps	Conversor de html para ps
latex2html	Conversor de LaTeX para html
lynx	Navegador web baseado em modo de texto, ou seja, é um web browser que nos permite abrir todo o tipo de páginas visualizando apenas os textos e links, não vendo assim as imagens, e sendo por isso bastante rápido, mas requere prática para ser manuseado
netscape	Navegador web da Netscape
sitecopy	Aplicação que nos permite manter facil e remotamente web sites
weblint	Verificador de sintaxes e de estilos html
