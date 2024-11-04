import psycopg2
import csv

conn = psycopg2.connect(host="cc3201.dcc.uchile.cl", database="cc3201",
    user="cc3201",
    password="j'<3_cc3201", port="5440")

cur = conn.cursor()


#cur.execute("truncate table atleta restart identity cascade")
#cur.execute("truncate table pais restart identity cascade")
#cur.execute("truncate table entrenador restart identity cascade")
#cur.execute("truncate table disciplina restart identity cascade")
#cur.execute("truncate table evento restart identity cascade")
#cur.execute("truncate table medalla restart identity cascade")
#cur.execute("truncate table evento_disciplina restart identity cascade")
#cur.execute("truncate table disciplina_atleta restart identity cascade")
#cur.execute("truncate table entrenador_atleta restart identity cascade")

atleta_pais_cache = []
with open('./Data/athletes.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    i = 0
    for row in reader:
        i+=1
        if i == 1:
            continue

        # Poblar atletas
        atleta_id = row[0]
        atleta_nombre = row[1]
        atleta_genero = row[4]
        atleta_pais_id = row[6]
        # Pasar a español
        if atleta_genero == "Male":
            atleta_genero = "Masculino"
        else:
            atleta_genero = "Femenino"

        atleta_nacionalidad = row[9]
        
        atleta_pais_residencia = row[20]
        if atleta_pais_residencia == "":
            atleta_pais_residencia = None
        
        atleta_altura = row[12]
        if atleta_altura == "" or int(float(atleta_altura)) == 0:
            atleta_altura = None
        
        atleta_peso = row[13]
        if atleta_peso == "" or int(float(atleta_peso)) == 0:
            atleta_peso = None
        

        atleta_fecha_nacimiento = str(row[16])
        atleta_lugar_nacimiento = row[17]
        if atleta_lugar_nacimiento == "":
            atleta_lugar_nacimiento = None

        ############ SOLO PARA VER COMO SE VE LA INFO ########################
        info = [atleta_id, atleta_nombre, atleta_fecha_nacimiento, atleta_genero]
        print(info)
        ########################

        atleta_pais_cache.append([atleta_id, atleta_pais_id])

        cur.execute("insert into atleta values (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                   [atleta_id, atleta_nombre, atleta_genero, atleta_nacionalidad, atleta_pais_residencia, atleta_altura, atleta_peso, atleta_fecha_nacimiento, atleta_lugar_nacimiento])


# Poblar Entrenador
with open('./Data/coaches.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    i = 0
    for row in reader:
        i+=1
        if i == 1:
            continue
        print(i)

        entrenador_id = row[0]
        entrenador_nombre = row[1]
        entrenador_genero = row[2]
        if entrenador_genero == "Male":
            entrenador_genero = "Masculino"
        else:
            entrenador_genero = "Femenino"

        entrenador_funcion = row[3]
        if entrenador_funcion == "Coach":
            entrenador_funcion = "Entrenador"
        elif entrenador_funcion == "Head Coach":
            entrenador_funcion = "Entrenador en jefe"
        elif entrenador_funcion == "Assistant Coach":
            entrenador_funcion = "Entrenador asistente"
        
        entrenador_categoria = row[4]


        # Creo que puede ser en que país dirige, no necesariamente su nacionalidad

        entrenador_nacionalidad = row[6]

        # Podríamos incluir la disciplina que coachea
        cur.execute("insert into entrenador values (%s, %s, %s, %s, %s, %s)",
                   [entrenador_id, entrenador_nombre, entrenador_genero, entrenador_funcion, entrenador_categoria, entrenador_nacionalidad])


#Poblar Pais
with open('./Data/medals_total.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    i = 0
    for row in reader:
        i+=1
        if i == 1:
            continue
        print(i)

        # Cambie nombre, a codigo del pais, por como están los datos
        # Además incluiré la cantidad de oros, platas y bronces

        pais_codigo = row[0]
        pais_oros = row[1]
        pais_platas = row[2]
        pais_bronces = row[3]
        pais_total = row[4] 
        
        cur.execute("insert into pais values (%s, %s, %s, %s, %s)",
                   [pais_codigo, pais_oros, pais_platas, pais_bronces, pais_total])


# Poblar tabla Evento
with open('./Data/medals.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    i = 0
    for row in reader:
        i+=1
        if i == 1:
            continue

        
        if row[1] == 1: # Significa que estamos viendo el ganador (medalla de oro)

            evento_disciplina = row[6] 
            evento_genero = row[5]

            # Hay 2 eventos con el mismo nombre, ya que está masculino y femenino,
            # asique se hace que el nombre del evento sea la concatenacion del genero al final.
            evento_nombre = evento_disciplina + ' ' + evento_genero 
            evento_ganador = row[3]
            cur.execute("insert into evento values (%s, %s)", [evento_nombre, evento_ganador])
        
        # Aprovechamos de poblar la tabla Medalla
        medalla_id = row[1]
        medalla_evento_nombre = row[6] + ' ' + row[5]
        medalla_atleta_id = row[10]
        medalla_tipo = row[0]
        cur.execute("insert into medalla values (%s, %s, %s, %s)", 
                   [medalla_id, medalla_evento_nombre, medalla_atleta_id, medalla_tipo])


# Poblar disciplina

# Poblar evento_disciplina

# Poblar evento_atleta

# Poblar entrenador_atleta


# Poblar atleta_pais
for dupla in atleta_pais_cache:
    atleta_id = dupla[0]
    pais_id = dupla[1]

    cur.execute("insert into atleta_pais values (%s, %s)", [atleta_id, pais_id])
