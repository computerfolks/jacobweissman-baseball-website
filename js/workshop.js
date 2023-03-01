//prevent enter key from causing form submission
$(document).ready(function () {
  $(window).keydown(function (event) {
    if (event.keyCode == 13) {
      event.preventDefault();
      return false;
    }
  });
});

//prevent dash
$(document).ready(function () {
  $(window).keydown(function (event) {
    if (event.keyCode == 189) {
      event.preventDefault();
      return false;
    }
  });
});

//prevent +
$(document).ready(function () {
  $(window).keydown(function (event) {
    if (event.keyCode == 187) {
      event.preventDefault();
      return false;
    }
  });
});

//prevent e
$(document).ready(function () {
  $(window).keydown(function (event) {
    if (event.keyCode == 69) {
      event.preventDefault();
      return false;
    }
  });
});

//three decimal places
function threedplaces(event) {
  if ((this.value * 100) % 1 != 0) {
    this.value = parseFloat(this.value).toFixed(2);
  }
}

var secondarycolor = "#99f6e4";
var lightcolor = "#ebedf9";
var primarycolor = "#881337";
var darkcolor = "#050814";
var inputcolor = "#b87187";

//tabs

//at page launch, select and display general, hide the others
document.getElementById("generallink").style.borderTop =
  "1px solid var(--main-light-color)";
document.getElementById("generallink").style.color = secondarycolor;

document.querySelectorAll(".cat-nav-link").forEach((item) => {
  item.onclick = navlinkClick;
});

function navlinkClick(event) {
  // console.log("test success");
  if (this.id != "submitlink") {
    this.style.color = secondarycolor;
  }
  this.style.borderTop = "1px solid var(--main-light-color)";
  document.querySelectorAll(".cat-nav-link").forEach((item) => {
    if (item != this) {
      item.style.backgroundColor = "";
      item.style.borderTop = "";
      if (item.id != "submitlink") {
        item.style.color = lightcolor;
      }
    }
  });

  document.querySelectorAll(".bigbox").forEach((item) => {
    //set all boxes to display none
    item.style.display = "none";
  });

  //examine which link was pressed, display that, all of the others will still be set to display none
  if (this.id == "generallink") {
    document.getElementById("generalbox").style.display = "block";
  }
  if (this.id == "battinglink") {
    document.getElementById("battingbox").style.display = "block";
  }
  if (this.id == "baserunninglink") {
    document.getElementById("baserunningbox").style.display = "block";
  }
  if (this.id == "pitchinglink") {
    document.getElementById("pitchingbox").style.display = "block";
  }
  if (this.id == "fieldinglink") {
    document.getElementById("fieldingbox").style.display = "block";
  }
  if (this.id == "submitlink") {
    document.getElementById("submitbox").style.display = "block";
  }
}

//at page launch, fill in the sum values, which theoretically should only be able to be 0 or 100
//batting
var sum = Number(0);
document.querySelectorAll(".battinginput").forEach((item) => {
  sum = sum + Number(item.value);
});
document.getElementById("battingsumcheck").innerHTML = sum;
if (sum == 100) {
  document.getElementById("battingsumcheck").style.color = "green";
}

//baserunning
var sum = Number(0);
document.querySelectorAll(".baserunninginput").forEach((item) => {
  sum = sum + Number(item.value);
});
document.getElementById("baserunningsumcheck").innerHTML = sum;
if (sum == 100) {
  document.getElementById("baserunningsumcheck").style.color = "green";
}

//pitching
var sum = Number(0);
document.querySelectorAll(".pitchinginput").forEach((item) => {
  sum = sum + Number(item.value);
});
document.getElementById("pitchingsumcheck").innerHTML = sum;
if (sum == 100) {
  document.getElementById("pitchingsumcheck").style.color = "green";
}

//fielding
var sum = Number(0);
document.querySelectorAll(".fieldinginput").forEach((item) => {
  sum = sum + Number(item.value);
});
document.getElementById("fieldingsumcheck").innerHTML = sum;
if (sum == 100) {
  document.getElementById("fieldingsumcheck").style.color = "green";
}

function checkbsrfld(event) {
  // console.log("checking bsrfld");
  document.querySelectorAll(".bsrfldradio").forEach((item) => {
    if (item != this) {
      item.checked = false;
    }
    // console.log("fixed the values");
  });
  this.checked = true;
  if (document.getElementById("bsrfldmanual").checked) {
    document.getElementById("bsrfldinput").style.display = "flex";
  }
  if (document.getElementById("bsrfldauto").checked) {
    document.getElementsByName("baserunning_weight")[0].value = 0;
    document.getElementsByName("fielding_weight")[0].value = 0;
    approveNewCategoryInput();
    document.getElementById("bsrfldinput").style.display = "none";
  }
}

