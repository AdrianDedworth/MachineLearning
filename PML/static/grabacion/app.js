///Prueba1

'use strict';

/* globals MediaRecorder */


var downloadButton = document.querySelector("button#download");

downloadButton.addEventListener('click', () => {
  const blob = new Blob(recordedBlobs, { type: 'video/mp4' });
  const url = window.URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.style.display = 'none';
  a.href = url;
  a.download = 'test.mp4';
  document.body.appendChild(a);
  a.click();
  setTimeout(() => {
    document.body.removeChild(a);
    window.URL.revokeObjectURL(url);
  }, 100);
});



let currentStream;
var facingMode = "user";
var video = document.getElementById('video');
var button = document.getElementById('button');
var select = document.getElementById('select');
var icono = document.getElementById('icono');
var nombre = document.getElementById("nombre");
var selected;
var label;
var button1 = document.getElementById("button1");

function stopMediaTracks(stream) {
  stream.getTracks().forEach(track => {
    track.stop();
  });
}


function gotDevices(mediaDevices) {
  select.innerHTML = '';
  select.appendChild(document.createElement('option'));
  let count = 1;
  mediaDevices.forEach(mediaDevice => {
    if (mediaDevice.kind == 'videoinput') {
      const option = document.createElement('option');
      option.value = mediaDevice.deviceId;
      label = mediaDevice.label && `camara ${count++}`
      const textNode = document.createTextNode(label);

      option.appendChild(textNode);
      select.appendChild(option);
    }

  });
}

function activarcaja() {
  document.getElementById("nombre").disabled = false;

}


function desactivarcaja() {
  document.getElementById("nombre").disabled = true;
  var contenido = document.getElementById("nombre").value;
  var textodata2 = document.getElementById("select");
  textodata2.options[textodata2.selectedIndex].text = contenido
}


function seleccioncamara() {

  if (typeof currentStream !== 'undefined') {
    stopMediaTracks(currentStream);
  }
  const videoConstraints = {};
  if (select.value === '') {
    videoConstraints.facingMode = 'environment';

  } else {
    videoConstraints.deviceId = { exact: select.value };
    
    //nombre superior
    var textodata = document.getElementById("select");
    selected = textodata.options[textodata.selectedIndex].text;
    document.getElementById("nombre").value = selected;


  }

  //boton cambiar 

  // button1.addEventListener('click', event => {
  // textodata.addEventListener('keyup', function(){
  //})

  //  });

  var canvas = document.getElementById("canvas");
  var video1 = document.getElementById("video1");
  var ctx = canvas.getContext("2d");
  var modelo = null;
  var size = 400;




  var camaras = [];
  var facingMode = "user";

  var constraints = {
    video: videoConstraints,
    audio: false,
  };
  (async () => {
    console.log("Cargando modelo...");
    modelo = await tf.loadLayersModel("http://localhost:5000/static/model/model.json");
    console.log("Modelo cargado...");
  })();


  var recorder
  function predecir() {
    if (modelo != null) {
      resample_single(canvas, 150, 150, othercanvas);

      var ctx2 = othercanvas.getContext("2d");

      var imgData = ctx2.getImageData(0, 0, 150, 150);
      var arr = [];
      var arr150 = [];
      for (var p = 0, i = 0; p < imgData.data.length; p += 4) {
        var red = imgData.data[p] / 255;
        var green = imgData.data[p + 1] / 255;
        var blue = imgData.data[p + 2] / 255;
        arr150.push([red, green, blue]);
        if (arr150.length == 150) {
          arr.push(arr150);
          arr150 = [];
        }
      }
      /*
           var respuesta;
      if (resultado = 0) {
        respuesta = "Gato";
      }if(resultado = 1){
        respuesta = "Perro";
      }else respuesta = " "
      
      document.getElementById("resultado").innerHTML = respuesta;
    }
  
      */
      arr = [arr];
      var tensor4 = tf.tensor4d(arr);
      var resultados = modelo.predict(tensor4).dataSync();
      var mayorIndice = resultados.indexOf(Math.max.apply(null, resultados));
      var clases = ['Gato', 'Perro'];
      console.log("Prediccion", clases[mayorIndice]);
      
      document.getElementById("resultados").innerHTML = clases[mayorIndice];
  }
    setTimeout(predecir, 150);
  
}

  function procesarCamara() {

    var ctx = canvas.getContext("2d");

    ctx.drawImage(video, 0, 0, size, size, 0, 0, size, size);

    setTimeout(procesarCamara, 20);
  }

  function resample_single(canvas, width, height, resize_canvas) {
    var width_source = canvas.width;
    var height_source = canvas.height;
    width = Math.round(width);
    height = Math.round(height);

    var ratio_w = width_source / width;
    var ratio_h = height_source / height;
    var ratio_w_half = Math.ceil(ratio_w / 2);
    var ratio_h_half = Math.ceil(ratio_h / 2);

    var ctx = canvas.getContext("2d");
    var ctx2 = resize_canvas.getContext("2d");
    var img = ctx.getImageData(0, 0, width_source, height_source);
    var img2 = ctx2.createImageData(width, height);
    var data = img.data;
    var data2 = img2.data;

    for (var j = 0; j < height; j++) {
      for (var i = 0; i < width; i++) {
        var x2 = (i + j * width) * 4;
        var weight = 0;
        var weights = 0;
        var weights_alpha = 0;
        var gx_r = 0;
        var gx_g = 0;
        var gx_b = 0;
        var gx_a = 0;
        var center_y = (j + 0.5) * ratio_h;
        var yy_start = Math.floor(j * ratio_h);
        var yy_stop = Math.ceil((j + 1) * ratio_h);
        for (var yy = yy_start; yy < yy_stop; yy++) {
          var dy = Math.abs(center_y - (yy + 0.5)) / ratio_h_half;
          var center_x = (i + 0.5) * ratio_w;
          var w0 = dy * dy;
          var xx_start = Math.floor(i * ratio_w);
          var xx_stop = Math.ceil((i + 1) * ratio_w);
          for (var xx = xx_start; xx < xx_stop; xx++) {
            var dx = Math.abs(center_x - (xx + 0.5)) / ratio_w_half;
            var w = Math.sqrt(w0 + dx * dx);
            if (w >= 1) {

              continue;
            }

            weight = 2 * w * w * w - 3 * w * w + 1;
            var pos_x = 4 * (xx + yy * width_source);

            gx_a += weight * data[pos_x + 3];
            weights_alpha += weight;

            if (data[pos_x + 3] < 255)
              weight = weight * data[pos_x + 3] / 250;
            gx_r += weight * data[pos_x];
            gx_g += weight * data[pos_x + 1];
            gx_b += weight * data[pos_x + 2];
            weights += weight;
          }
        }
        data2[x2] = gx_r / weights;
        data2[x2 + 1] = gx_g / weights;
        data2[x2 + 2] = gx_b / weights;
        data2[x2 + 3] = gx_a / weights_alpha;
      }
    }


    ctx2.putImageData(img2, 0, 0);
  }


  navigator.mediaDevices
    .getUserMedia(constraints)
    .then(stream => {
      currentStream = stream;
      video.srcObject = stream;
      procesarCamara();
      predecir();
      return navigator.mediaDevices.enumerateDevices();
    })
    .then(gotDevices)
    .catch(error => {
      console.error(error);
    });

}//fin
//export{recordedVideo,recordedBlobs}
var mediaRecorder = null;
var recordedBlobs = [];

