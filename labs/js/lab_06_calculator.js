var app = new Vue({
    el: '#app',
    data: {
      screen_example: '',
      first_operand: '',
      second_operand: '',
      operator1: '',
    },
    methods: {
        calculate: function(num){
            let first_num = num
        
            this.screen_example += first_num
            
        },
        clear: function(){
            location.reload();
        },
        equals: function(solution){
            this.second_operand = this.screen_example
            // use first operand, second operand and operator to calculate result
            // let result = (this.first_operand, this.operator1, )
            if (this.operator1 === '+'){
                this.screen_example = parseInt(this.first_operand) + parseInt(this.second_operand)
            }
            else if (this.operator1 === '-' ){
                this.screen_example = parseInt(this.first_operand) - parseInt(this.second_operand)
            }
            else if (this.operator1 === '÷' ){
                this.screen_example = parseInt(this.first_operand) / parseInt(this.second_operand)
            }
            else if (this.operator1 === '%' ){
                this.screen_example = (parseInt(this.first_operand) / parseInt(this.second_operand)) *100
            }
            else if (this.operator1 === 'X' ){
                this.screen_example = (parseInt(this.first_operand) * parseInt(this.second_operand))
            }
            else if (this.operator1 === '^' ){
                this.screen_example = (parseInt(this.first_operand) ** parseInt(this.second_operand))
            }
            else if (this.operator1 === '!' ){
                this.screen_example = factorial(this.first_operand)
            }
            else if (this.operator1 === 'Sin' ){
                this.screen_example = Math.sin(this.first_operand)
                console.log(this.screen_example)
            }
            else if (this.operator1 === 'Cos' ){
                this.screen_example = Math.cos(this.first_operand)
                console.log(this.screen_example)
            }
            else if (this.operator1 === 'Tan' ){
                this.screen_example = Math.tan(this.first_operand * Math.PI / 180)
                console.log(this.screen_example)
            }
            else if (this.operator1 === '␡'){
                this.second_operand == ''
            }

            
        },
        operator: function(op){
            this.first_operand = this.screen_example
            if(this.operator1 === '␡'){
                this.first_operand == ''
            }
            else if(this.operator1 === '.'){
                this.first_operand = this.operator1 += this.first_operand
                    this.first_operand = this.screen_example
            }
            this.operator1 = op
            this.screen_example = ''
            
            
            
        },
    
    }
  })

function factorial(num){
    if( num === 0 || num === 1)
    return 1;
    for (let i = num - 1; i >= 1; i--){
        num *= i;
    }
    return num
}
// function sine(num){
//     let result = math.sin(num)
//     return result
// }