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

function setPot(){
    var request = new XMLHttpRequest();
    var ptemp = document.getElementById("setTemp").value;
    request.open('GET','http://pi.cmasterx.com:8000/api?set_temp='+ptemp);
    
    request.send();


}