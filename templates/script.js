var urls = new Array();
var audioPlayer = document.querySelectorAll(".audio").forEach(musica =>{urls.push(musica)})
var current = 0;

var count = document.querySelectorAll('.count')
console.log(count)

function playSong() {
    document.querySelectorAll(".buttons").forEach((btn) => {
    let audio = btn.getAttribute("name") 
    if(audio === "play"){
        btn.setAttribute("name", "pause")
        urls[current].load();
        urls[current].play();
        urls[current].addEventListener('ended', function (event) {
            btn.setAttribute("name", "play")
            });
        }else {
            btn.setAttribute("name", "play")
            music.audio.pause()
            }
  });
}

function pickSong(num) {
current = num;
playSong();
}
  
function nextSong() {
current++;
if (current >= urls.length) {
    urls[current].stop();
}
playSong();
}
  
urls[current].addEventListener('ended', nextSong, false);
urls[current].addEventListener('error', nextSong, true);






  document.querySelectorAll(".buttons").forEach((btn) => {
    var current = 0;

     let music = {}
     var urls = new Array();

     btn.addEventListener("click", function (event){
         let audio = btn.getAttribute("name")

         music.audio = event.target.nextElementSibling



         if(audio === "play"){
         btn.setAttribute("name", "pause")
           music.audio.play()
           music.audio.addEventListener('ended', function (event) {
             btn.setAttribute("name", "play")
             });
            }else {
            btn.setAttribute("name", "play")
            music.audio.pause()
            }
     })



});