/**
/  CSMA 101 
/  Fall 2020
/  Echo Theohar
/  @uthor Natalia Campos
/  natalia.campos@woodbury.edu
*/

var rain = [];
var img1, img2, img3;
var amount = 100;
var flood = 100;
var rising = 970;

function preload(){
   img1 = loadImage("Data/cloud.png");
   img2 = loadImage("Data/closedUmb.png");
    img3 = loadImage("Data/openUmb.png");
}

function setup(){
    createCanvas(1000,1000);
    //creates rainfall
    for (var i = 0; i<amount; i++){
        rain[i] = new R(random(width), random(height), 5,10, random(1,3), random(3,6));
    }
}

function draw(){
    background(80,80,130);
    
    textSize(10);
    fill(255);
    text("Click UP and DOWN arrows.", 100, 500);
    
    //creates continous rainfall
    for(var i = 0; i<amount; i++){
        rain[i].drawR();
        rain[i].falling();
        rain[i].reset();
    }
    
    //uploads cloud
    image(img1, 0, 0, 1000);
    
    //creates flood
    fill(60,60,150);
    rect(0, rising, 1000,flood);
    
    keyPressed();
}

function R(rX, rY, rSz1, rSz2, speedX, speedY){
    
    //declaring local vars
    this.xVal = rX;
    this.yVal = rY;
    this.size1 = rSz1;
    this.size2 = rSz2;
    this.spdX = speedX;
    this.spdY = speedY;
    
    //methods of the rain
    //draws each rain drop
    this.drawR = function(){
        fill(60,60,170);
        ellipse(this.xVal, this.yVal, this.size1,this.size2);
    }
    
    //how fast it rains
    this.falling = function(){
        this.yVal += this.spdY;
    }
    
    //resets rainfall and adds to flood
    this.reset = function(){
        if(this.yVal>height){
            this.yVal = 0;
            flood++;
            //stops flooding when its over the humans head about half of the height of the screen
            if(rising!=height/2){
                rising--;
            }
        }
        
    }
    
}

function keyPressed(){
    if(keyCode == UP_ARROW){
        //uploads open umbrella
        image(img3, 200, 200, 0);
    }
    else{
        //uploads closed umbrella
        image(img2, 200, 200, 0);
    }
}