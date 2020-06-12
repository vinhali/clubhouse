create table goals(
id serial primary key,
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
category varchar
);

create table goals_history(
id serial primary key,
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
category varchar
);
