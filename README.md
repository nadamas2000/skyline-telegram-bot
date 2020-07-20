# Projecte Skyline Bot
Projecte de bot de Telegram per l'assignatura GRAU-LP (UPC)
08/06/2020 

## Descripció
L'objectiu d'aquest projecte es programar un bot per a la plataforma de comunicació
Telegram segons els requeriments demanats.
https://gebakx.github.io/SkylineBot/

La funció d'aquest bot és de representar Skylines en funció dels paràmetres inicials i poder operar amb ells.

## Prerequisits
#### Interacció
Per poder interactuar amb el bot es recomanable fer servir un client de Telegram. Es pot instal·lar a la següent adreça:
https://telegram.org/apps

#####Token de Telegram
Per crear un canal de Telegram per a un bot cal seguir les instruccions del canal de telegram [@BotFather](https://telegram.me/botfather).
Un cop creat el bot donarà un codi TOKEN que s'ha de guardar a un fitxer **token.txt** al mateix directori que el bot.
El codi per el bot es de l'estil:
```
123456789:AbCdEfGhIjKlMnOpQrStUvWxYz012345567
```


#### Llenguatge i entorn
Aquest bot funciona amb Python3. Per instal·lar Python cal anar a la seva web i instal·lar la versió per al seu sistema operatiu.
https://www.python.org/

Un cop instal·lat es necessita el programa complementari PIP de Python. Per instal·lar PIP cal descarregar el programa en Python get-pip.py. https://bootstrap.pypa.io/get-pip.py

I executar-ho de la seguent manera al directori on es trobi:
```
python get-pip.py
```
##### Llibreries
Les llibreries de Python necessaris que requereix el bot son:

* [matplotlib](https://matplotlib.org/) - Llibreria de representació de dades
* [telegram.ext](https://core.telegram.org/bots/api) - Llibreria de la API de Telegram
* [antlr4](https://www.antlr.org/) - Llibreria de reconeixement de llenguatge
* [pickle](https://docs.python.org/3/library/pickle.html) - Llibreria de tractament de fitxers

Per instal·lar les llibreries s'ha d'executar la comanda:
```
pip install -r requirements.txt
```
On el fitxer **requirements.txt** s'entrega amb el projecte i conté la llista de paquets de python i la seva versió per a que PIP les pugui instal·lar.
```
matplotlib==3.2.1
python-telegram-bot==12.7
antlr4-python3-runtime==4.8
pickle-mixin==1.0.2
```


## Posada en marxa
Per posar en marxa el bot cal executar-ho amb la instrucció:
```
python3 bot.py
```
Mentre estigui executant-se es podran fer peticions de Skylines. Es possible que hagi de verificar la seva connectivitat si hi ha algun tipus de Firewall a la connexió.

## Definició del llenguatge

A la definició del llenguatge s'ha estipulat amb el següent codi grammar:
```
grammar Skyline;

root : assignacio | expressio EOF;

assignacio: ID ASIG expressio;

skylinelist: BEGL elems? ENDL ;

elems: skylinebuilding (SEP skylinebuilding)*;

skylinebuilding: '(' inner=threenums ')' ;

threenums: NUM (SEP NUM) (SEP NUM) ;

skylinerandom: '{' inner=fivenums '}' ;

fivenums: NUM (SEP NUM) (SEP NUM) (SEP NUM) (SEP NUM) ;

skylineobj: skylinelist
    | skylinerandom
    | skylinebuilding
    | ID
    ;

expressio: '(' inner=expressio ')'
    | SUB expressio
    | expressio MUL expressio
    | expressio SUM expressio
    | expressio SUB expressio
    | skylineobj
    | NUM
    ;

NUM: [0-9]+ ;
ID: [a-zA-Z][a-zA-Z0-9]* ;

SUM: '+' ;
SUB: '-' ;
MUL: '*' ;
ASIG: ':=';

BEGL: '[' ;
ENDL: ']' ;

SEP: ',' ;

WS: [ \t\r\n\u000C] -> skip ;
```
Al llenguatge es demanava que les operacions de suma, resta i multiplicació, amb operadors (+,-,*) només sigues permesa amb un Skyline a la esquerra i un enter a la dreta.
Això s'ha restringit per la classe Skyline ja que interferia amb altres operacions com:
   * `-((2,3,4) + (3,4,5))` on la negació d'una operació de Skylines resulta correcte encara que el llenguatge reconeix com la negació d'un parèntesi, que es una expressió.
   * `(2,3,4) + (5 - 4)` que també és correcte però la resta es fa amb dos enters.
   
Per simplificar el codi s'ha decidir prendre aquesta decisió i no especificar càlculs explícits a la definició de "expressió" del grammar.
En els cassos no permesos es presenta un error amb el missatge "Operació no permesa" enviat des de la classe Skyline. 

## Funcionament

Algunes de les proves realitzades satisfactòriament amb el bot de Telegram son:

`(2,3,4)`

`[(1, 2, 3), (3, 4, 6)]`

`[(1, 1, 2), (1000000000000, 1, 1000000000001)]` (Les línies son tan fines que no es veuen)

`{100000,20,3,1,10000}` (El càlcul de 100.000 edificis triga uns 20 segons)

`(2,3,4) + 4`

`(2,3,4) - 4`

`(2,3,4) * 4`

`(2,3,4) + (3,4,5)`

`(2,3,4) * (3,4,5)`

`-((2,3,4) + (3,4,5))`

`a := (2,3,4) + (3,4,5)`

`a + 4`

`a * 4`

`a - 4`

`-a`

`/save a`

`/load a`

`b := ((5,6,7) + (6,7,8)) * 3`

`a + b`

`a * b`

`a := (a+1) * b`

`a := [(1, 2, 3), (3, 4, 6)]`

`b := {100000,20,3,1,10000} + 200` (El càlcul de 100.000 edificis triga uns 20 segons)

`a := 4 + a` (Dona error perquè la operació no es permesa, com ha de indicar)

`a := 4 * a` (Dona error perquè la operació no es permesa, com ha de indicar)

`a := 4 - a` (Dona error perquè la operació no es permesa, com ha de indicar)


## Proves de llenguatge

Dintre de la carpeta **cl** es troba la part de llenguatge i hi han dos programes en python que permeten realitzar operacions amb Skylines en modus text.

* [test.SkylineOpTree.py] - Permet mostrar l'arbre de lectura de les instruccions.
* [test.SkylineOpCalc.py] - Permet calcular amb Skylines i enters com en el bot. El resultat es mostra només en texte.



