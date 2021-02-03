let ex1 = document.getElementById('#ex1')

function load_moon_phases(obj,callback){
    var gets=[]
    for (var i in obj){
        gets.push(i + "=" +encodeURIComponent(obj[i]))
    }
    gets.push("LDZ=" + new Date(obj.year,obj.month-1,1) / 1000)
    var xmlhttp = new XMLHttpRequest()
    var url = "https://www.icalendar37.net/lunar/api/?" + gets.join("&")
    xmlhttp.onreadystatechange = function() {
        if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
            callback(JSON.parse(xmlhttp.responseText))
        }
    }
    xmlhttp.open("GET", url, true)
    xmlhttp.send()
}

var configMoon = {
    lang  		: 'en', // (*) 
    month 		: new Date().getMonth() + 1, // 1  - 12
    year  		: new Date().getFullYear(), // year
    size		: 100, //  "100%" - pixels
    lightColor	: "#FFFF88", //CSS color
    shadeColor	: "black", // CSS color    
    texturize	: false, // true - false
}
  













function example_1(moon){    
    var day = new Date().getDate()
    var dayWeek=moon.phase[day].dayWeek
    var html = "<div>" +
    "<b>" + moon.nameDay[dayWeek]+ "</b>" +
    "<div>" + day + " <b>" + moon.monthName + "</b> " +
    moon.year + "</div>" +
    "<div shadow>" + moon.phase[day].svg + "</div>" +
    "<div>" + moon.phase[day].phaseName + " " +
    "" + ((moon.phase[day].isPhaseLimit )? ""  :   Math.round(moon.phase[day].lighting) + "%") +
    "</div>" +
    "</div>"
    document.getElementById("ex1").innerHTML = html
}   
var configMoon = {
    lang  		:'en', 
    month 		:new Date().getMonth() + 1,
    year  		:new Date().getFullYear(),
    size		:150, 
    lightColor	:"rgb(255,255,210)", 
    shadeColor	:"black", 
    texturize	:false, 
}
load_moon_phases(configMoon,example_1)