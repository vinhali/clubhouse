create database checkpoint;

create table goals(
id int primary key,
nameStorie varchar,
startStorie timestamp,
statusStorie BOOLEAN,
endStorie timestamp,
twentyFive int,
statusTwentyFive BOOLEAN,
fifty int,
statusFifty BOOLEAN,
seventyFive int,
statusSeventyFive BOOLEAN,
oneHundred int,
statusOneHundred BOOLEAN,
category varchar,
status varchar
);

create table goals_history(
id int primary key,
nameStorie varchar,
startStorie timestamp,
statusStorie BOOLEAN,
endStorie timestamp,
twentyFive int,
statusTwentyFive BOOLEAN,
fifty int,
statusFifty BOOLEAN,
seventyFive int,
statusSeventyFive BOOLEAN,
oneHundred int,
statusOneHundred BOOLEAN,
category varchar,
status varchar
);

create table exception(
id int primary key,
category varchar,
reason varchar,
justified boolean,
date_insert timestamp
);
