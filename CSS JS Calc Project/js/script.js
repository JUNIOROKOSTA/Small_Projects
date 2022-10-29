var inputDisplay = document.querySelector('.value');
var onCliclCalc = document.querySelectorAll('.num');
var result = [];
var calcResult = 0;

for(i=0; i< onCliclCalc.length; i++){
    onCliclCalc[i].addEventListener('click', function(e){
        var btn = e.target.innerText;
        calcCalc(btn)
    })
};

function calcDisplay(btn){
    resultCalc(btn);   
};

function displayCalc(btn){
    inputDisplay.value+= btn;
};

function resultCalc(btn){
    var g=result.length;
    var n= (result.toString())
    n = (n.replace(/,/g, "")).length;
    console.log(n)

    if(g > 19){
        goResultCalc();
    } else if(n > 19){
        inputDisplay.value="ERRO!!!"
        return;
    } else if(g < 19){
        result.push(btn)
        displayCalc(btn);
    }
};

function goResultCalc(){
    var t = result.toString();
    t = t.replace(/,/g, "");
    inputDisplay.value= eval(t);
    result=[eval(t)];
};

function cleaResult(){
    inputDisplay.value= " ";
    result=[];
};

function calcCalc(btn){
    switch(btn){
        case "9":
            calcDisplay("9");
            break;
        case "8":
            calcDisplay("8");
            break;
        case "7":
            calcDisplay("7");
            break;
        case "6":
            calcDisplay("6");
            break;
        case "5":
            calcDisplay("5");
            break;
        case "4":
            calcDisplay("4");
            break;
        case "3":
            calcDisplay("3");
            break;
        case "2":
            calcDisplay("2");
            break;
        case "1":
            calcDisplay("1");
            break;
        case "0":
            calcDisplay("0");
            break;
        case "C":
            cleaResult();
            break;

        case ".":
            calcDisplay(".");
            break;

        case "+":
            calcDisplay("+");
            break;
        case "-":
            calcDisplay("-");
            break;
        case "*":
            calcDisplay("*");
            break;
        case "/":
            calcDisplay("/");
            break;
        case "=":
            goResultCalc();
            break;
    };
};