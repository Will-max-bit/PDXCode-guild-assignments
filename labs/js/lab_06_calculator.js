var app = new Vue({
    el: '#app',
    data: {
      message: 'Hello Vue!',
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
            else if(this.operator1 === '␡'){
                this.second_operand == ''
            }

            // alert(this.first_operand)
            // alert(this.operator1)
            // alert(this.second_operand)
            
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