function ShowTrainingText(){
    var training = document.getElementById('training-text');
    let message = "<span style='background-color: #089de28c;width: 285px;height: 4px;border-radius: 10px;margin-left: 25px;margin-top: 7px;'>ENTRENANDO...</span>";
    training.innerHTML = message;

    if (training.style.display == 'none') {
        training.style.display = 'block';
    }
}