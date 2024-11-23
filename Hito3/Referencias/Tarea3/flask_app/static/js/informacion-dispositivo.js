    const validateName = (name) => {
        if(!name) return false;
        let lengthValid = name.trim().length >= 3 && name.trim().length <= 80;
        return lengthValid;
    }

    const validateComment = (comment) => {
        if(!comment) return false;
        let lengthValid = comment.trim().length >= 5 && comment.trim().length <= 200;
        return lengthValid;
    }

  const validateForm = () => {
    // obtener elementos del DOM usando el nombre del formulario.
    let myForm = document.forms["myForm"];
    let name = myForm["nombre"].value;
    let comentario = myForm["comentario"].value;
  
    // variables auxiliares de validación y función.
    let invalidInputs = [];
    let isValid = true;
    
    const setInvalidInput = (inputName) => {
      invalidInputs.push(inputName);
      isValid &&= false;
    };
    
    // lógica de validación
    if (!validateName(name)) {
      setInvalidInput("Nombre");
    }
    if (!validateComment(comentario)) {
      setInvalidInput("Comentario");
    }
    
    
    
    // finalmente mostrar la validaci├│n
    let validationBox = document.getElementById("val-box");
    let validationMessageElem = document.getElementById("val-msg");
    let validationListElem = document.getElementById("val-list");
    let formContainer = document.querySelector(".main-container");
  
    if (!isValid) {
      validationListElem.textContent = "";
      // agregar elementos inv├ílidos al elemento val-list.
      for (input of invalidInputs) {
        let listElement = document.createElement("li");
        listElement.innerText = input;
        validationListElem.append(listElement);
      }
      // establecer val-msg
      validationMessageElem.innerText = "Los siguientes campos son inválidos:";
      
      // aplicar estilos de error
      validationBox.style.backgroundColor = "#ffdddd";
      validationBox.style.borderLeftColor = "#f44336";
      
      // hacer visible el mensaje de validaci├│n
      validationBox.hidden = false;
      
    } else {
      // Ocultar el formulario
      myForm.style.display = "none";
      document.getElementById("submit-btn").style.display = "none";
      document.getElementById("add-form").style.display = "none";
     
  
      // establecer mensaje de ├®xito
      validationMessageElem.innerText = "Se agregó el comentario correctamente.";
      validationListElem.textContent = "";
  
      // aplicar estilos de ├®xito
      validationBox.style.backgroundColor = "#ddffdd";
      validationBox.style.borderLeftColor = "#4CAF50";
  
  
      // hacer visible el mensaje de validaci├│n
      validationBox.hidden = false;
    }
  };



  let commentBtn = document.getElementById("comentario-btn");
  commentBtn.addEventListener("click", validateForm);  

  document.addEventListener('DOMContentLoaded', () => {
    // Seleccionar todas las imágenes con la clase "macbookImage"
    const images = document.querySelectorAll('.img640');

    // Agregar un evento a cada imagen
    images.forEach((image) => {
        image.addEventListener('click', function() {
            document.getElementById('image-overlay').style.display = 'flex'; // Muestra el overlay con la imagen
        
        
            document.getElementById('image-overlay-img').src = this.src;
          });
    });

    // Evento para cerrar el overlay
    document.getElementById('image-overlay').addEventListener('click', function() {
        this.style.display = 'none'; // Oculta el overlay cuando se hace clic fuera de la imagen
    });
});