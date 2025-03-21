-- CREATE SCHEMA public AUTHORIZATION pg_database_owner;

CREATE TABLE public.account (
	account_id serial4 NOT NULL,
	"password" varchar(100) NULL,
	username varchar(255) NULL,
	address_id int4 NULL,
	email text NULL,
	CONSTRAINT account_pkey PRIMARY KEY (account_id)
);

CREATE TABLE public.address (
	address_id serial4 NOT NULL,
	street_address varchar(255) NULL,
	city varchar(100) NULL,
	state varchar(100) NULL,
	country varchar(100) NULL,
	phone varchar(20) NULL,
	CONSTRAINT address_pkey PRIMARY KEY (address_id)
);

CREATE TABLE public.book (
	isbn varchar(20) NOT NULL,
	title varchar(255) NULL,
	category_id int4 NULL,
	publisher varchar(255) NULL,
	"language" varchar(100) NULL,
	no_of_copies int2 NULL DEFAULT 1,
	CONSTRAINT book_pkey PRIMARY KEY (isbn)
);

CREATE TABLE public.booklending (
	lending_id serial4 NOT NULL,
	account_id int4 NULL,
	creation_date date NULL,
	due_date date NULL,
	isbn varchar(20) NOT NULL,
	CONSTRAINT booklending_pkey PRIMARY KEY (lending_id)
);

CREATE TABLE public.bookreservation (
	reservation_id serial4 NOT NULL,
	account_id int4 NULL,
	creation_date date NULL,
	isbn varchar(20) NOT NULL,
	CONSTRAINT bookreservation_pkey PRIMARY KEY (reservation_id)
);

CREATE TABLE public.category (
	id serial4 NOT NULL,
	"name" varchar(100) NOT NULL,
	CONSTRAINT category_pkey PRIMARY KEY (id)
);

CREATE TABLE public.librarian (
	librarian_id serial4 NOT NULL,
	account_id int4 NULL,
	CONSTRAINT librarian_pkey PRIMARY KEY (librarian_id)
);

CREATE TABLE public.reservation_history (
	history_id serial4 NOT NULL,
	account_id int4 NULL,
	borrowed_date timestamp NULL,
	return_date timestamp NULL,
	isbn varchar(20) NOT NULL,
	CONSTRAINT reservation_history_pkey PRIMARY KEY (history_id)
);