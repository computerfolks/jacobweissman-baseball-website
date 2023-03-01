//limit the name input to be three letters max
function teamcolor(event) {
  var string = this.textContent;
  var length = 3;
  var trimmedString = string.substring(0, length);
  this.textContent = trimmedString;
  document.querySelectorAll(".coloredcircle").forEach((item) => {
    var x = item.nextSibling;
    if (x.textContent.toUpperCase == "NYY") {
      if (x.id == "hometeam") {
        item.style.color = "#30CED8";
      }
    }
  });
}

document.querySelectorAll(".nameinput").forEach((item) => {
  item.oninput = teamcolor;
  item.onchange = teamcolor;
});
