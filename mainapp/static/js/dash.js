function screen_resize() {
    var h = parseInt(window.innerHeight);
    var w = parseInt(window.innerWidth);
    document.getElementById("myBox1").requestFullscreen().catch((e) => {
        });
    if(w <= 500) {
      screen.orientation.lock("landscape-primary")
        }
}
function getFullscreenElement() {
  return document.fullscreenElement || document.webkitFullscreenElement || document.mozFullscreenElement || document.msFullscreenElement;
}

function toggleFullscreen() {
    screen_resize();
    var x = document.getElementById("normal_mode");
    var y=  document.getElementById("fullscreen_mode");
    x.style.display= "none";
    y.style.display = "block";
}
function exitfull(){
  document.exitFullscreen();
    var x = document.getElementById("normal_mode");
    var y=  document.getElementById("fullscreen_mode");
    y.style.display= "none";
    x.style.display = "block";
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