// Team Eccentric Busters :: Nicholas Tarsis, Hui Wang 
// SoftDev pd7
// K28 -- Getting more comfortable with the dev console and the DOM
// 2023-04-17m
// --------------------------------------------------


//send diagnostic output to console
//(Ctrl-Shift-K in Firefox to reveal console)
console.log("AYO");

var i = "hello";
var j = 20;


//assign an anonymous fxn to a var
var f = function(x) {
  var j=30;
  return j+x;
};


//instantiate an object
var o = { 'name' : 'Thluffy',
          age : 1024,
          items : [10, 20, 30, 40],
          morestuff : {a : 1, b : 'ayo'},
          func : function(x) {
            return x+30;
          }
        };

//appends a new <li> element to the list
var addItem = function(text) {
  var list = document.getElementById("thelist");
  // assigns a variable to the list element on the page
  var newitem = document.createElement("li");
  // creates a new list item element
  newitem.innerHTML = text;
  // changes the text between the tags of the element <li>text</li>
  list.appendChild(newitem);
  // adds the element to the list element
};
// addItem("bruh");

// removes the item with the index n in the array of list items
var removeItem = function(n) {
  var listitems = document.getElementsByTagName('li');
  listitems[n].remove();
};
// removeItem(0);

// adds the red class to all the list item elements
var red = function() {
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    items[i].classList.add('red');
    // adds the class red to the start of the class list and not the end
    // ex:
    // <li class="green blue">item 1</li>
    // changes to
    // <li class="red green blue">item 1</li>
  }
};
//red();

// adds the red class to all the even indexed list item elements
// adds the blue class to all the odd indexed list item elements
var stripe = function() {
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    if (i%2==0){
      items[i].classList.add('red');
    } else {
      items[i].classList.add('blue');
    }
  }
};
stripe();

//insert your implementations here for...
// FAC
function fac (n) {
    if (n < 2){
        return 1;
    }
    return n*(fac(n-1));
}

// FIB
function fib (n){
    if (n < 2){
        return n;
    }
    return fib(n-1)+fib(n-2);
}

// GCD
function gcd (a, b){
    if (a==0){
        return b;
    }
    return gcd(b%a,a);
}

// In addition to the style shown above,
//  you are encouraged to test drive the "arrow function syntax" as shown below.
//  Note anything notable.
const myFxn = (param1, param2) => {
  // body
  return retVal;
};

const facA = (n) => {
    if (n < 2){
        return 1;
    }
    return n*(facA(n-1));
}
function fact_test (){
console.log(fac(1)); // should be 1
console.log(fac(2)); // should be 2
console.log(fac(3)); // should be 6
console.log(fac(4)); // should be 24
console.log(fac(5)); // should be 120
}

function fib_test (){

console.log(fib(0)); // should be 0
console.log(fib(1)); // should be 1
console.log(fib(2)); // should be 1
console.log(fib(3)); // should be 2
console.log(fib(4)); // should be 3
}

function gcd_test (){
console.log(gcd(0, 0)); // should be 0
console.log(gcd(1, 10)); // should be 1
console.log(gcd(2, 6)); // should be 2
console.log(gcd(8, 12)); // should be 4
console.log(gcd(15, 9)); // should be 3
}

var fact_btn = document.getElementById("a");
fact_btn.addEventListener("click", fact_test);
var fib_btn = document.getElementById("b");
fib_btn.addEventListener("click", fib_test);
var gcd_btn = document.getElementById("c");
gcd_btn.addEventListener("click", gcd_test);