function approveNewSeasonWeightsInput(event) {
  //this keeps everything to three decimal places automaticall
  //this.value = parseFloat(this.value).toFixed(2);
  //do not allow negative values
  if (this.value < 0) {
    // this.value = 0;
    document.querySelectorAll(".errorseasonweights").forEach((item) => {
      item.style.display = "block";
    });
    positiveseason = false;
  } else {
    positiveseason = true;
  }
  //this makes sure the total values do not exceed 100
  var sum = Number(0);
  document.querySelectorAll(".seasonweightsinput").forEach((item) => {
    sum = sum + Number(item.value);
  });
  if (sum > 100) {
    // this.value = 100 - (sum - this.value);
    document.querySelectorAll(".errorseasonweights").forEach((item) => {
      item.style.display = "block";
    });
    lessthanhundredseason = false;
  } else {
    lessthanhundredseason = true;
  }
  //this.value = parseFloat(this.value).toFixed(2);
  if (positiveseason && lessthanhundredseason) {
    document.querySelectorAll(".errorseasonweights").forEach((item) => {
      item.style.display = "none";
    });
  }
  // notready();
}

function checkseasonweights() {
  document.querySelectorAll(".seasonweightsradio").forEach((item) => {
    if (item != this) {
      item.checked = false;
    }
  });
  this.checked = true;
  if (document.getElementById("seasonweightsmanual").checked) {
    // console.log("manual is checked");
    document.getElementById("seasonweightsauto").checked = false;
    document.getElementById("threeyearmanualinput").style.display = "flex";
    //select all the classes corresponding to the 2020, 2021, 2022 weights and check the input is valid
  } else {
    // document.querySelectorAll(".seasonweightsinput").forEach((item) => {
    //   item.value = 0;
    // });
    document.getElementsByName("s2022_weight")[0].value = 60.0;
    document.getElementsByName("s2021_weight")[0].value = 28.0;
    document.getElementsByName("s2020_weight")[0].value = 12.0;
    approveNewSeasonWeightsInput();
    document.getElementById("threeyearmanualinput").style.display = "none";
  }
}

document.querySelectorAll(".bsrfldradio").forEach((item) => {
  item.oninput = checkbsrfld;
  item.onchange = threedplaces;
});

document.querySelectorAll(".seasonweightsradio").forEach((item) => {
  item.oninput = checkseasonweights;
  item.onchange = threedplaces;
});

function checkplus(event) {
  // console.log("checking");
  document.querySelectorAll(".plusradio").forEach((item) => {
    if (item != this) {
      item.checked = false;
    }
  });
  this.checked = true;
}

document.querySelectorAll(".plusradio").forEach((item) => {
  item.oninput = checkplus;
});

function checkhomefield(event) {
  // console.log("checking home field");
  document.querySelectorAll(".homefieldradio").forEach((item) => {
    if (item.id != this.id) {
      // console.log(item.id);
      // console.log(this.id);
      item.checked = false;
      // console.log("changed an item");
    }
  });
  this.checked = true;
  if (document.getElementById("homefieldmanual").checked) {
    document.getElementById("homefieldmanualinput").style.display = "flex";
  } else {
    document.getElementById("homefieldweightinput").value = 3.5;
    approveHomeFieldInput();
    document.getElementById("homefieldmanualinput").style.display = "none";
  }
}

document.getElementById("homefieldweightinput").onchange = threedplaces;

document.querySelectorAll(".homefieldradio").forEach((item) => {
  item.oninput = checkhomefield;
  // console.log(item.id);
});

function approveHomeFieldInput(event) {
  // console.log("hello");
  if (document.getElementById("homefieldweightinput").value > 50) {
    // document.getElementById("homefieldweightinput").value = 50.0;
    document.querySelectorAll(".errorhomefield").forEach((item) => {
      item.style.display = "block";
    });
  } else if (document.getElementById("homefieldweightinput").value < 0) {
    // document.getElementById("homefieldweightinput").value = 0.0;
    document.querySelectorAll(".errorhomefield").forEach((item) => {
      item.style.display = "block";
    });
  } else {
    document.querySelectorAll(".errorhomefield").forEach((item) => {
      item.style.display = "none";
    });
  }
  // document.getElementById("homefieldweightinput").value = parseFloat(
  //   document.getElementById("homefieldweightinput").value
  // ).toFixed(2);
}

