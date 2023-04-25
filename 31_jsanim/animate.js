var c = document.getElementById("slate");
var dotButton = document.getElementById("buttonCircle") ;
var stopButton = document.getElementById("buttonStop"); 

var ctx = c.getContext("2d");
ctx.fillStyle = "blue";

var requestID;
var radius_change = 0.01;


var clear = (e) => {
    ctx.clearRect(0, 0, c.width, c.height);
}

var radius = 0;

var drawCircle = (e) => {
    ctx.beginPath();
    ctx.arc(c.width/2,c.height/2,radius, 0, 2*Math.PI);
    ctx.stroke();
    ctx.fill();
}

var drawDot = () => {
    while (True){
        radius+=radius_change;
        if (radius == c.height/2 || radius == 0){
            radius_change*=-1;
        }
        clear();
        radius+=radius_change;
        drawCircle();
        requestID = window.requestAnimationFrame(drawDot());
        cancelAnimationFrame(requestID);
    }
    

}
//requestID = window.requestAnimationFrame(drawDot());
//cancelAnimationFrame(requestID);


var stopIt = () => {
    console.log("stopIt invoked...");
    console.log(requestID);

}

dotButton.addEventListener("click", drawDot);
stopButton.addEventListener("click", stopIt);