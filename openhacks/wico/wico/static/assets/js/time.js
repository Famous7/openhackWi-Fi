var datediv = document.getElementById('datediv');
var date = new Date();
datediv.innerHTML = date.getFullYear() + ". " + date.getMonth() + ". " +
date.getDate();

var interval = setInterval(timestamphome, 1000);

function timestamphome(){
  var date = new Date();
  var time = document.getElementById('timediv');
  time.innerHTML = date.getHours() + ":" + date.getMinutes() + ":"
  +date.getSeconds();
}
