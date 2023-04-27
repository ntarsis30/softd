var c = document.getElementById("playground");
var dotButton = document.getElementById("circle");
var dvdButton = document.getElementById("dvd");
var stopButton = document.getElementById("stop");

var ctx = c.getContext("2d");
ctx.fillStyle = "blue";

var requestID;

var clear = (e) => {
    //e.preventDefault();
    ctx.clearRect(0, 0, 500, 500);
}
var radius = 0;
var growing = true;

var drawDot = () =>{
    window.cancelAnimationFrame(requestID);
    requestID = window.requestAnimationFrame(drawDot);
    clear();
    if (radius == 250) {
        growing = false;
    }
    else if (radius == 0 && !growing) {
        growing = true;
    }
    if (growing) {
        radius++;
    }
    else {
        radius--;
    }
    ctx.beginPath();
    ctx.arc(250, 250, radius, 0, Math.PI * 2, true);
    ctx.fill();
    ctx.stroke();
}

var stopIt = function() {
    console.log("stopIt invoked...");
    console.log(requestID);
    window.cancelAnimationFrame(requestID);
}

var dvdLogoSetup = function(){
    clear();

    window.cancelAnimationFrame(requestID);
    var rectWidth = 60; 
    var rectHeight = 40;

    var rectX = Math.floor(Math.random() * (500 - rectWidth));
    var rectY = Math.floor(Math.random() * (500 - rectHeight));

    var xVel = 1;
    var yVel = 1;
    
    var logo = new Image();
    logo.src = "logo_dvd.jpg"; 

    var dvdLogo = function(){
        ctx.clearRect(0, 0, c.width, c.height);
        // ctx.fillRect(rectX, rectY, rectWidth, rectHeight);
        ctx.drawImage(logo, rectX, rectY, rectWidth, rectHeight);
        if(rectX == 0 || rectX + rectWidth == 500) xVel *= -1; 
        if(rectY == 0 || rectY + rectHeight == 500) yVel *= -1;

        rectX += xVel;
        rectY += yVel;
        requestID = window.requestAnimationFrame(dvdLogo);
    }
    dvdLogo(); 

}

dotButton.addEventListener("click", drawDot);
stopButton.addEventListener("click", stopIt);
dvdButton.addEventListener("click", dvdLogoSetup); 