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