function screen_resize() {
    var h = parseInt(window.innerHeight);
    var w = parseInt(window.innerWidth);
    if(w <= 500) {
      screen.orientation.lock("landscape-primary")
        }
}
function getFullscreenElement() {
  return document.fullscreenElement || document.webkitFullscreenElement || document.mozFullscreenElement || document.msFullscreenElement;
}

function toggleFullscreen() {
  document.getElementById("myBox1").requestFullscreen()
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
  document.getElementById("myBox2").requestFullscreen()
    screen_resize();
    var x = document.getElementById("normal_mode2");
    var y=  document.getElementById("fullscreen_mode2");
    x.style.display= "none";
    y.style.display = "block";
}
function exitfull2(){
  document.exitFullscreen();
    var x = document.getElementById("normal_mode2");
    var y=  document.getElementById("fullscreen_mode2");
    y.style.display= "none";
    x.style.display = "block";
}

function toggleFullscreen3() {
  document.getElementById("myBox3").requestFullscreen()
    screen_resize();
    var x = document.getElementById("normal_mode3");
    var y=  document.getElementById("fullscreen_mode3");
    x.style.display= "none";
    y.style.display = "block";
}
function exitfull3(){
  document.exitFullscreen();
    var x = document.getElementById("normal_mode3");
    var y=  document.getElementById("fullscreen_mode3");
    y.style.display= "none";
    x.style.display = "block";
}
function toggleFullscreen4() {
  document.getElementById("customer_card").requestFullscreen()
    screen_resize();
    var x = document.getElementById("normal_mode4");
    var y=  document.getElementById("fullscreen_mode4");
    var z= document.getElementById("customerbtn1");
    var w= document.getElementById("vendorbtn1");
    w.style.display= "none";
    z.style.display= "none";
    x.style.display= "none";
    y.style.display = "block";
}
function exitfull4(){
    document.exitFullscreen();
    var x = document.getElementById("normal_mode4");
    var y=  document.getElementById("fullscreen_mode4");
    var z= document.getElementById("customerbtn1");
    var w= document.getElementById("vendorbtn1");
    w.style.display= "block";
    z.style.display= "block";
    y.style.display= "none";
    x.style.display = "block";
}
function toggleFullscreen5() {
  document.getElementById("vendor_card").requestFullscreen()
    screen_resize();
    var x = document.getElementById("normal_mode5");
    var y=  document.getElementById("fullscreen_mode5");

    var z= document.getElementById("customerbtn2");
    var w= document.getElementById("vendorbtn2");
    w.style.display= "none";
    z.style.display= "none";
    x.style.display= "none";
    y.style.display = "block";
}
function exitfull5(){
  document.exitFullscreen();
    var x = document.getElementById("normal_mode5");
    var y=  document.getElementById("fullscreen_mode5");
    var z= document.getElementById("customerbtn2");
    var w= document.getElementById("vendorbtn2");
    w.style.display= "block";
    z.style.display= "block";
    y.style.display= "none";
    x.style.display = "block";
}
function toggleFullscreen6() {
  document.getElementById("myBox6").requestFullscreen()
    screen_resize();
    var x = document.getElementById("normal_mode6");
    var y=  document.getElementById("fullscreen_mode6");
    x.style.display= "none";
    y.style.display = "block";
}
function exitfull6(){
  document.exitFullscreen();
    var x = document.getElementById("normal_mode6");
    var y=  document.getElementById("fullscreen_mode6");
    y.style.display= "none";
    x.style.display = "block";
}
function toggleFullscreen7() {
  document.getElementById("myBox7").requestFullscreen()
    screen_resize();
    var x = document.getElementById("normal_mode7");
    var y=  document.getElementById("fullscreen_mode7");
    x.style.display= "none";
    y.style.display = "block";
}
function exitfull7(){
  document.exitFullscreen();
    var x = document.getElementById("normal_mode7");
    var y=  document.getElementById("fullscreen_mode7");
    y.style.display= "none";
    x.style.display = "block";
}
function toggleFullscreen8() {
  document.getElementById("myBox8").requestFullscreen()
    screen_resize();
    var x = document.getElementById("normal_mode8");
    var y=  document.getElementById("fullscreen_mode8");
    x.style.display= "none";
    y.style.display = "block";
}
function exitfull8(){
  document.exitFullscreen();
    var x = document.getElementById("normal_mode8");
    var y=  document.getElementById("fullscreen_mode8");
    y.style.display= "none";
    x.style.display = "block";
}
function toggleFullscreen9() {
  document.getElementById("myBox9").requestFullscreen()
    screen_resize();
    var x = document.getElementById("normal_mode9");
    var y=  document.getElementById("fullscreen_mode9");
    x.style.display= "none";
    y.style.display = "block";
}
function exitfull9(){
  document.exitFullscreen();
    var x = document.getElementById("normal_mode9");
    var y=  document.getElementById("fullscreen_mode9");
    y.style.display= "none";
    x.style.display = "block";
}
