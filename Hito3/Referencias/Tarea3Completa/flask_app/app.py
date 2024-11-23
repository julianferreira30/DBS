from flask import Flask, request, render_template, redirect, url_for, session, jsonify
from flask_cors import cross_origin
from utils.validations import validate_donation, validate_img, validate_comment, validate_contact
from database import db
from werkzeug.utils import secure_filename
import hashlib
import filetype
import os
from datetime import datetime

UPLOAD_FOLDER = 'static/uploads'



app = Flask(__name__)


app.secret_key = "s3cr3t_k3y"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER




# --- Routes ---
@app.route("/", methods=["GET"])
def index():
    return render_template("index/index.html")

@app.route('/botones-index', methods=['POST'])
def botones_index():
    # Obtener la acción del formulario
    action = request.form.get('action')

    # Redirigir en función del valor de "action"
    if action == 'agregar_donacion':
        return redirect(url_for('agregar_donacion'))  # Redirige a la página de agregar donación
    elif action == 'ver_dispositivos':
        return redirect(url_for('ver_dispositivos'))
    elif action == 'grafico_contactos':
        return redirect(url_for('grafico_contactos')) # CREAR APP ROUTE PARA ESTA FUNCION
    elif action == 'grafico_dispositivos':
        return redirect(url_for('grafico_dispositivos')) # CREAR APP ROUTE PARA ESTA FUNCION

@app.route("/grafico-contactos", methods=["GET"])
def grafico_contactos():
    return render_template("donations/grafico-contactos.html")

@app.route("/get-grafico-contactos", methods=["GET"])
@cross_origin(origin="127.0.0.1", supports_credentials=True)
def get_grafico_contactos():
    data = db.get_grafico_contactos_data()
    data = [{"comuna": row[0], "cantidad": row[1]} for row in data if row[1] > 0]
    return jsonify(data)


@app.route("/grafico-dispositivos", methods=["GET"])
def grafico_dispositivos():
    return render_template("donations/grafico-dispositivos.html")

@app.route("/get-grafico-dispositivos", methods=["GET"])
@cross_origin(origin="127.0.0.1", supports_credentials=True)
def get_grafico_dispositivos():
    data = db.get_grafico_dispositivos_data()
    data = [{"tipo": row[0], "cantidad": row[1]} for row in data] 
    return jsonify(data)







@app.route("/ver-dispositivos", methods=["GET"])
def ver_dispositivos():
    # get devices
     # Número de dispositivos por página
    items_per_page = 5
    
    # Obtener el número de la página actual, por defecto es la 1 si no se proporciona el parámetro
    page = request.args.get('page', 1, type=int)
    
    # Obtener todos los dispositivos de la base de datos
    all_devices = db.get_all_devices()
    
    # Calcular el total de páginas
    total_devices = len(all_devices)
    total_pages = (total_devices + items_per_page - 1) // items_per_page
    print("total_devices: ", total_devices)
    
    # Obtener los dispositivos correspondientes a la página actual
    start = (page - 1) * items_per_page
    end = start + items_per_page
    devices_on_page = all_devices[start:end]




    data = []
    for device in devices_on_page:
        device_id ,contact_id, device_name, device_desc, device_type, device_years, device_condition = device
        print(f"device_id: {device_id}")
        images = db.get_image_by_device_id(device_id)
        print(f"images: {images}")
        if images != ():
            img_id, img_route, img_filename = images[0] # Me quedo con la primera imagen asociada al disp
        else:
            img_filename = 'default.jpg'
        contact_comuna = db.get_contact_comuna_by_contact_id(contact_id)
        contact_comuna = db.get_comuna_by_id(contact_comuna)[1]
        
        ### CHECKPOINT 
        img_filename = f"uploads/{img_filename}"
        data.append({
            "tipo": device_type,
            "nombre": device_name,
            "estado": device_condition,
            "comuna": contact_comuna,
            "path_image": url_for('static', filename=img_filename),
            "id": device_id
        })
    
    return render_template("donations/ver-dispositivos.html", 
                           data=data, page=page, total_pages=total_pages)


