const existsFile = document.getElementById("uploadFile");
const btnSubmit = document.getElementById("btn-Accept");

current_file = existsFile.files;

function checkFile(){
    if(current_file.length === 0){
        alert("->DEBE ELEGIR UN VIDEO \n->FORMATOS ACEPTADOS: mp4, avi, wmv, mpg")
    }
}