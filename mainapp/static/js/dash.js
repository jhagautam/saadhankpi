
function getFullscreenElement() {
  return document.fullscreenElement || document.webkitFullscreenElement || document.mozFullscreenElement || document.msFullscreenElement;
}

function toggleFullscreen() {
  if (getFullscreenElement()) {
    document.exitFullscreen();
  } else {
    document.getElementById("myBox1").requestFullscreen().catch((e) => {
      console.log('hi');
      
    });
  }
}

function toggleFullscreen2() {
  if (getFullscreenElement()) {
    document.exitFullscreen();
  } else {
    document.getElementById("myBox2").requestFullscreen().catch((e) => {
      console.log('hi');
      
    });
  }
}
function toggleFullscreen3() {
  if (getFullscreenElement()) {
    document.exitFullscreen();
  } else {
    document.getElementById("myBox3").requestFullscreen().catch((e) => {
      console.log('hi');
      
    });
  }
}
function toggleFullscreen4() {
  if (getFullscreenElement()) {
    document.exitFullscreen();
  } else {
    document.getElementById("myBox4").requestFullscreen().catch((e) => {
      console.log('hi');
      
    });
  }
}
function toggleFullscreen5() {
  if (getFullscreenElement()) {
    document.exitFullscreen();
  } else {
    document.getElementById("myBox5").requestFullscreen().catch((e) => {
      console.log('hi');
      
    });
  }
}
function toggleFullscreen6() {
  if (getFullscreenElement()) {
    document.exitFullscreen();
  } else {
    document.getElementById("myBox6").requestFullscreen().catch((e) => {
      console.log('hi');
      
    });
  }
}
function toggleFullscreen7() {
  if (getFullscreenElement()) {
    document.exitFullscreen();
  } else {
    document.getElementById("myBox7").requestFullscreen().catch((e) => {
      console.log('hi');
      
    });
  }
}
function toggleFullscreen8() {
  if (getFullscreenElement()) {
    document.exitFullscreen();
  } else {
    document.getElementById("myBox8").requestFullscreen().catch((e) => {
      console.log('hi');
      
    });
  }
}
function toggleFullscreen9() {
  if (getFullscreenElement()) {
    document.exitFullscreen();
  } else {
    document.getElementById("myBox9").requestFullscreen().catch((e) => {
      console.log('hi');
      
    });
  }
}


