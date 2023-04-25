var c = document.getElementById("slate");

var ctx = c.getContext("2d");

var mode = "circle";

var toggleMode = (e)  => {
    console.log("toggling...");
    if (mode == "rect"){
        mode = "circle";
        bToggler.innerHTML="Circle";
    }

    else {
        mode = "rect";
        bToggler.innerHTML="Rectangle";

    }
}

var drawRect = function(e) {
    var mouseX = e.offsetX;
    var mouseY = e.offsetY;    
    console.log("mouseclick registered at ", mouseX, mouseY);
    ctx.beginPath();
    ctx.fillStyle = "red";
    ctx.fillRect(mouseX,mouseY,30,100);
    ctx.fill();
}

var drawCircle = (e) => {
    var mouseX = e.offsetX;
    var mouseY = e.offsetY;
    console.log("mouseclick registered at ", mouseX, mouseY);
    ctx.beginPath();
    ctx.fillStyle = "red";
    ctx.arc(mouseX,mouseY,15, 0, 2*Math.PI);
    ctx.stroke();
    ctx.fill();
}

var draw = (e) => {
    console.log("drawing...");
    if (mode == "rect"){
        drawRect(e);
    }

    else {        
        drawCircle(e);

    }
}

var wipeCanvas = () => {
    ctx.clearRect(0, 0, c.width, c.height);
}

c.addEventListener("click",draw);

var bToggler = document.getElementById("buttonToggle") ;
bToggler.addEventListener("click",toggleMode);

var clearB = document.getElementById("buttonClear");
clearB.addEventListener("click",wipeCanvas);
