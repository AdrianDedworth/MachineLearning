const existsFile = document.getElementById("uploadFile");
const btnEntrena = document.getElementById("btn-entrena");

function deactivateEntrena(){
    btnEntrena.disabled = true;
    btnEntrena.classList.remove("active");
}

function checkFile(){
    function activateEntrena(){
        btnEntrena.disabled = false;
        btnEntrena.classList.add("active");
    }

    if(existsFile.value.length > 0){
        current_file_path = existsFile.value.split('\\');
        alert("VIDEO -> " + current_file_path[2] + "\nSUBIDO");
        activateEntrena();
    }else{
        alert("->DEBE ELEGIR UN VIDEO \n->FORMATOS ACEPTADOS: mp4, avi, wmv, mpg");
    }
}