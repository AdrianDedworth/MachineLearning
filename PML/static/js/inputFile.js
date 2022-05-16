const existsFile = document.getElementById("uploadFile");

function checkFile(){
    if(existsFile.value.length > 0){
        current_file_path = existsFile.value.split('\\');
        alert("VIDEO -> " + current_file_path[2] + "\nSUBIDO");
    }else{
        alert("->DEBE ELEGIR UN VIDEO \n->FORMATOS ACEPTADOS: mp4, avi, wmv, mpg");
    }
}