document.getElementById("homefieldweightinput").oninput = approveHomeFieldInput;

//verification of input
function approveNewBattingInput(event) {
  //this keeps everything to three decimal places automatically
  if (this.value > 0) {
    this.parentElement.querySelector(".value-title").style.color = inputcolor;
  } else {
    this.parentElement.querySelector(".value-title").style.color = lightcolor;
  }
  //this.value = parseFloat(this.value).toFixed(2);
  //do not allow negative values
  positivebatting = true;
  document.querySelectorAll(".battinginput").forEach((item) => {
    if (item.value < 0) {
      positivebatting = false;
      negbatting = item.id;
      document.querySelectorAll(".errorbatting").forEach((item) => {
        item.style.display = "block";
      });
    }
  });
  battingSum();
}

function battingSum() {
  //this makes sure the total values do not exceed 100
  var sum = Number(0);
  document.querySelectorAll(".battinginput").forEach((item) => {
    sum = sum + Number(item.value);
  });
  if (sum > 100) {
    // this.value = 100 - (sum - this.value);
    document.querySelectorAll(".errorbatting").forEach((item) => {
      item.style.display = "block";
    });
    lessthanhundredbatting = false;
  } else {
    lessthanhundredbatting = true;
  }
  //update the current sum that is displayed to the user
  document.getElementById("battingsumcheck").innerHTML = sum;
  //if sum is 100, make the color green, otherwise make it black (or red if error)
  if (positivebatting == false) {
    document.getElementById("battingsumcheck").style.color = primarycolor;
    document.getElementById("battingsumcheck").innerHTML =
      "please remove negative number in the '" +
      document
        .getElementById(negbatting)
        .previousElementSibling.textContent.replace(" -", "") +
      "' input box";
  } else if (sum > 100) {
    document.getElementById("battingsumcheck").style.color = primarycolor;
  } else if (sum < 100) {
    document.getElementById("battingsumcheck").style.color = darkcolor;
  } else {
    document.getElementById("battingsumcheck").style.color = "green";
  }

  if (positivebatting && lessthanhundredbatting) {
    document.querySelectorAll(".errorbatting").forEach((item) => {
      item.style.display = "none";
    });
  }
}

//set the approvenewbattinginput function to apply to all battinginput variables
document.querySelectorAll(".battinginput").forEach((item) => {
  item.oninput = approveNewBattingInput;
  if (item.value > 0) {
    item.parentElement.querySelector(".value-title").style.color = inputcolor;
  }
  item.onchange = battingOnChange;
  //fix the batting sum as well
});

function battingOnChange(event) {
  if ((this.value * 100) % 1 != 0) {
    this.value = parseFloat(this.value).toFixed(2);
  }
  battingSum();
  var fixedbattingsum = document.getElementById("battingsumcheck").innerHTML;
  // console.log(fixedbattingsum);
  if (!fixedbattingsum.includes("please")) {
    if (fixedbattingsum == 100) {
      document.getElementById("battingsumcheck").innerHTML = "100";
    } else {
      document.getElementById("battingsumcheck").innerHTML =
        parseFloat(fixedbattingsum).toFixed(2);
    }
  }
}

//verification of input
function approveNewBaserunningInput(event) {
  //this keeps everything to three decimal places automatically
  //this.value = parseFloat(this.value).toFixed(2);
  if (this.value > 0) {
    this.parentElement.querySelector(".value-title").style.color = inputcolor;
  } else {
    this.parentElement.querySelector(".value-title").style.color = lightcolor;
  }
  //do not allow negative values
  positivebaserunning = true;
  document.querySelectorAll(".baserunninginput").forEach((item) => {
    if (item.value < 0) {
      positivebaserunning = false;
      negbaserunning = item.id;
      document.querySelectorAll(".errorbaserunning").forEach((item) => {
        item.style.display = "block";
      });
    }
  });
  baserunningSum();
}

