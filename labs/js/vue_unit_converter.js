
let app = new Vue({
    el: '#app',
    data: {
    //   message: 'Hello Vue!',
      options1: '',
      options2: '',
      distance: '',
      results: '',
    //   
    
    },
    methods: {
        outPut: function() {
            // alert('test')
            if (this.distance === ''){
                alert('invalid selection')
            }
            dictConversions = {
                'ft': 0.3048,
                'mi': 1609.34,
                'km': 1000,
                'yd': 0.9144,
                'in': 0.0254,
                'mt': 1,
            }
            let result = dictConversions[this.options1] * this.distance / dictConversions[this.options2]
            results = document.querySelector('#results')
            results.innerHTML = result
            


        }
    }
  })
