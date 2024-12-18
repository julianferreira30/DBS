import psycopg2
from psycopg2.errors import ForeignKeyViolation
import csv
import ast

conn = psycopg2.connect(
    host="cc3201.dcc.uchile.cl",
    database="cc3201",
    user="cc3201",
    password="cc3201",
    port="5508"
)

cur = conn.cursor()

'''
cur.execute("truncate table atleta restart identity cascade")
cur.execute("truncate table equipo restart identity cascade")
cur.execute("truncate table pais restart identity cascade")
cur.execute("truncate table entrenador restart identity cascade")
cur.execute("truncate table disciplina restart identity cascade")
cur.execute("truncate table evento restart identity cascade")
cur.execute("truncate table medalla_individual restart identity cascade")
cur.execute("truncate table medalla_grupal restart identity cascade")
cur.execute("truncate table evento_disciplina restart identity cascade")
cur.execute("truncate table entrenador_atleta restart identity cascade")
'''

# Guardar datos de país asociados a atletas
atleta_pais_cache = []
pais_con_medallas_cache = []
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
        #print(info)
        #######################

        atleta_pais_cache.append([atleta_id, atleta_pais_id])

        #cur.execute("insert into atleta values (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
         #          [atleta_id, atleta_nombre, atleta_genero, atleta_nacionalidad, atleta_pais_residencia, atleta_altura, atleta_peso, atleta_fecha_nacimiento, atleta_lugar_nacimiento])
