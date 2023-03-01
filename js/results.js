// change the color of the teams
document.querySelectorAll(".coloredcircle").forEach((item) => {
  // find out if homerow or awayrow for problematic color choices: x will store either homerow or awayrow
  var x = item.parentElement.parentElement.id;
  var y = item.parentElement.nextSibling.nextSibling;

  if (y.textContent.includes("Arizona")) {
    //on dark
    if (x.includes("home")) {
      item.style.color = "#30CED8";
    }
    //on light
    if (x.includes("away")) {
      item.style.color = "#A71930";
    }
  }

  if (y.textContent.includes("Atlanta")) {
    // on dark
    if (x.includes("home")) {
      item.style.color = "#CE1141";
    }
    //on light
    if (x.includes("away")) {
      item.style.color = "#13274F";
    }
  }

  if (y.textContent.includes("Baltimore")) {
    //on dark
    if (x.includes("home")) {
      item.style.color = "#DF4601";
    }
    // on light
    if (x.includes("away")) {
      item.style.color = "#DF4601";
    }
  }

  if (y.textContent.includes("Boston")) {
    //on dark
    if (x.includes("home")) {
      item.style.color = "#BD3039";
    }
    // on light
    if (x.includes("away")) {
      item.style.color = "#0C2340";
    }
  }

  if (y.textContent.includes("Chicago NL")) {
    // on dark
    if (x.includes("home")) {
      item.style.color = "#CC3433";
    }
    //on light
    if (x.includes("away")) {
      item.style.color = "#0E3386";
    }
  }

  if (y.textContent.includes("Chicago AL")) {
    // on dark
    if (x.includes("home")) {
      item.style.color = "#C4CED4";
    }
    //on light
    if (x.includes("away")) {
      item.style.color = "#000000";
    }
  }

  if (y.textContent.includes("Cincinnati")) {
    // on dark
    if (x.includes("home")) {
      item.style.color = "#C6011F";
    }
    //on light
    if (x.includes("away")) {
      item.style.color = "#C6011F";
    }
  }

  if (y.textContent.includes("Cleveland")) {
    // on dark
    if (x.includes("home")) {
      item.style.color = "#E50022";
    }
    //on light
    if (x.includes("away")) {
      item.style.color = "#E50022";
    }
    // item.style.color = "#00385D";
  }

  if (y.textContent.includes("Colorado")) {
    //on light
    if (x.includes("away")) {
      item.style.color = "#333366";
    }
    //on dark
    if (x.includes("home")) {
      item.style.color = "#C4CED4";
    }
  }

  if (y.textContent.includes("Detroit")) {
    // on light
    if (x.includes("away")) {
      item.style.color = "#0C2340";
    }
    //on dark
    if (x.includes("home")) {
      item.style.color = "#FA4616";
    }
  }

  if (y.textContent.includes("Houston")) {
    //on dark
    if (x.includes("home")) {
      item.style.color = "#EB6E1F";
    }
    //on light
    if (x.includes("away")) {
      item.style.color = "#EB6E1F";
    }
    // item.style.color = "#002D62";
  }

  if (y.textContent.includes("Kansas City")) {
    //on dark
    if (x.includes("home")) {
      item.style.color = "#BD9B60";
    }
    //on light
    if (x.includes("away")) {
      item.style.color = "#004687";
    }
  }

  if (y.textContent.includes("Los Angeles AL")) {
    //on dark
    if (x.includes("home")) {
      item.style.color = "#BA0021";
    }
    //on light
    if (x.includes("away")) {
      item.style.color = "#BA0021";
      // item.style.color = "#862633";
    }
  }

  if (y.textContent.includes("Los Angeles NL")) {
    //on dark
    if (x.includes("home")) {
      item.style.color = "#005A9C";
    }
    //on light
    if (x.includes("away")) {
      // item.style.color = "#EF3E42";
      item.style.color = "#005A9C";
    }
  }

  if (y.textContent.includes("Miami")) {
    //on dark
    if (x.includes("home")) {
      item.style.color = "#EF3340";
    }
    //on light
    if (x.includes("away")) {
      item.style.color = "#00A3E0";
    }
  }

  if (y.textContent.includes("Milwaukee")) {
    //on dark
    if (x.includes("home")) {
      item.style.color = "#FFC52F";
    }
    //on light
    if (x.includes("away")) {
      item.style.color = "#12284B";
    }
  }

  if (y.textContent.includes("Minnesota")) {
    //on dark
    if (x.includes("home")) {
      item.style.color = "#D31145";
    }
    //on light
    if (x.includes("away")) {
      item.style.color = "#002B5C";
    }
  }
  if (y.textContent.includes("New York NL")) {
    //on dark
    if (x.includes("home")) {
      item.style.color = "#FF5910";
    }
    //on light
    if (x.includes("away")) {
      item.style.color = "#002D72";
    }
  }

  if (y.textContent.includes("New York AL")) {
    //on light
    if (x.includes("away")) {
      item.style.color = "#0C2340";
    }
    //on dark
    if (x.includes("home")) {
      item.style.color = "#0C2340";
      // item.style.color = "#E4002C";
    }
  }

  if (y.textContent.includes("Oakland")) {
    //on light
    if (x.includes("away")) {
      item.style.color = "#003831";
    }
    //on dark
    if (x.includes("home")) {
      item.style.color = "#EFB21E";
    }
  }

  if (y.textContent.includes("Philadelphia")) {
    //on light
    if (x.includes("away")) {
      item.style.color = "#E81828";
    }
    //on dark
    if (x.includes("home")) {
      item.style.color = "#E81828";
    }
    // item.style.color = "#002D72";
  }

  if (y.textContent.includes("Pittsburgh")) {
    //on light
    if (x.includes("away")) {
      item.style.color = "#FDB827";
    }
    //on dark
    if (x.includes("home")) {
      item.style.color = "#FDB827";
    }
  }

  if (y.textContent.includes("San Diego")) {
    //on light
    if (x.includes("away")) {
      item.style.color = "#2F241D";
    }
    //on dark
    if (x.includes("home")) {
      item.style.color = "#FFC425";
    }
  }

  if (y.textContent.includes("San Francisco")) {
    //on light
    if (x.includes("away")) {
      item.style.color = "#FD5A1E";
    }
    //on dark
    if (x.includes("home")) {
      item.style.color = "#FD5A1E";
    }
  }

  if (y.textContent.includes("Seattle")) {
    // on dark
    if (x.includes("home")) {
      item.style.color = "#005C5C";
    }
    // on light
    if (x.includes("away")) {
      item.style.color = "#0C2C56";
    }
  }

  if (y.textContent.includes("St. Louis")) {
    //on dark
    if (x.includes("home")) {
      item.style.color = "#C41E3A";
    }
    //on light
    if (x.includes("away")) {
      item.style.color = "#0C2340";
    }
  }

  if (y.textContent.includes("Tampa Bay")) {
    //on dark
    if (x.includes("home")) {
      item.style.color = "#8FBCE6";
    }
    //on light
    if (x.includes("away")) {
      item.style.color = "#092C5C";
    }
  }

  if (y.textContent.includes("Texas")) {
    //on light
    if (x.includes("away")) {
      item.style.color = "#003278";
    }
    //on dark
    if (x.includes("home")) {
      item.style.color = "#C0111F";
    }
  }

  if (y.textContent.includes("Toronto")) {
    //on light
    if (x.includes("away")) {
      item.style.color = "#134A8E";
    }
    //on dark
    if (x.includes("home")) {
      item.style.color = "#E8291C";
    }
  }

  if (y.textContent.includes("Washington")) {
    //on dark
    if (x.includes("home")) {
      item.style.color = "#AB0003";
    }
    //on light
    if (x.includes("away")) {
      item.style.color = "#14225A";
    }
  }
});