function handleDataAvailable(event) {
  console.log('handleDataAvailable', event);
  if (event.data && event.data.size > 0) {
    recordedBlobs.push(event.data);
  }
}

downloadButton.addEventListener('click', () => {
    const blob = new Blob(recordedBlobs, { type: 'video/mp4' });
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.style.display = 'none';
    a.href = url;
    a.download = 'test.mp4';
    document.body.appendChild(a);
    a.click();
    setTimeout(() => {
      document.body.removeChild(a);
      window.URL.revokeObjectURL(url);
    }, 100);
  });
  

function stopRecordingCallback() {

  var blob = mediaRecorder.getBlob();
  video.src = URL.createObjectURL(blob);

  mediaRecorder.currentStream.stop();

  var formdata = new FormData();
  formdata.append('blobFile', new Blob(blob));

  fetch('uploader.php', {
    method :"POST",
    body: formdata
}).then(()=>{
    alert('streamed video file uploaded')

  })
}

function startRecording() {
  let options = { mimeType: 'video/webm;codecs=vp9,opus' };
  try {
    mediaRecorder = new MediaRecorder(currentStream, options);
  } catch (e) {
    console.error('Exception while creating MediaRecorder:', e);
    errorMsgElement.innerHTML = `Exception while creating MediaRecorder: ${JSON.stringify(e)}`;
    return;
  }

  console.log('Created MediaRecorder', mediaRecorder, 'with options', options);

  var recordingDuration = 2000;
  mediaRecorder.setRecordingDuration(recordingDuration).onRecordingStopped(stopRecordingCallback);

  
  mediaRecorder.onstop = (event) => {
    console.log('Recorder stopped: ', event);
    console.log('Recorded Blobs: ', recordedBlobs);
  };
  mediaRecorder.ondataavailable = handleDataAvailable;
  mediaRecorder.start();
  console.log('MediaRecorder started', mediaRecorder);
}
function handleSuccess(stream) {
  recordButton.disabled = false;
  console.log('getUserMedia() got stream:', currentStream);
  currentStream = stream;

  const gumVideo = document.querySelector('video#gum');
  gumVideo.srcObject = currentStream;
}

navigator.mediaDevices.enumerateDevices().then(gotDevices);