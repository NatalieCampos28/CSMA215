//Was added to index.html but failed <script src="p5/addons/p5.sound.js"></script>

/**
/  CSMA 101 
/  Fall 2020
/  Echo Theohar
/  @uthor Natalia Campos
/  natalia.campos@woodbury.edu
*/

//variables for ball
var ballX = 10;
var ballY = 10;
var diameter = 50; //for collision
var directionX = 6;
var directionY = 7;

//variables for sound and score
//let sound1;
//let sound2;
var sound1On = false;
var sound2On = false;
var scoreL = 0;
var scoreR = 0;
var wallHitL = false;
var wallHitR = false;

//paddle color changing variables
var fill1 = 255;
var fill2 = 255;
var fill3 = 255;
var fill4 = 255;
var fill5 = 255;
var fill6 = 255;

//variables for Paddles
//var rectX;
var rectY = 400;
var rectW = 25;
var rectH = 100;
    
//var rectX1;
var rectY1 = 400;
var rectW1 = 25;
var rectH1 = 100;

//function preload() {
 // soundFormats('mp3', 'ogg', 'wav');
  //sound1 = loadSound('SoundEffects/pongBlip1.wav');
  //sound2 = loadSound('SoundEffects/pongBlip2.wav');
//}

function setup(){
    createCanvas(800,800);
}

function draw(){
    background(100);
    
    fill(255);
    textSize(50);
    text('Score: '+scoreL+' | '+scoreR+' ', 250, 50);
    
    //ball bounces off walls
    ballX = ballX + directionX;
    ballY = ballY + directionY;
    
    if(ballX < 0){
        directionX =- directionX;
        wallHitL = true;
        wallHitR = false;
    }
    if(ballX > width){
        directionX =- directionX;
        wallHitR = true;
        wallHitL = false;
        //sound2.play();
    }
    
    if(ballY < 0 || ballY > height){
        directionY =- directionY;
        //sound2.play();
    }
    
    
    //draw ball and paddle
    fill(random(255), random(255), random(255));
    ellipse(ballX, ballY, diameter);
    
    //left paddle
    fill(fill1, fill2, fill3);
    rect(0, rectY, rectW, rectH);
    //right paddle
    fill(fill4, fill5, fill6);
    rect(775, rectY1, rectW1, rectH1);
    
    keyChange();
    keepScore();
    
    //detect collision with left paddle
    if(ballX+(diameter/2) > 20 && ballX+(diameter/2) < 20+(rectW/2) && ballY > rectY-50 && ballY < rectY+50){
        sound1On = true;
        directionX*=-1;
        directionY*=-1;
        fill1 = random(255);
        fill2 = random(255);
        fill3 = random(255);
    }
    
    //detect collision with right paddle
    if(ballX+(diameter/2) > 785 && ballX+(diameter/2) < 785 + (rectW1/2) && ballY > rectY1-50 && ballY < rectY1+50){
        sound2On = true;
        directionX*=-1;
        directionY*=-1;
        fill4 = random(255);
        fill5 = random(255);
        fill6 = random(255);
    }
    
    //Function to move right and left paddles
    function keyChange(){
        if(keyIsDown(LEFT_ARROW)){
            moveLeftKey();
        }else if(keyIsDown(RIGHT_ARROW)){
            moveRightKey();
        }
    }
    
    //function for left paddle
    function moveLeftKey(){
        if(keyIsDown(UP_ARROW)){
                rectY-=10;
        }else if(keyIsDown(DOWN_ARROW)){
                rectY+=10;
        }
    }
    
    //function to move right paddle
    function moveRightKey(){
        if(keyIsDown(UP_ARROW)){
                rectY1-=10;
        }else if(keyIsDown(DOWN_ARROW)){
                rectY1+=10;
        }
    }
    
    //function to keep score and play sound effects
    function keepScore() {
        //if (sound1On == true) {
        //sound1.play();
            if(sound1On == true && wallHitR == true){
               scoreL=+1;
            }
                sound1On = false;
        //sound1On = false;
        //}
        //if(sound2On == true){
        //sound1.play();
            if(sound2On == true && wallHitL == true){
                scoreR=+1;
            }
                sound2On = false;
        //sound2On = false;
        //}
    }
}