conn.commit()
'''
# Poblar Equipos
with open('./Data/teams.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    i = 0
    for row in reader:
        i+=1
        if i == 1:
            continue
        team_id = row[0]
        team_name = row[1]
        team_gender = row[2]
        team_country = row[3]
        team_discipline = row[6]
        team_event = row[8]
        try:
            athletes_IDS = ast.literal_eval(row[11])
        except (ValueError, SyntaxError) as e:
            print(f"Error al evaluar row[11]: {row[11]} - {e}")
            continue
        athletes_IDS = ast.literal_eval(row[11])
        print(athletes_IDS)
        print(type(athletes_IDS))
        for id in athletes_IDS:
            athlete_id = id
            try:
                int(athlete_id)
                cur.execute("insert into equipo values (%s, %s, %s, %s, %s, %s, %s)", 
                        [team_id, athlete_id, team_name, team_country, team_gender, team_discipline, team_event])
            except ValueError:
                continue 
conn.commit()

# Poblar Entrenador
with open('./Data/coaches.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    i = 0
    for row in reader:
        i+=1
        if i == 1:
            continue

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

        entrenador_nacionalidad = row[6]

        # Podríamos incluir la disciplina que coachea
        cur.execute("insert into entrenador values (%s, %s, %s, %s, %s, %s)",
                   [entrenador_id, entrenador_nombre, entrenador_genero, entrenador_funcion, entrenador_categoria, entrenador_nacionalidad])
conn.commit()
'''
#Poblar Pais
with open('./Data/medals_total.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    i = 0
    for row in reader:
        i+=1
        if i == 1:
            continue
        print(i)

        pais_codigo = row[0]
        pais_oros = row[1]
        pais_platas = row[2]
        pais_bronces = row[3]
        pais_total = row[4] 
        pais_con_medallas_cache.append(pais_codigo)
        
        #cur.execute("insert into pais values (%s, %s, %s, %s, %s)",
         #          [pais_codigo, pais_oros, pais_platas, pais_bronces, pais_total])
conn.commit()
'''
# Poblar disciplina
disciplinas_cache = set()  # Cache para evitar duplicados
with open('./Data/schedules.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        discipline_code = row['discipline_code']
        discipline_name = row['discipline']

        # Verificar si ya se agregó esta disciplina
        if discipline_code not in disciplinas_cache:
            cur.execute("INSERT INTO disciplina (nombre) VALUES (%s)", 
                        (discipline_name,))
            disciplinas_cache.add(discipline_code)
conn.commit()

# Poblar tabla Evento evitando duplicados
evento_cache = set()
with open('./Data/medals.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    i = 0
    for row in reader:
        i+=1
        if i == 1:
            continue

        # Poblar eventos
        evento_disciplina = row[7]
        evento_genero = row[5]
        evento_nombre = evento_disciplina + ' ' + evento_genero 
        evento_ganador = row[3]
        print(evento_nombre)
        # Verificar duplicado
        if evento_nombre not in evento_cache:
            cur.execute("insert into evento values (%s, %s)", [evento_nombre, evento_ganador])
            evento_cache.add(evento_nombre)
        medalla_id = row[1]
        medalla_evento_nombre = row[7] + ' ' + row[5]
        medalla_atleta_id = row[10]
        medalla_tipo = row[0]
        if isinstance(medalla_atleta_id, int):
            cur.execute("insert into medalla_individual values (%s, %s, %s, %s)", 
                   [medalla_id, medalla_evento_nombre, medalla_atleta_id, medalla_tipo])
        else:
            cur.execute("select atleta_id from equipo where id = %s", (medalla_atleta_id, ))
            todosAtletas = cur.fetchall()
            print(todosAtletas)
            print("Los atletas")
            for atleta in todosAtletas:
                print(medalla_evento_nombre)
                cur.execute("insert into medalla_grupal values (%s, %s, %s, %s, %s)", 
                    [medalla_id, atleta, medalla_evento_nombre, medalla_atleta_id, medalla_tipo])
conn.commit()
'''
'''
# Poblar tabla Medalla
with open('./Data/medals.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    i = 0
    for row in reader:
        i+=1
        if i == 1:
            continue
        print(str(i) + 'medalla')
        medalla_id = row[1]
        medalla_evento_nombre = row[7] + ' ' + row[5]
        medalla_atleta_id = row[10]
        medalla_tipo = row[0]
        if isinstance(medalla_atleta_id, int):
            cur.execute("insert into medalla_individual values (%s, %s, %s, %s)", 
                   [medalla_id, medalla_evento_nombre, medalla_atleta_id, medalla_tipo])
        else:
            cur.execute("select atleta_id from equipo where id = %s", (medalla_atleta_id, ))
            todosAtletas = cur.fetchall()
            for atleta in todosAtletas:
                print(medalla_evento_nombre)
                cur.execute("insert into medalla_grupal values (%s, %s, %s, %s, %s)", 
                    [medalla_id, atleta, medalla_evento_nombre, medalla_atleta_id, medalla_tipo])
conn.commit()
'''
'''


# Poblar evento_disciplina
evento_disciplina_cache = set()  # Cache para evitar duplicados

with open('./Data/medals.csv') as medals_file:
    reader = csv.DictReader(medals_file)
    #reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    i = 0
    for row in reader:
        i+=1
        print(str(i) + "evento_disc")
        nombre_evento = row['event'] + ' ' + row['gender'] # Nombre evento
        discipline_code = row['discipline']  # Código disciplina
        phase = row.get('phase', None)  # Fase del evento
        venue = row.get('venue', None)  # Lugar del evento

        # Verificar cache
        if (nombre_evento, discipline_code) not in evento_disciplina_cache:
            # Insertar la relación
            cur.execute("INSERT INTO evento_disciplina (disciplina_id, evento_nombre, phase, venue) VALUES (%s, %s, %s, %s)",
                        (discipline_code, nombre_evento, phase, venue))
            evento_disciplina_cache.add((nombre_evento, discipline_code))  # Añadir al cache
conn.commit()

# Poblar evento_atleta (Relacion Compite_en)
evento_atleta_cache = set()  # Cache para evitar duplicados

with open('./Data/medals.csv') as medals_file:
    medals_reader = csv.DictReader(medals_file)
    i = 0
    for row in medals_reader:
        i += 1
        print(str(i) + "evento_ATLETA")
        nombre_evento = row['event'] + ' ' + row['gender'] # Nombre evento
        codigo_atleta = row['code']  # Código atleta

        # Verificar relación
        if (nombre_evento, codigo_atleta) not in evento_atleta_cache:
            if isinstance(codigo_atleta, int):
                cur.execute("INSERT INTO evento_atleta (evento_nombre, atleta_id) VALUES (%s, %s)",
                        (nombre_evento, codigo_atleta))
            else:
                cur.execute("select atleta_id from equipo where id = %s", (codigo_atleta, ))
                todosAtletas = cur.fetchall()
                for atleta in todosAtletas:
                    cur.execute("insert into evento_equipo (evento_nombre, equipo_id, atleta_id) VALUES (%s, %s, %s)", 
                                (nombre_evento, codigo_atleta, atleta))
            evento_atleta_cache.add((nombre_evento, codigo_atleta))  # Añadir al cache
conn.commit()



# Poblar entrenador_atleta (coaches / athletes)
entrenador_atleta_cache = set()

coaches_data = {}
with open('./Data/coaches.csv') as coaches_file:
    coaches_reader = csv.DictReader(coaches_file)
    i = 0
    for coach in coaches_reader:
        i += 1
        print(str(i)+ "entrenador_atletaaaa")
        coach_code = coach['code']
        coach_discipline = coach['disciplines'].strip("[]").replace("'", "").split(", ")
        coaches_data[coach_code] = coach_discipline
conn.commit()

with open('./Data/athletes.csv') as athletes_file:
    athletes_reader = csv.DictReader(athletes_file)
    i = 0
    for athlete in athletes_reader:
        i += 1
        print(str(i)+ "entrenador_atletaaaa")
        athlete_code = athlete['code']
        athlete_discipline = athlete['disciplines'].strip("[]").replace("'", "").split(", ")

        for coach_code, coach_discipline in coaches_data.items():
            if set(athlete_discipline) & set(coach_discipline):
                if (coach_code, athlete_code) not in entrenador_atleta_cache:
                    cur.execute("INSERT INTO entrenador_atleta (entrenador_id, atleta_id) VALUES (%s, %s)",
                                (coach_code, athlete_code))
                    entrenador_atleta_cache.add((coach_code, athlete_code))

#TEST

# Poblar entrenador_atleta (coaches / athletes)
entrenador_atleta_cache = set()

# Crear un índice por disciplina para los entrenadores
coaches_by_discipline = {}

with open('./Data/coaches.csv') as coaches_file:
    coaches_reader = csv.DictReader(coaches_file)
    for coach in coaches_reader:
        coach_code = coach['code']
        coach_disciplines = coach['disciplines'].strip("[]").replace("'", "").split(", ")

        # Indexar entrenadores por disciplina
        for discipline in coach_disciplines:
            if discipline not in coaches_by_discipline:
                coaches_by_discipline[discipline] = []
            coaches_by_discipline[discipline].append(coach_code)

# Procesar atletas
with open('./Data/athletes.csv') as athletes_file:
    athletes_reader = csv.DictReader(athletes_file)
    i = 0
    for athlete in athletes_reader:
        i += 1
        print(f"{i} - Procesando atleta")

        athlete_code = athlete['code']
        athlete_disciplines = athlete['disciplines'].strip("[]").replace("'", "").split(", ")

        # Encontrar entrenadores para disciplinas del atleta
        possible_coaches = set()
        for discipline in athlete_disciplines:
            if discipline in coaches_by_discipline:
                possible_coaches.update(coaches_by_discipline[discipline])

        # Insertar relaciones entrenador-atleta
        for coach_code in possible_coaches:
            if (coach_code, athlete_code) not in entrenador_atleta_cache:
                cur.execute("INSERT INTO entrenador_atleta (entrenador_id, atleta_id) VALUES (%s, %s)",
                            (coach_code, athlete_code))
                entrenador_atleta_cache.add((coach_code, athlete_code))



'''









# Poblar atleta_pais
i = 0
for dupla in atleta_pais_cache:
    i += 1
    print(str(i)+ "atleta_pais")
    atleta_id = dupla[0]
    pais_id = dupla[1]
    if pais_id in pais_con_medallas_cache:
        cur.execute("insert into atleta_pais values (%s, %s)", [atleta_id, pais_id])
    else:
        cur.execute("insert into pais values (%s, %s, %s, %s, %s)",
                   [pais_id, 0, 0, 0, 0])
        pais_con_medallas_cache.append(pais_id)
        cur.execute("insert into atleta_pais values (%s, %s)", [atleta_id, pais_id])
# Commit changes
conn.commit()

# Close connection
cur.close()
conn.close()