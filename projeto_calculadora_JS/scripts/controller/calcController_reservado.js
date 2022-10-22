class calcController{

    constructor(){
        this._lastOperation = '';
        this._lastNumber = '';
        this._operation = [];
        this._locale = 'pt-BR'
        this._displayCalcEl = document.querySelector("#display");
        this._dateEl = document.querySelector("#data");
        this._timeEl = document.querySelector("#hora");
        this._currentDate;
        this.initialize();
        this.initButtonsEvents();
    }

    initialize(){
        this.setDisplayDateTime();
        setInterval(()=>{
            this.setDisplayDateTime();

        }, 1000);

        this.setLastNumberToDisplay();

    }
    clearAll(){
        this._operation = [];
        //this._lastNumber = '';
        //this._lastOperation = '';
        this.setLastNumberToDisplay();

    }

    clearEntry(){
        this._operation.pop();
        this.setLastNumberToDisplay();

    }

    getLastOperation(){
        return this._operation[this._operation.length -1];
    }

    isOperation(value){

        return (['+','-','%','/','*'].indexOf(value) > -1);
    }

    setLastOperation(value){
        this._operation[this._operation.length -1] = value;

    }

    pushOperation(value){
        this._operation.push(value);
        if (this._operation.length > 3){
            
            this.calc();

        }

    }

    getResult(){

        return eval(this._operation.join(""));
    }

    calc(){
        console.log('antes calc> ', this._operation)
        let last = '';
        this._lastOperation = this.getLastItem();

        if (this._operation.length < 3){
            let fistitem = this._operation[0];
            this._operation = [fistitem, this._lastOperation, this._lastNumber];

        }
        
        if(this._operation > 3){
            last = this._operation.pop();

            this._lastNumber = this.getResult();

        } 
        else if(this._operation == 3){

            this._lastNumber = this.getResult(false);
        }

        console.log("lasNumber> ", this._lastNumber);
        console.log("lasOperation> ", this._lastOperation);

        let result = this.getResult();

        if (last == '%'){

            result /= 100;

            this._operation = [result]

        } else {

            this._operation = [result];
            if (last) this._operation.push(last);
        }


        this.setLastNumberToDisplay();

    }

    getLastItem(isOperat = true){
        let lastItem;

        for (let i = this._operation.length-1; i >= 0; i--){
            if(this.isOperation(this._operation[i])== isOperat){
                lastItem = this._operation[i]
                break;
            }
        }

        if (!lastItem){
            lastItem = (isOperat) ? this._lastOperation : this._lastNumber;

        }
        return lastItem;
    }

    setLastNumberToDisplay(){

        let lastNumber = this.getLastItem(false);

        if(!lastNumber){
            lastNumber = 0;
        }

        this.displayCalc = lastNumber;

    }

    addOperation(value){
        if(isNaN(this.getLastOperation())){
            
            if(this.isOperation(value)){
                this.setLastOperation(value);


            } else {
                this.pushOperation(value);
                this.setLastNumberToDisplay();
            }
       
        } else{
            if(this.isOperation(value)){
                this.pushOperation(value)
           
            } else{
                let newValue = this.getLastOperation().toString() + value.toString();
                this.setLastOperation(parseInt(newValue));
                this.setLastNumberToDisplay();
            }      
        }     
    }

    setError(){
        this.displayCalc = "ERROR";
    }

    /*addDot(){

        let lastOperation = this.getLastOperation();

        if (this.isOperator(lastOperation) || !lastOperation) {

            this.pushOperation('0.');

        } else {

            this.setLastOperation(lastOperation.toString() + '.');

        }

        this.setLastNumberToDisplay();
        
    }*/

    execBtn(value){
        switch (value){
            case 'ac':
                this.clearAll();
                break;
            
            case 'ce':
                this.clearEntry();
                break;
            
            case 'soma':
                this.addOperation('+');
                break;
            
            case 'subtracao':
                this.addOperation('-');               
                break;
            
            case 'divisao':
                this.addOperation('/');
                break;
            
            case 'multiplicacao':
                this.addOperation('*');
                break;
            
            case 'porcento':
                this.addOperation('%');
                break;
            
            case 'igual':
                this.calc();
                break;

            case 'ponto':
                this.addDot();
                break;

            case '0':
            case '1':
            case '2':
            case '3':
            case '4':
            case '5':
            case '6':
            case '7':
            case '8':
            case '9':
                this.addOperation(parseInt(value));
                break;                              
            
            default:
                this.setError();
                break;
        }
    }

    addEventListenerAll(element, events,fn){
        events.split(' ').forEach(event =>{
            element.addEventListener(event, fn, false);
        });
    }


    initButtonsEvents(){
        let buttons= document.querySelectorAll("#buttons > g, #parts >g");
        buttons.forEach((btn, index)=>{
            this.addEventListenerAll(btn, 'click drag', e=>{
                let textBtn = btn.className.baseVal.replace("btn-","");
                this.execBtn(textBtn);

            });

            this.addEventListenerAll(btn, "mouseover mouseup mousedown", e => {
                btn.style.cursor = "pointer";
            });
        });
    }

    setDisplayDateTime(){
        this.displayDateEl = this.currentDate.toLocaleDateString(this._locale, {
            day:"2-digit", month: 'long', year: 'numeric'} );
        this.displayTimeEl = this.currentDate.toLocaleTimeString(this._locale);
    }

    get displayDateEl(){
        return this._dateEl.innerHTML;
    }

    set displayDateEl(value){
        return this._dateEl.innerHTML = value;
    }

    get displayTimeEl(){
        this._timeEl.innerHTML;
    }
    
    set displayTimeEl(value){
        this._timeEl.innerHTML = value;
    }

    get displayCalc(){
        return this._displayCalcEl.innerHTML;
    }
    set displayCalc(value){
        this._displayCalcEl.innerHTML = value;
    }

    get currentDate(){
        return new Date();
    }
    set currentDate(value){
        this._currentDate = value;
    }

}


