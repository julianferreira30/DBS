import pymysql
import json

DB_NAME = "tarea2"
DB_USERNAME = "cc5002" #cc5002
DB_PASSWORD = "programacionweb" #programacionweb
DB_HOST = "localhost"
DB_PORT = 3306
DB_CHARSET = "utf8"

#with open('database/querys.json', 'r') as querys:
#	QUERY_DICT = json.load(querys)

# -- conn ---

def get_conn():
	conn = pymysql.connect(
		db=DB_NAME,
		user=DB_USERNAME,
		passwd=DB_PASSWORD,
		host=DB_HOST,
		port=DB_PORT,
		charset=DB_CHARSET
	)
	return conn

# -- querys --

def get_device_by_ContactId(id):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute("SELECT id, contacto_id, nombre, descripcion, tipo, anos_uso, estado FROM dispositivo WHERE contacto_id=id")
	return cursor.fetchall()

def create_contact(name, email, phone, comuna, date):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute("INSERT INTO contacto (nombre, email, celular, comuna_id, fecha_creacion) VALUES (%s, %s, %s, %s, %s)" 
				, (name, email, phone, comuna, date))
	conn.commit()
	return cursor.lastrowid

def create_device(contact_id, name, desc, dev_type, years, status):
	# INSERT INTO dispositivo (contacto_id, nombre, descripcion, tipo, anos_uso, estado) VALUES (?,?,?,?,?,?)
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute("INSERT INTO dispositivo (contacto_id, nombre, descripcion, tipo, anos_uso, estado) VALUES (%s, %s, %s, %s, %s, %s)" 
				, (contact_id, name, desc, dev_type, years, status))
	conn.commit()
	return cursor.lastrowid

def create_file(file_route, filename, device_id):
	conn = get_conn()
	cursor = conn.cursor()
	#INSERT INTO archivo (ruta_archivo, nombre_archivo, dispositivo_id) VALUES (?,?,?)
	cursor.execute("INSERT INTO archivo (ruta_archivo, nombre_archivo, dispositivo_id) VALUES (%s, %s, %s)" 
				, (file_route, filename, device_id))
	
	conn.commit()
	return cursor.lastrowid

def create_comment(nombre, texto, fecha, dispositivo_id):
	conn = get_conn()
	cursor = conn.cursor()
	#cursor.execute(f"INSERT INTO comentario (nombre, texto, fecha, dispositivo_id) VALUES ({nombre}, {texto}, {fecha}, {dispositivo_id})")
	cursor.execute("INSERT INTO comentario (nombre, texto, fecha, dispositivo_id) VALUES (%s, %s, %s, %s)" 
				, (nombre, texto, fecha, dispositivo_id))
	conn.commit()
	return cursor.lastrowid

def get_contacto_by_id(id):
	conn = get_conn()
	cursor = conn.cursor()
	#
	# cursor.execute(f"SELECT id, nombre, email, celular, comuna_id, fecha_creacion FROM contacto WHERE id={id}")
	cursor.execute("SELECT id, nombre, email, celular, comuna_id, fecha_creacion FROM contacto WHERE id=%s", (id,))
	return cursor.fetchone()

def get_comuna_by_id(id):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute("SELECT id, nombre, region_id FROM comuna WHERE id=%s", (id,))
	return cursor.fetchone()

def get_comuna_by_nombre(nombre):
	conn = get_conn()
	cursor = conn.cursor()
	#cursor.execute(f"SELECT id, nombre, region_id FROM comuna WHERE nombre={nombre}")
	cursor.execute("SELECT id, nombre, region_id FROM comuna WHERE nombre=%s", (nombre,))
	return cursor.fetchone()

def get_region_by_id(id):
	conn = get_conn()
	cursor = conn.cursor()
	#cursor.execute(f"SELECT id, nombre FROM region WHERE id={id}")
	cursor.execute("SELECT id, nombre FROM region WHERE id=%s", (id,))
	return cursor.fetchone()

def get_devices():
	conn = get_conn()
	cursor = conn.cursor()
	#cursor.execute("SELECT id, contacto_id, nombre, descripcion, tipo, anos_uso, estado FROM dispositivo ORDER BY id DESC LIMIT 0, 5")
	cursor.execute("SELECT id, contacto_id, nombre, descripcion, tipo, anos_uso, estado FROM dispositivo ORDER BY id DESC LIMIT 0, 5")
	devices = cursor.fetchall()
	return devices

def get_all_devices():
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute("SELECT id, contacto_id, nombre, descripcion, tipo, anos_uso, estado FROM dispositivo")
	devices = cursor.fetchall()
	return devices

def get_regiones():
	conn = get_conn()
	cursor = conn.cursor()
	#cursor.execute("SELECT id, nombre FROM region")
	cursor.execute("SELECT id, nombre FROM region")
	regiones = cursor.fetchall()
	return regiones

def get_image_by_device_id(device_id):
	conn = get_conn()
	cursor = conn.cursor()
	#cursor.execute(f"SELECT id, ruta_archivo, nombre_archivo FROM archivo WHERE dispositivo_id={device_id}")
	cursor.execute("SELECT id, ruta_archivo, nombre_archivo FROM archivo WHERE dispositivo_id=%s", (device_id,))
	image = cursor.fetchall()
	return image

def get_contact_comuna_by_contact_id(contact_id):
	conn = get_conn()
	cursor = conn.cursor()
	#cursor.execute(f"SELECT nombre FROM contacto WHERE id={contact_id}")
	cursor.execute("SELECT comuna_id FROM contacto WHERE id=%s", (contact_id,))
	comuna = cursor.fetchone()
	return comuna

def get_contact_id():
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute("SELECT contacto_id FROM contacto WHERE fecha_creacion = date")
	contact = cursor.fetchone()
	return contact

def get_device_by_id(device_id):
	conn = get_conn()
	cursor = conn.cursor()
	#cursor.execute(f"SELECT id, contacto_id, nombre, descripcion, tipo, anos_uso, estado FROM dispositivo WHERE id={device_id}")
	cursor.execute("SELECT id, contacto_id, nombre, descripcion, tipo, anos_uso, estado FROM dispositivo WHERE id=%s", (device_id,))
	device = cursor.fetchone()
	return device

def get_comments_by_device_id(device_id):
	conn = get_conn()
	cursor = conn.cursor()
	#cursor.execute(f"SELECT id, nombre, texto, fecha FROM comentario WHERE dispositivo_id={device_id}")
	cursor.execute("SELECT id, nombre, texto, fecha FROM comentario WHERE dispositivo_id=%s", (device_id,))
	comments = cursor.fetchall()
	return comments


def get_grafico_contactos_data():
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute("SELECT co. nombre, COUNT(c.id) \
					FROM contacto c JOIN dispositivo d \
					ON c.id = d.contacto_id \
					RIGHT JOIN comuna co \
					ON c.comuna_id = co.id \
					GROUP BY co.nombre")
	return cursor.fetchall()

def get_grafico_dispositivos_data():
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute("SELECT d.tipo, COUNT(d.id) \
					FROM dispositivo d \
					GROUP BY d.tipo")
	return cursor.fetchall()