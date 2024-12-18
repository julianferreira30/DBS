
import psycopg2
import csv

conn = psycopg2.connect(
    host="cc3201.dcc.uchile.cl",
    database="cc3201",
    user="cc3201",
    password="cc3201",
    port="5508"
)

cur = conn.cursor()
cur.execute("create table if not exists atleta( \
               id varchar(255) primary key, \
    nombre varchar(255) not null, \ 
    genero varchar(255) not null, \
    nacionalidad varchar(255) not null, \
    pais_residencia varchar(255), \
    altura integer,
    peso float,
    fecha_nacimiento varchar(255) not null,
    lugar_nacimiento varchar(255)
")


 aux = "create table if not exists entrenador(
    id integer primary key,
    nombre varchar(255) not null,
    genero varchar(255) not null,
    funcion varchar(255) not null,
    categoria varchar(255) not null,
    nacionalidad varchar(255) not null
);

-----------Equipo---------------
create table if not exists equipo(
    id varchar(255),
    atleta_id integer,
    nombre varchar(255),
    pais varchar(255),
    genero varchar(255),
    disciplina varchar(255),
    events varchar,
    primary key (id, atleta_id),
    foreign key atleta_id references atleta(id) 
);

-----Pais------
create table if not exists pais(
    id varchar(255) primary key,
    recuento_medallas integer not null,
    oros integer not null,
    platas integer not null,
    bronces integer not null
);

------Disciplina-------
create table if not exists disciplina(
    id serial primary key,
    nombre varchar(255) not null
);

--------Evento--------
create table if not exists evento(
    nombre varchar(255) primary key,
    ganador varchar(255) not null
);

-------Medalla-------
create table if not exists medalla_individual(
    id integer not null,
    evento_nombre varchar(255) not null,
    atleta_id varchar(255) not null,
    tipo varchar(255) not null,
    primary key (id, evento_nombre, atleta_id),
    foreign key (evento_nombre) references evento(nombre),
    foreign key (atleta_id) references atleta(id)
);

create table if not exists medalla_grupal(
    id integer not null,
    evento_nombre varchar(255) not null,
    equipo_id varchar(255) not null,
    tipo varchar(255) not null,
    primary key (id, evento_nombre, atleta_id),
    foreign key (evento_nombre) references evento(nombre),
    foreign key (equipo_id) references equipo(id)
);

-------------Contiene------------
___________SE PODRIA CAMBIAR EL NOMBRE_______
create table if not exists evento_disciplina(
    disciplina_id integer not null,
    evento_nombre varchar(255) not null,
    phase varchar(255) not null,
    venue varchar(255) not null,
    primary key (disciplina_id, evento_nombre),
    foreign key (disciplina_id) references disciplina(id),
    foreign key (evento_nombre) references evento(nombre)
);

-------------------Representa------------------
--------CAMBIARE EL NOMBRE-----------------
create table if not exists atleta_pais(
    atleta_id varchar(255) not null,
    pais_id varchar(255) not null,
    primary key (atleta_id, pais_id),
    foreign key (atleta_id) references atleta(id),
    foreign key (pais_id) references pais(id)
);


------------Compite_en------------
____________TAMBIEN SE PUEDE CAMBIAR EL NOMBRE_________
create table if not exists evento_atleta(
    evento_nombre varchar(255) not null,
    atleta_id varchar(255) not null,
    primary key (evento_nombre, atleta_id),
    foreign key (evento_nombre) references evento(nombre),
    foreign key (atleta_id) references atleta(id)
);

--------Entrena-------
create table if not exists entrenador_atleta(
    entrenador_id integer not null,
    atleta_id varchar(255) not null,
    primary key (entrenador_id, atleta_id),
    foreign key (entrenador_id) references entrenador(id),
    foreign key (atleta_id) references atleta(id)
);