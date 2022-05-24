function ShowTrainingText(){
    var training = document.getElementById('training-text');
    let message = "<span>ENTRENANDO...</span>"
    training.innerHTML = message;

    if (training.style.display == 'none') {
        training.style.display = 'block';
    }
}