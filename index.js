document.getElementById("pottemp").innerText = "Set Temperature: " + 76;
setInterval(function(){ updateValues(); }, 2000);

function refreshValues(){
    var request = new XMLHttpRequest();
    request.open('GET','http://pi.cmasterx.com:8000/api');
    request.onload=function(){
        if(request.status==200){
    //put http request here and store data in following var
             var sensorData = JSON.parse(this.response);
             var temp0=sensorData["temperature-0"];
             var temp1=sensorData["temperature-1"];
             var avTemp=(temp0+temp1)/2;
             var pottemp=sensorData["potentiometer-0"];
             var ph=sensorData.ph;
             var clarity=sensorData.turbidity;
             var alarm=sensorData.alarm;

            document.getElementById("temp").innerText = "Temperature Conditions: "+avTemp;
            document.getElementById("pottemp").innerText = "Set Temperature: "+pottemp;
            document.getElementById("ph").innerText = "PH: "+ph;
            document.getElementById("clarity").innerText = "Clarity: "+clarity;
            document.getElementById("alarm").innerText= "Alarm: "+alarm;
        }
        else{
            console.log("error with http req");
        }
    }
    request.send();


}

var i = 0;

function updateValues() {
    var clarity = i % 10;
    clarity = clarity / 2 >> 0;

    document.getElementById("temp").innerText = "Temperature Conditions: "+ (77 + (i / 20 >> 0) % 2);
    // document.getElementById("pottemp").innerText = "Set Temperature: " + 76;
    document.getElementById("ph").innerText = "PH: "+ (5.02 + Math.random() * 0.3);
    document.getElementById("clarity").innerText = "Clarity: "+ (clarity + 1);
    document.getElementById("alarm").innerText= "Alarm: " + "False";

    i++;
}

function setPot(){
    // var request = new XMLHttpRequest();
    var tmp = document.getElementById("setTemp").value;
    document.getElementById("pottemp").innerText = "Set Temperature: " + tmp;
    // request.open('GET','http://pi.cmasterx.com:8000/api?set_temp='+ptemp);
    
    // request.send();


}