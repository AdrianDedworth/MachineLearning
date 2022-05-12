const expresiones ={
    telefono: /^\d+$/, // Solo números
    fname: /^[a-zA-ZÀ-ÿ\s]{2,50}$/, // Letras y espacios, pueden llevar acentos.
    lname: /^[a-zA-ZÀ-ÿ\s]{2,50}$/,
}

const formulario = document.getElementById("form-add-new");
const inputs = document.querySelectorAll("#fomr-add-new input");

const validarFormulario = (e) => {
    switch(e.target.name){
        case "fname":
            if(expresiones.fname.test(e.target.value)){

            }else{
                
            }
        break;
        case "lname":
        break;
        case "num-cel":
        break;
    }
}

inputs.forEach((input) => {
    input.addEventListener('keyup', validarFormulario);
    input.addEventListener('blur', validarFormulario);
});

formulario.addEventListener('submit', (e) => {
    e.preventDefault();
});