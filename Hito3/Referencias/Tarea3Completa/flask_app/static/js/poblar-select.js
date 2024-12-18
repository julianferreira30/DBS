const data = [
  {
      "id": 1, "nombre": "Región de Tarapacá",
      "comunas": [
          {"id": 10301, "nombre": "Camiña"},
          {"id": 10302, "nombre": "Huara"},
          {"id": 10303, "nombre": "Pozo Almonte"},
          {"id": 10304, "nombre": "Iquique"},
          {"id": 10305, "nombre": "Pica"},
          {"id": 10306, "nombre": "Colchane"},
          {"id": 10307, "nombre": "Alto Hospicio"}
      ]
  },
  {
      "id": 2, "nombre": "Región de Antofagasta",
      "comunas": [
          {"id": 20101, "nombre": "Tocopilla"},
          {"id": 20102, "nombre": "Maria Elena"},
          {"id": 20201, "nombre": "Ollague"},
          {"id": 20202, "nombre": "Calama"},
          {"id": 20203, "nombre": "San Pedro Atacama"},
          {"id": 20301, "nombre": "Sierra Gorda"},
          {"id": 20302, "nombre": "Mejillones"},
          {"id": 20303, "nombre": "Antofagasta"},
          {"id": 20304, "nombre": "Taltal"}
      ]
  },
  {
      "id": 3, "nombre": "Región de Atacama",
      "comunas": [
          {"id": 30101, "nombre": "Diego de Almagro"},
          {"id": 30102, "nombre": "Chañaral"},
          {"id": 30201, "nombre": "Caldera"},
          {"id": 30202, "nombre": "Copiapo"},
          {"id": 30203, "nombre": "Tierra Amarilla"},
          {"id": 30301, "nombre": "Huasco"},
          {"id": 30302, "nombre": "Freirina"},
          {"id": 30303, "nombre": "Vallenar"},
          {"id": 30304, "nombre": "Alto del Carmen"}
      ]
  },
  {
      "id": 4, "nombre": "Región de Coquimbo",
      "comunas": [
          {"id": 40101, "nombre": "La Higuera"},
          {"id": 40102, "nombre": "La Serena"},
          {"id": 40103, "nombre": "Vicuña"},
          {"id": 40104, "nombre": "Paihuano"},
          {"id": 40105, "nombre": "Coquimbo"},
          {"id": 40106, "nombre": "Andacollo"},
          {"id": 40201, "nombre": "Rio Hurtado"},
          {"id": 40202, "nombre": "Ovalle"},
          {"id": 40203, "nombre": "Monte Patria"},
          {"id": 40204, "nombre": "Punitaqui"},
          {"id": 40205, "nombre": "Combarbala"}
      ]
  },
  {
      "id": 5, "nombre": "Región de Valparaíso",
      "comunas": [
          {"id": 50101, "nombre": "Petorca"},
          {"id": 50102, "nombre": "Cabildo"},
          {"id": 50103, "nombre": "Papudo"},
          {"id": 50104, "nombre": "La Ligua"},
          {"id": 50105, "nombre": "Zapallar"},
          {"id": 50201, "nombre": "Putaendo"},
          {"id": 50202, "nombre": "Santa Maria"},
          {"id": 50203, "nombre": "San Felipe"},
          {"id": 50204, "nombre": "Pencahue"},
          {"id": 50205, "nombre": "Catemu"},
          {"id": 50206, "nombre": "Llay Llay"},
          {"id": 50301, "nombre": "Nogales"},
          {"id": 50302, "nombre": "La Calera"},
          {"id": 50303, "nombre": "Hijuelas"},
          {"id": 50304, "nombre": "La Cruz"},
          {"id": 50305, "nombre": "Quillota"},
          {"id": 50306, "nombre": "Olmue"},
          {"id": 50307, "nombre": "Limache"},
          {"id": 50401, "nombre": "Los Andes"},
          {"id": 50402, "nombre": "Rinconada"},
          {"id": 50403, "nombre": "Calle Larga"},
          {"id": 50404, "nombre": "San Esteban"},
          {"id": 50501, "nombre": "Puchuncavi"},
          {"id": 50502, "nombre": "Quintero"},
          {"id": 50503, "nombre": "Viña del Mar"},
          {"id": 50504, "nombre": "Villa Alemana"},
          {"id": 50505, "nombre": "Quilpue"},
          {"id": 50506, "nombre": "Valparaiso"},
          {"id": 50507, "nombre": "Juan Fernandez"},
          {"id": 50508, "nombre": "Casablanca"},
          {"id": 50509, "nombre": "Concon"},
          {"id": 50601, "nombre": "Isla de Pascua"},
          {"id": 50701, "nombre": "Algarrobo"},
          {"id": 50702, "nombre": "El Quisco"},
          {"id": 50703, "nombre": "El Tabo"},
          {"id": 50704, "nombre": "Cartagena"},
          {"id": 50705, "nombre": "San Antonio"},
          {"id": 50706, "nombre": "Santo Domingo"}
      ]
  },
  {
      "id": 6, "nombre": "Región del Libertador Bernardo O'Higgins",
      "comunas": [
          {"id": 60101, "nombre": "Mostazal"},
          {"id": 60102, "nombre": "Codegua"},
          {"id": 60103, "nombre": "Graneros"},
          {"id": 60104, "nombre": "Machali"},
          {"id": 60105, "nombre": "Rancagua"},
          {"id": 60106, "nombre": "Olivar"},
          {"id": 60107, "nombre": "Doñihue"},
          {"id": 60108, "nombre": "Requinoa"},
          {"id": 60109, "nombre": "Coinco"},
          {"id": 60110, "nombre": "Coltauco"},
          {"id": 60111, "nombre": "Quinta Tilcoco"},
          {"id": 60112, "nombre": "Las Cabras"},
          {"id": 60113, "nombre": "Rengo"},
          {"id": 60114, "nombre": "Peumo"},
          {"id": 60115, "nombre": "Pichidegua"},
          {"id": 60116, "nombre": "Malloa"},
          {"id": 60117, "nombre": "San Vicente"}
      ]
  },
  {
      "id": 7, "nombre": "Región del Maule",
      "comunas": [
          {"id": 70101, "nombre": "Teno"},
          {"id": 70102, "nombre": "Romeral"},
          {"id": 70103, "nombre": "Rauco"},
          {"id": 70104, "nombre": "Curico"},
          {"id": 70105, "nombre": "Sagrada Familia"},
          {"id": 70106, "nombre": "Hualañe"},
          {"id": 70107, "nombre": "Vichuquen"},
          {"id": 70108, "nombre": "Molina"},
          {"id": 70109, "nombre": "Licanten"}
      ]
  },
  {
      "id": 8, "nombre": "Región del Biobío",
      "comunas": [
          {"id": 80201, "nombre": "Tome"},
          {"id": 80202, "nombre": "Florida"},
          {"id": 80203, "nombre": "Penco"},
          {"id": 80204, "nombre": "Talcahuano"},
          {"id": 80205, "nombre": "Concepcion"},
          {"id": 80206, "nombre": "Hualqui"},
          {"id": 80207, "nombre": "Coronel"},
          {"id": 80208, "nombre": "Lota"},
          {"id": 80209, "nombre": "Santa Juana"},
          {"id": 80210, "nombre": "Chiguayante"},
          {"id": 80211, "nombre": "San Pedro de la Paz"},
          {"id": 80212, "nombre": "Hualpen"}
      ]
  },
  {
      "id": 9, "nombre": "Región de La Araucanía",
      "comunas": [
          {"id": 90101, "nombre": "Renaico"},
          {"id": 90102, "nombre": "Angol"},
          {"id": 90103, "nombre": "Collipulli"},
          {"id": 90104, "nombre": "Los Sauces"},
          {"id": 90105, "nombre": "Puren"},
          {"id": 90106, "nombre": "Ercilla"},
          {"id": 90107, "nombre": "Lumaco"},
          {"id": 90108, "nombre": "Victoria"},
          {"id": 90109, "nombre": "Traiguen"}
      ]
  },
  {
      "id": 10, "nombre": "Región de Los Lagos",
      "comunas": [
          {"id": 100201, "nombre": "San Pablo"},
          {"id": 100202, "nombre": "San Juan"},
          {"id": 100203, "nombre": "Osorno"},
          {"id": 100204, "nombre": "Puyehue"},
          {"id": 100205, "nombre": "Rio Negro"},
          {"id": 100206, "nombre": "Purranque"},
          {"id": 100207, "nombre": "Puerto Octay"}
      ]
  },
  {
    "id": 11, "nombre": "Región Aisén del General Carlos Ibáñez del Campo",
    "comunas": [
        {"id": 110101, "nombre": "Guaitecas"},
        {"id": 110102, "nombre": "Cisnes"},
        {"id": 110103, "nombre": "Aysen"},
        {"id": 110201, "nombre": "Coyhaique"},
        {"id": 110202, "nombre": "Lago Verde"},
        {"id": 110301, "nombre": "Rio Ibañez"},
        {"id": 110302, "nombre": "Chile Chico"},
        {"id": 110401, "nombre": "Cochrane"},
        {"id": 110402, "nombre": "Tortel"},
        {"id": 110403, "nombre": "O'Higgins"}
    ]
},
{
    "id": 12, "nombre": "Región de Magallanes y la Antártica Chilena",
    "comunas": [
        {"id": 120101, "nombre": "Torres del Paine"},
        {"id": 120102, "nombre": "Puerto Natales"},
        {"id": 120201, "nombre": "Laguna Blanca"},
        {"id": 120202, "nombre": "San Gregorio"},
        {"id": 120203, "nombre": "Rio Verde"},
        {"id": 120204, "nombre": "Punta Arenas"},
        {"id": 120301, "nombre": "Porvenir"},
        {"id": 120302, "nombre": "Primavera"},
        {"id": 120303, "nombre": "Timaukel"},
        {"id": 120401, "nombre": "Antartica"}
    ]
},
{
    "id": 13, "nombre": "Región Metropolitana de Santiago",
    "comunas": [
        {"id": 130101, "nombre": "Tiltil"},
        {"id": 130102, "nombre": "Colina"},
        {"id": 130103, "nombre": "Lampa"},
        {"id": 130201, "nombre": "Conchali"},
        {"id": 130202, "nombre": "Quilicura"},
        {"id": 130203, "nombre": "Renca"},
        {"id": 130204, "nombre": "Las Condes"},
        {"id": 130205, "nombre": "Pudahuel"},
        {"id": 130206, "nombre": "Quinta Normal"},
        {"id": 130207, "nombre": "Providencia"},
        {"id": 130208, "nombre": "Santiago"},
        {"id": 130209, "nombre": "La Reina"},
        {"id": 130210, "nombre": "Ñuñoa"},
        {"id": 130211, "nombre": "San Miguel"},
        {"id": 130212, "nombre": "Maipú"},
        {"id": 130213, "nombre": "La Cisterna"},
        {"id": 130214, "nombre": "La Florida"},
        {"id": 130215, "nombre": "La Granja"},
        {"id": 130216, "nombre": "Independencia"},
        {"id": 130217, "nombre": "Huechuraba"},
        {"id": 130218, "nombre": "Recoleta"},
        {"id": 130219, "nombre": "Vitacura"},
        {"id": 130220, "nombre": "Lo Barnechea"},
        {"id": 130221, "nombre": "Macul"},
        {"id": 130222, "nombre": "Peñalolén"},
        {"id": 130223, "nombre": "San Joaquín"},
        {"id": 130224, "nombre": "La Pintana"},
        {"id": 130225, "nombre": "San Ramón"},
        {"id": 130226, "nombre": "El Bosque"},
        {"id": 130227, "nombre": "Pedro Aguirre Cerda"},
        {"id": 130228, "nombre": "Lo Espejo"},
        {"id": 130229, "nombre": "Estación Central"},
        {"id": 130230, "nombre": "Cerrillos"},
        {"id": 130231, "nombre": "Lo Prado"},
        {"id": 130232, "nombre": "Cerro Navia"}
    ]
},
{
    "id": 14, "nombre": "Región de Los Ríos",
    "comunas": [
        {"id": 100101, "nombre": "Lanco"},
        {"id": 100102, "nombre": "Mariquina"},
        {"id": 100103, "nombre": "Panguipulli"},
        {"id": 100104, "nombre": "Mafil"},
        {"id": 100105, "nombre": "Valdivia"},
        {"id": 100106, "nombre": "Los Lagos"},
        {"id": 100107, "nombre": "Corral"},
        {"id": 100108, "nombre": "Paillaco"},
        {"id": 100109, "nombre": "Futrono"},
        {"id": 100110, "nombre": "Lago Ranco"},
        {"id": 100111, "nombre": "La Unión"}
    ]
},
{
    "id": 15, "nombre": "Región Arica y Parinacota",
    "comunas": [
        {"id": 10101, "nombre": "Gral. Lagos"},
        {"id": 10102, "nombre": "Putre"},
        {"id": 10201, "nombre": "Arica"},
        {"id": 10202, "nombre": "Camarones"}
    ]
},
{
    "id": 16, "nombre": "Región del Ñuble",
    "comunas": [
        {"id": 80101, "nombre": "Cobquecura"},
        {"id": 80102, "nombre": "Ñiquen"},
        {"id": 80103, "nombre": "San Fabian"},
        {"id": 80104, "nombre": "San Carlos"},
        {"id": 80105, "nombre": "Quirihue"},
        {"id": 80106, "nombre": "Ninhue"},
        {"id": 80107, "nombre": "Trehuaco"},
        {"id": 80108, "nombre": "San Nicolas"},
        {"id": 80109, "nombre": "Coihueco"},
        {"id": 80110, "nombre": "Chillan"},
        {"id": 80111, "nombre": "Portezuelo"},
        {"id": 80112, "nombre": "Pinto"},
        {"id": 80113, "nombre": "Coelemu"},
        {"id": 80114, "nombre": "Bulnes"},
        {"id": 80115, "nombre": "San Ignacio"},
        {"id": 80116, "nombre": "Ranquil"},
        {"id": 80117, "nombre": "Quillon"},
        {"id": 80118, "nombre": "El Carmen"},
        {"id": 80119, "nombre": "Pemuco"},
        {"id": 80120, "nombre": "Yungay"},
        {"id": 80121, "nombre": "Chillan Viejo"}
    ]
}
  
]


