
create table series
( id int auto_increment,
  name varchar(20));

create table episodes 
( id int auto_increment,
  name varchar(60),
  number int,
  serie_id int);
