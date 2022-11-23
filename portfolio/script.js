function myTime()
{
let time = new Date();

let second = time.getSeconds();
if (second < 10) second = "0" + second;

let minute = time.getMinutes();
if (minute < 10) minute = "0" + minute;

let hour = time.getHours();
if (hour < 10) hour = "0" + hour;

document.getElementById("function").innerHTML = hour + ":" + minute + ":" + second;

setTimeout("myTime()", 1000);
}
