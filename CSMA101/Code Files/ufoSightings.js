/**
/  CSMA 101 
/  Fall 2020
/  Echo Theohar
/  @uthor Natalia Campos
/  natalia.campos@woodbury.edu
/
/   Title: Number of UFO Sightings in the US in the First 6 Months of /   2020
/
/   Project Description: This project is based on data points 
/   collected by the National UFO Reporting Center that reported an 
/   increase of suspected UFO sightings which many articles have   
/   written to believe that the reason is because of the Pandemic 
/   lockdown forcing many to stay home and speculate things that they /   would not normally speculate at home. This data then shows the 
/   increase in the very high increase in sightings during the 
/   lockdown of the 2nd month of the lockdown when almost everyone 
/   was staying at home compared to before the pandemic lockdowns in /   Januaury and the reopening of many places in the month of July.
*/

//create variables
var months = [];
var beamArray = [];
var points = [];
var yPoints = [];
var sz = [];
var ufoData, ufo, human, humLev, beam;

//on and off
var still = true;
var move = true;

//var x = mouseX;
//var y = mouseY;
var ufoX;
var ufoY;
var tag = 0;
var count = 800;
var rise = 0;
var r = 102;
var g = 255;
function preload(){
    
    //load csv info
    ufoData = loadTable("Assets/UFOSitings.csv");
    
    //load images
    ufo = loadImage("Data/ufo.png");
    human = loadImage("Data/human.png");
    humLev = loadImage("Data/abduction.png");
    beam = loadImage("Data/levBeam.png");
    
}

function setup(){
    createCanvas(1700, 1000);
    
    //call each column of csv
    for(var i =0; i<ufoData.getRowCount(); i++){
        
        //array of names
       months[i] = ufoData.getString(i,0);
        
        ////array of y's to determine how big they are
        points[i] = ufoData.getNum(i, 1);
        
        //array of y axis points
        yPoints[i] = ufoData.getNum(i, 2);
        
    }
}

function draw(){
    background(0);
    
    //create borders
    stroke(255);
    line(230, 100, 230, 800);
    stroke(255);
    line(230, 800, 1500, 800);
    
    //create titles on y and x axis
    graphLabels();
    //draw text and visuals
    for(var i = 0; i < ufoData.getRowCount(); i++){
        
        push();
        translate(140,-8);
        image(human,180*(i+0.65), 575,400,300);
        pop();
        
        push();
        fill(255);
        textSize(30);
        translate(180,-8);
        text(months[i], 190 * (i+.55), 850);
        pop();

        
        fill(255);
        textSize(30);
        text(yPoints[i], 150, 110 * (i+1));
        
    
    //create moving UFO and animations
    theUFO();
    freezeM();
    upArrow();
    leaveBar();
    permBeams();
        
    }
}

function graphLabels(){
    
    push();
    fill(255);
    textSize(35);
    translate(-420, 800);
    rotate(radians(-90));
    text("Number of Sightings", 200, height/2);
    pop();
    
    fill(255);
    textSize(40);
    text("Months of 2020", 750, 930);
    
    fill(255);
    textSize(50);
    text("Number of UFO Sightings in the US in 2020", 410, 130);
}

//creates movement of UFO
function theUFO(){
    //draw ufo and its movements
    if(move){
    image(ufo,mouseX,mouseY,200,100);
    }
}

function showBar(){
    image(beam,ufoX+40,ufoY+30,70,points[tag]);
}

//snaps the moving UFO to get ready to collect human
function freezeM(){
    if(mouseY>350 && mouseX>310 && mouseX<350 && still){
        move = false;
        ufoX = 275;
        ufoY = 460;
        tag = 0;
    }
    if(mouseY>350 && mouseX>510 && mouseX<530 && still){
        move = false;
        ufoX = 465;
        ufoY = 460;
        tag = 1;
    }
    if(mouseY>150 && mouseX>690 && mouseX<710 && still){
        move = false;
        ufoX = 645;
        ufoY = 310;
        tag = 2;
    }
      if(mouseY>50 && mouseX>870 && mouseX<890 && still){
        move = false;
        ufoX = 815;
        ufoY = 140;
        tag = 3;
    }
    if(mouseY>400 && mouseX>1050 && mouseX<1070 && still){
        move = false;
        ufoX = 995;
        ufoY = 530;
        tag = 4;
    }
    if(mouseY>650 && mouseX>1230 && mouseX<1250 && still){
        move = false;
        ufoX = 1178;
        ufoY = 610;
        tag = 5;
    }
    if(mouseY>380 && mouseX>1410 && mouseX<1430 && still){
        move = false;
        ufoX = 1375;
        ufoY = 450;
        tag = 6;
    }

    still = true;
    
}

//levitates human rising 
function levitate(){
    if(count>ufoY){
    image(humLev,ufoX+40,count,80,60);
        count--;
    }
}

//creates the beam that represents the bar after human has risen
function leaveBar(){
    if(count<=ufoY){
        fill(r,g,0);
        append(beamArray,rect(ufoX+60,ufoY+24,40, points[tag]-30));
        beamArray[tag];
        move = true;
        }
}

//uses function Up arrow to activate levitation
function upArrow(){
    if(move==false){
        showBar();
        image(ufo,ufoX,ufoY,200,100);
        if(keyCode===UP_ARROW){
            levitate();
        }
    }
}

//Displays beams permenently
function permBeams(){
    if(keyIsDown(DOWN_ARROW)){
        for(var i = 0; i<beamArray.length; i++){
            fill(r,g,0);
            beamArray[i];
        }
    }
}


