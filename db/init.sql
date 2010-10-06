
create table series
( id int,
  name varchar(20));

create table episodes 
( id int,
  name varchar(60),
  number int,
  serie_id int);