const tipos = [
  "Pantalla", "Notebook", "Tablet", "Celular", "Consola", "Mouse", "Teclado",
  "Impresora", "Parlante", "Audífonos", "Otro"
]

const funcionamiento = [
  "Funciona perfecto", "Funciona a medias", "No funciona"
]

//RELACIONADO A DISPOSITIVOS
const poblarDispositivos = () => {
  let dispositivosSelect = document.getElementById("select-tipo-dispositivo");
  for (const dispositivo of tipos) {
    let option = document.createElement("option");
    option.value = dispositivo;
    option.text = dispositivo;
    dispositivosSelect.appendChild(option);
  }
  
};

const poblarFuncionamiento = () => {
  let funcionamientoSelect = document.getElementById("select-funcionamiento");
  for (const opcion of funcionamiento) {
    let option = document.createElement("option");
    option.value = opcion;
    option.text = opcion;
    funcionamientoSelect.appendChild(option);
  }
  
};

// RELACIONADO A REGIONES

// Llenar el desplegable de regiones
const regionesSelect = document.getElementById('select-region');
const comunasSelect = document.getElementById('select-comuna');
const poblarRegiones = () => {
  data.forEach(region => {
    const option = document.createElement("option");
    option.value = region.id;
    option.textContent = region.nombre;
    regionesSelect.appendChild(option);
  });
}
const updateComunas = () => {
// Obtener el ID de la regi├│n seleccionada
const selectedRegionId = parseInt(regionesSelect.value);
  
// Limpiar las opciones existentes
comunasSelect.innerHTML = '<option value="">Seleccione comuna</option>';

// Buscar la regi├│n seleccionada en los datos
const selectedRegion = data.find(region => region.id === selectedRegionId);

if (selectedRegion) {
    // Agregar las opciones de comunas
    selectedRegion.comunas.forEach(comuna => {
        const option = document.createElement("option");
        option.value = comuna.id;
        option.textContent = comuna.nombre;
        comunasSelect.appendChild(option);
    });
  }
};








// Manejar el cambio de regi├│n
regionesSelect.addEventListener('change', updateComunas);

const poblarDesplegables = () => {
  poblarDispositivos();
  poblarFuncionamiento();
  poblarRegiones();
}
 // window.onload = poblarDesplegables;
document.addEventListener("DOMContentLoaded", poblarDesplegables);  // Ejecutar cuando el DOM esté listo
