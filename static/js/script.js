alert ( "script.js OK!" );
function isNumber(){
    var x = document.getElementById("input").value; // get id
    var y = document.getElementById("chb");
    if (x==""||isNaN(x)){ 
        alert("Not number");
        y.innerHTML="No";
    }else{
        alert("Number");
        y.innerHTML="Yes";
    }
}

function changeImage(){
    x = document.getElementById("chi"); // get id
    if (x.src.match("emoji1")){ 
        x.src="static/image/emoji2.png";
    }else{
        x.src="static/image/emoji1.png";
    }
}