@app.route("/agregar-donacion", methods=["GET", "POST"])
def agregar_donacion():
    # Obtener los datos del donante
    if request.method == "GET":
        return render_template("donations/agregar-donacion.html")
          
    nombre_donante = request.form.get("nombre")
    email_donante = request.form.get("email")
    telefono_donante = request.form.get("phone")
    region_donante = request.form.get("select-region")
    comuna_donante = request.form.get("select-comuna")
    fecha_actual = datetime.now()
    comuna_donante_id = db.get_comuna_by_nombre(comuna_donante)
    
    # si la validación es correcta, guardar los datos en la base de datos:
    if validate_contact(nombre_donante, email_donante, telefono_donante):
        
        # Crear contacto
        contact_id = db.create_contact(nombre_donante, email_donante, 
                            telefono_donante, comuna_donante, fecha_actual)
        
        dispositivos = []
        for key in request.form:
            if key.startswith('name-dispositivo'):
                # Obtener el índice único del dispositivo (por ejemplo, si es 'name-dispositivo-0')
                print(f"comuna_donante: {comuna_donante}")

                # Extraer la información del dispositivo
                unique_id = key.split('-')[-1]
                
                if unique_id != "dispositivo":
                    print(f"unique_id: {unique_id}")
                    dispositivo = {
                        'nombre': request.form.get(f'name-dispositivo-{unique_id}'),
                        'descripcion': request.form.get(f'descripcion-dispositivo-{unique_id}'),
                        'tipo': request.form.get(f'select-tipo-dispositivo-{unique_id}'),
                        'annos_uso': request.form.get(f'annos-uso-{unique_id}'),
                        'estado_funcionamiento': request.form.get(f'select-funcionamiento-{unique_id}'),
                        'imagenes': []
                    }
                    archivos = request.files.getlist(f'files-{unique_id}')
                else:
                    dispositivo = {
                        'nombre': request.form.get(f'name-dispositivo'),
                        'descripcion': request.form.get(f'descripcion-dispositivo'),
                        'tipo': request.form.get(f'select-tipo-dispositivo'),
                        'annos_uso': request.form.get(f'annos-uso'),
                        'estado_funcionamiento': request.form.get(f'select-funcionamiento'),
                        'imagenes': []
                    }
                    archivos = request.files.getlist(f'files')
                
                # Agregar dispositivo a la db
                print("AAAAA")
                print(dispositivo['nombre'])
                device_id = db.create_device(contact_id, dispositivo['nombre'], dispositivo['descripcion'], dispositivo['tipo'], 
                                  dispositivo['annos_uso'], dispositivo['estado_funcionamiento'])
                
                
                
                
                # Procesar las imágenes 


                for archivo in archivos:
                    if archivo.filename != '' and validate_img(archivo):
                        print(f"archivo, {archivo}")
                        # Generar nombre único para el archivo
                        _filename = hashlib.sha256(
                            secure_filename(archivo.filename)
                            .encode("utf-8")
                            ).hexdigest()
                        _extension = filetype.guess(archivo).extension
                        img_filename = f"{_filename}.{_extension}"

                        # Guardar el archivo
                        archivo.save(os.path.join(app.config["UPLOAD_FOLDER"], img_filename))
                        dispositivo['imagenes'].append(img_filename)

                        # Guardar la imagen en la base de datos
                        db.create_file(os.path.join(app.config["UPLOAD_FOLDER"], img_filename), img_filename, device_id)

                

        # Cargar a la pagina principal
        return redirect(url_for("index"))

@app.route('/dispositivo/<int:dispositivo_id>', methods=["GET", "POST"])
def informacion_dispositivos(dispositivo_id):
    if request.method == "POST":
        # Procesar la información del formulario
        comment_fecha = datetime.now()
        comment_nombre = request.form.get("nombre")
        comment_text = request.form.get("comentario")
        if validate_comment(comment_nombre, comment_text):
            db.create_comment(comment_nombre, comment_text, comment_fecha, dispositivo_id)
            return redirect(url_for("informacion_dispositivos", dispositivo_id=dispositivo_id))       
    
    device_id ,contact_id, device_name, device_desc, device_type, device_years, device_condition = db.get_device_by_id(dispositivo_id)
    _, contact_name, contact_email, contact_phone, contact_comuna, contact_date = db.get_contacto_by_id(contact_id)
    _, comuna_nombre, region_id = db.get_comuna_by_id(contact_comuna)
    _, region_name = db.get_region_by_id(region_id)
    
    images = db.get_image_by_device_id(dispositivo_id)
    data = []
    data.append({
            "tipo": device_type,
            "nombre_disp": device_name,
            "estado": device_condition,
            "descripcion": device_desc,
            "annos_uso": device_years,
            "comuna": comuna_nombre,
            "region": region_name,
            "email": contact_email,
            "telefono": contact_phone,
            "nombre_contacto": contact_name,
            "path_image": [],
            "id": dispositivo_id
        })
    for img in images:
        img_id, img_route, img_filename = img
        img_filename = f"uploads/{img_filename}"
        data[0]["path_image"].append(url_for('static', filename=img_filename))
    
    
    comentarios = []
    for comment in db.get_comments_by_device_id(dispositivo_id):
        _, comment_name, comment_text, comment_date = comment
        comentarios.append({
            "nombre": comment_name,
            "texto": comment_text,
            "fecha": comment_date
        })


    # Verificar si el dispositivo existe
    if device_id:
        return render_template('donations/informacion-dispositivo.html', data=data, comentarios=comentarios)
    else:
        return "Dispositivo no encontrado", 404

if __name__ == "__main__":
    app.run(debug=True)