function baserunningSum() {
  //this makes sure the total values do not exceed 100
  var sum = Number(0);
  document.querySelectorAll(".baserunninginput").forEach((item) => {
    sum = sum + Number(item.value);
  });
  if (sum > 100) {
    // this.value = 100 - (sum - this.value);
    document.querySelectorAll(".errorbaserunning").forEach((item) => {
      item.style.display = "block";
    });
    lessthanhundredbaserunning = false;
  } else {
    lessthanhundredbaserunning = true;
  }
  //update the current sum that is displayed to the user
  document.getElementById("baserunningsumcheck").innerHTML = sum;
  //if sum is 100, make the color green, otherwise make it black (or red if error)
  if (positivebaserunning == false) {
    document.getElementById("baserunningsumcheck").style.color = primarycolor;
    document.getElementById("baserunningsumcheck").innerHTML =
      "please remove negative number in the '" +
      document
        .getElementById(negbaserunning)
        .previousElementSibling.textContent.replace(" -", "") +
      "' input box";
  } else if (sum > 100) {
    document.getElementById("baserunningsumcheck").style.color = primarycolor;
  } else if (sum < 100) {
    document.getElementById("baserunningsumcheck").style.color = darkcolor;
  } else {
    document.getElementById("baserunningsumcheck").style.color = "green";
  }

  if (positivebaserunning && lessthanhundredbaserunning) {
    document.querySelectorAll(".errorbaserunning").forEach((item) => {
      item.style.display = "none";
    });
  }
}

//set the approvenewbaserunninginput function to apply to all baserunninginput variables
document.querySelectorAll(".baserunninginput").forEach((item) => {
  item.oninput = approveNewBaserunningInput;
  if (item.value > 0) {
    item.parentElement.querySelector(".value-title").style.color = inputcolor;
  }
  item.onchange = baserunningOnChange;
});

function baserunningOnChange(event) {
  if ((this.value * 100) % 1 != 0) {
    this.value = parseFloat(this.value).toFixed(2);
  }
  baserunningSum();
  var fixedbaserunningsum = document.getElementById(
    "baserunningsumcheck"
  ).innerHTML;
  // console.log(fixedbaserunningsum);
  if (!fixedbaserunningsum.includes("please")) {
    if (fixedbaserunningsum == 100) {
      document.getElementById("baserunningsumcheck").innerHTML = "100";
    } else {
      document.getElementById("baserunningsumcheck").innerHTML =
        parseFloat(fixedbaserunningsum).toFixed(2);
    }
  }
}

function approveNewFieldingInput(event) {
  //this keeps everything to three decimal places automatically
  if (this.value > 0) {
    this.parentElement.querySelector(".value-title").style.color = inputcolor;
  } else {
    this.parentElement.querySelector(".value-title").style.color = lightcolor;
  }
  //this.value = parseFloat(this.value).toFixed(2);
  //do not allow negative values
  positivefielding = true;
  document.querySelectorAll(".fieldinginput").forEach((item) => {
    if (item.value < 0) {
      positivefielding = false;
      negfielding = item.id;
      document.querySelectorAll(".errorfielding").forEach((item) => {
        item.style.display = "block";
      });
    }
  });
  fieldingSum();
}

function fieldingSum() {
  //this makes sure the total values do not exceed 100
  var sum = Number(0);
  document.querySelectorAll(".fieldinginput").forEach((item) => {
    sum = sum + Number(item.value);
  });
  if (sum > 100) {
    // this.value = 100 - (sum - this.value);
    document.querySelectorAll(".errorfielding").forEach((item) => {
      item.style.display = "block";
    });
    lessthanhundredfielding = false;
  } else {
    lessthanhundredfielding = true;
  }
  //update the current sum that is displayed to the user
  document.getElementById("fieldingsumcheck").innerHTML = sum;
  //if sum is 100, make the color green, otherwise make it black (or red if error)
  if (positivefielding == false) {
    document.getElementById("fieldingsumcheck").style.color = primarycolor;
    document.getElementById("fieldingsumcheck").innerHTML =
      "please remove negative number in the '" +
      document
        .getElementById(negfielding)
        .previousElementSibling.textContent.replace(" -", "") +
      "' input box";
  } else if (sum > 100) {
    document.getElementById("fieldingsumcheck").style.color = primarycolor;
  } else if (sum < 100) {
    document.getElementById("fieldingsumcheck").style.color = darkcolor;
  } else {
    document.getElementById("fieldingsumcheck").style.color = "green";
  }

  if (positivefielding && lessthanhundredfielding) {
    document.querySelectorAll(".errorfielding").forEach((item) => {
      item.style.display = "none";
    });
  }
}

//set the approvenewfieldinginput function to apply to all fieldinginput variables
document.querySelectorAll(".fieldinginput").forEach((item) => {
  item.oninput = approveNewFieldingInput;
  // console.log(item.value);
  if (item.value > "0") {
    item.parentElement.querySelector(".value-title").style.color = inputcolor;
  }
  item.onchange = fieldingOnChange;
});

