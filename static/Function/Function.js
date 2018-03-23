//This is the Javascript code

//Date Calender Data began generating
var startDateM = 3;
var startDateD = 1;
var startDateY = 2018;

//Current Date info
var d = new Date();
var CurrDateM = d.getMonth() + 1;
var CurrDateD = d.getDate();
var CurrDateY = d.getFullYear();
var CurrWeekDay = d.getDay();

//Number of Days in each month
var z = 1;
var Row = document.getElementById("Week");
var InnerDiv = Row.getElementsByTagName("DIV");

for(var i = 0; i < InnerDiv.length; i++) {


  InnerDiv[i].innerHTML = z;
  z++;

}

var Row = document.getElementById("Week2");
var InnerDiv = Row.getElementsByTagName("DIV");

for(var i = 0; i < InnerDiv.length; i++) {


  InnerDiv[i].innerHTML = z;
  z++;


}

var Row = document.getElementById("Week3");
var InnerDiv = Row.getElementsByTagName("DIV");

for(var i = 0; i < InnerDiv.length; i++) {


  InnerDiv[i].innerHTML = z;
  z++;


}

var Row = document.getElementById("Week4");
var InnerDiv = Row.getElementsByTagName("DIV");

for(var i = 0; i < InnerDiv.length; i++) {


  InnerDiv[i].innerHTML = z;
  z++;


}

var Row = document.getElementById("Week5");
var InnerDiv = Row.getElementsByTagName("DIV");

for(var i = 0; i < InnerDiv.length; i++) {


  InnerDiv[i].innerHTML = z;
  z++;


}
