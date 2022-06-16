var loader = function(e){
    let file = e.target.files;
    let show = "<span style='background-color: transparent;'>Ha Elegido: </span>" + file[0].name;

    let output = document.getElementById("lbluploadFile");
    output.innerHTML = show;
};

//event listener

let fileInput = document.getElementById("uploadFile");
fileInput.addEventListener("change", loader);