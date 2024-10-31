# Estudiantes: Diego Espinoza - Julián Ferreira

import psycopg2
import csv

conn = psycopg2.connect(host="cc3201.dcc.uchile.cl", database="cc3201",
    user="cc3201",
    password="j'<3_cc3201", port="5440")

cur = conn.cursor()

cur.execute("truncate table ochocincouno_superhero restart identity cascade")
cur.execute("truncate table ochocincouno_character restart identity cascade")
cur.execute("truncate table ochocincouno_alter_ego restart identity cascade")
cur.execute("truncate table ochocincouno_work_occupation restart identity cascade")
cur.execute("truncate table ochocincouno_superhero_alter_ego restart identity cascade")
cur.execute("truncate table ochocincouno_superhero_work_occupation restart identity cascade")





alterEgoCache = {}
occupationCache = {}
superhero_occupation_cache = {}
with open('./data.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    i = 0
    for row in reader:
        i += 1
        if i == 1:
            continue
        print(i)
        
        # Superhero
        superhero_name = row[1]
        print(superhero_name)
        # Chequeo de la altura
        if row[18] == "":
            height = None
        else:
            superhero_height = row[18].split(" ")
            if superhero_height[1] == "meters":
                height = int(float(superhero_height[0])*100)
            else:
                height = superhero_height[0]

        if row[20] == "":
            weight = None
        else:
            superhero_weight = row[20].split(" ")
            if superhero_weight[1] == "tons":
                superhero_weight[0] = superhero_weight[0].replace(",", "")
                weight = int(float(superhero_weight[0])*1000)
            else:
                weight = superhero_weight[0]


        alterEgoCache[superhero_name] = []
        cur.execute("insert into ochocincouno_superhero (name, height, weight) values (%s, %s, %s) returning id", 
                    [superhero_name, height, weight])
        superhero_id = cur.fetchone()[0]


        # Character
        character_bio = row[8]
        if character_bio != "":
            cur.execute("insert into ochocincouno_character (superhero_id, biography_name) values (%s, %s)", [superhero_id, character_bio])
        else:
            character_bio = None
            cur.execute("insert into ochocincouno_character (superhero_id, biography_name) values (%s, %s)", [superhero_id, character_bio])

        
        # AlterEgo
        alterEgo = row[9]
        #print(alterEgo)
        if alterEgo != "No alter egos found.":
            alterEgo = alterEgo.replace(";", ",")
            alterEgo = alterEgo.split(",")
            #print(f"Alter spliteao {alterEgo}")
            #print(f"Largo de los alter {len(alterEgo)}")
            # Para cada alter ego del super heroe
            for ego in alterEgo:
                ego = ego.strip()
                ego = ego.replace('"','')
                
                # No existe el alterego para ese superheroe
                if ego not in alterEgoCache[superhero_name]:
                    alterEgoCache[superhero_name].append(ego)
                    cur.execute("insert into ochocincouno_alter_ego (name) values (%s) returning id", [ego])
                    ego_id = cur.fetchone()[0]
                    #Insertar en la tabla de la relacion
                    cur.execute("insert into ochocincouno_superhero_alter_ego (superhero_id, alter_ego_id) values (%s, %s)",
                                [superhero_id, ego_id])

        #Work
        occupation = row[23]
        #Existe la ocupacion
        if occupation != "-":
            superhero_occupation_cache[superhero_name] = []
            occupation = occupation.replace(";", ",")
            occupation = occupation.split(",")
            for work in occupation:
                work = work.lower().strip()
                work = work.replace('"','')

                # No existe el trabajo, por lo que hay que crearlo y agregarlo al cache
                if work not in occupationCache:
                    cur.execute("insert into ochocincouno_work_occupation (name) values (%s) returning id", [work])
                    work_id = cur.fetchone()[0]
                    occupationCache[work] = work_id
                    superhero_occupation_cache[superhero_name].append((superhero_id, work_id))
                # Si existe el trabajo en el cache
                else:
                    work_id = occupationCache[work]

                
                if (superhero_id, work_id) not in superhero_occupation_cache[superhero_name]:
                    #Insertar en la tabla de la relacion
                    cur.execute("insert into ochocincouno_superhero_work_occupation (superhero_id, work_occupation_id) values (%s, %s)",
                                [superhero_id, work_id])



                    #Falta revisar si existe el par ordenado (superhero_id, work_id)
                    


    conn.commit()
    