function fieldingOnChange(event) {
  if ((this.value * 100) % 1 != 0) {
    this.value = parseFloat(this.value).toFixed(2);
  }
  fieldingSum();
  var fixedfieldingsum = document.getElementById("fieldingsumcheck").innerHTML;
  // console.log(fixedfieldingsum);
  if (!fixedfieldingsum.includes("please")) {
    if (fixedfieldingsum == 100) {
      document.getElementById("fieldingsumcheck").innerHTML = "100";
    } else {
      document.getElementById("fieldingsumcheck").innerHTML =
        parseFloat(fixedfieldingsum).toFixed(2);
    }
  }
}

//verification of input
function approveNewPitchingInput(event) {
  //this keeps everything to three decimal places automatically
  if (this.value > 0) {
    this.parentElement.querySelector(".value-title").style.color = inputcolor;
  } else {
    this.parentElement.querySelector(".value-title").style.color = lightcolor;
  }
  //this.value = parseFloat(this.value).toFixed(2);
  //do not allow negative values
  positivepitching = true;
  document.querySelectorAll(".pitchinginput").forEach((item) => {
    if (item.value < 0) {
      positivepitching = false;
      negpitching = item.id;
      document.querySelectorAll(".errorpitching").forEach((item) => {
        item.style.display = "block";
      });
    }
  });
  pitchingSum();
}

function pitchingSum() {
  //this makes sure the total values do not exceed 100
  var sum = Number(0);
  document.querySelectorAll(".pitchinginput").forEach((item) => {
    sum = sum + Number(item.value);
  });
  if (sum > 100) {
    // this.value = 100 - (sum - this.value);
    document.querySelectorAll(".errorpitching").forEach((item) => {
      item.style.display = "block";
    });
    lessthanhundredpitching = false;
  } else {
    lessthanhundredpitching = true;
  }
  //update the current sum that is displayed to the user
  document.getElementById("pitchingsumcheck").innerHTML = sum;
  //if sum is 100, make the color green, otherwise make it black (or red if error)
  if (positivepitching == false) {
    document.getElementById("pitchingsumcheck").style.color = primarycolor;
    document.getElementById("pitchingsumcheck").innerHTML =
      "please remove negative number in the '" +
      document
        .getElementById(negpitching)
        .previousElementSibling.textContent.replace(" -", "") +
      "' input box";
  } else if (sum > 100) {
    document.getElementById("pitchingsumcheck").style.color = primarycolor;
  } else if (sum < 100) {
    document.getElementById("pitchingsumcheck").style.color = darkcolor;
  } else {
    document.getElementById("pitchingsumcheck").style.color = "green";
  }

  if (positivepitching && lessthanhundredpitching) {
    document.querySelectorAll(".errorpitching").forEach((item) => {
      item.style.display = "none";
    });
  }
  // notready();
}

//set the approvenewpitchinginput function to apply to all pitchinginput variables
document.querySelectorAll(".pitchinginput").forEach((item) => {
  item.oninput = approveNewPitchingInput;
  if (item.value > 0) {
    item.parentElement.querySelector(".value-title").style.color = inputcolor;
    // console.log("checked pitching");
  }
  item.onchange = pitchingOnChange;
});

function pitchingOnChange(event) {
  if ((this.value * 100) % 1 != 0) {
    this.value = parseFloat(this.value).toFixed(2);
  }
  pitchingSum();
  var fixedpitchingsum = document.getElementById("pitchingsumcheck").innerHTML;
  // console.log(fixedpitchingsum);
  if (!fixedpitchingsum.includes("please")) {
    if (fixedpitchingsum == 100) {
      document.getElementById("pitchingsumcheck").innerHTML = "100";
    } else {
      document.getElementById("pitchingsumcheck").innerHTML =
        parseFloat(fixedpitchingsum).toFixed(2);
    }
  }
}

function approveNewCategoryInput(event) {
  //this keeps everything to three decimal places automatically
  //this.value = parseFloat(this.value).toFixed(2);
  //do not allow negative values
  if (this.value < 0) {
    document.querySelectorAll(".errorcategories").forEach((item) => {
      item.style.display = "block";
    });
    // this.value = 0;
    positivecategory = false;
  } else {
    positivecategory = true;
  }
  //this makes sure the total values do not exceed 100
  var sum = Number(0);
  document.querySelectorAll(".categoryinput").forEach((item) => {
    sum = sum + Number(item.value);
  });
  if (sum > 100) {
    // this.value = 100 - (sum - this.value);
    document.querySelectorAll(".errorcategories").forEach((item) => {
      item.style.display = "block";
    });
    lessthanhundredcategory = false;
  } else {
    lessthanhundredcategory = true;
  }
  //this.value = parseFloat(this.value).toFixed(2);
  if (positivecategory && lessthanhundredcategory) {
    document.querySelectorAll(".errorcategories").forEach((item) => {
      item.style.display = "none";
    });
  }
  // notready();
}

//set the approvenewcategoryinput function to apply to all categoryinput variables
document.querySelectorAll(".categoryinput").forEach((item) => {
  item.oninput = approveNewCategoryInput;
  item.onchange = threedplaces;
});

document.querySelectorAll(".seasonweightsinput").forEach((item) => {
  item.oninput = approveNewSeasonWeightsInput;
  item.onchange = threedplaces;
});

//starter innings should round to 0.0, 0.1, 0.2
function starterinnings(event) {
  // document.getElementById("inningsinput").value = parseFloat(
  //   document.getElementById("inningsinput").value
  // ).toFixed(1);
  if (document.getElementById("inningsinput").value > 9) {
    document.querySelectorAll(".errorinnings").forEach((item) => {
      item.style.display = "block";
    });
    // document.getElementById("inningsinput").value = 9;
  } else if (document.getElementById("inningsinput").value < 1) {
    document.querySelectorAll(".errorinnings").forEach((item) => {
      item.style.display = "block";
    });
    // document.getElementById("inningsinput").value = 1;
  } else if (document.getElementById("inningsinput").value % 1 > 0.21) {
    // document.getElementById("inningsinput").value =
    //   document.getElementById("inningsinput").value -
    //   (document.getElementById("inningsinput").value % 1) +
    //   0.2;
    document.querySelectorAll(".errorinnings").forEach((item) => {
      item.style.display = "block";
    });
  } else {
    document.querySelectorAll(".errorinnings").forEach((item) => {
      item.style.display = "none";
    });
  }
}

function inningsdplaces(event) {
  if ((this.value * 10) % 1 != 0) {
    this.value = parseFloat(this.value).toFixed(1);
  }
}

document.getElementById("inningsinput").oninput = starterinnings;
document.getElementById("inningsinput").onchange = inningsdplaces;

//when the page loads, if something other than auto is selected, I need to deselect auto
document.querySelectorAll(".homefieldradio").forEach((item) => {
  if (item.id != "homefieldauto" && item.checked == true) {
    document.getElementById("homefieldauto").checked = false;
  }
  if (document.getElementById("homefieldmanual").checked) {
    document.getElementById("homefieldmanualinput").style.display = "flex";
  }
});

document.querySelectorAll(".seasonweightsradio").forEach((item) => {
  if (item.id != "seasonweightsauto" && item.checked == true) {
    document.getElementById("seasonweightsauto").checked = false;
  }
  if (document.getElementById("seasonweightsmanual").checked) {
    document.getElementById("threeyearmanualinput").style.display = "flex";
  }
});

document.querySelectorAll(".plusradio").forEach((item) => {
  if (item.id != "plusstandard" && item.checked == true) {
    document.getElementById("plusstandard").checked = false;
  }
});

document.querySelectorAll(".bsrfldradio").forEach((item) => {
  if (item.id != "bsrfldauto" && item.checked == true) {
    document.getElementById("bsrfldauto").checked = false;
  }
  if (document.getElementById("bsrfldmanual").checked) {
    document.getElementById("bsrfldinput").style.display = "flex";
  }
});

document.getElementById("userweightsform").onsubmit = loadingPage;
document.getElementById("userweightsformsubmitreal").onclick = loadingCircle;
// document.getElementById("loading").style.display = "none";
document.getElementById("loadingcircle").style.display = "none";

document.addEventListener("visibilitychange", () => {
  document.getElementById("submitbutton").style.display = "block";
  // document.getElementById("loading").style.display = "none";
  document.getElementById("loadingcircle").style.display = "none";
});

dots = window.setInterval(function () {
  var wait = document.getElementById("dotdotdot");
  if (wait.innerHTML.length > 2) wait.innerHTML = "";
  else wait.innerHTML += ".";
}, 300);

function loadingPage(event) {
  console.log("submitted");
  document.getElementById("submitbutton").style.display = "none";
  // document.getElementById("loading").style.display = "flex";
}

function loadingCircle(event) {
  document.getElementById("loadingcircle").style.display = "flex";
}
