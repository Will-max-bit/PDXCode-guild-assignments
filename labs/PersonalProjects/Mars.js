let app = new Vue({
    el: '#app',
    data: {

    },
    methods: {
        insightWeather: function () {
            axios({
                method: 'get',
                url: `https://api.nasa.gov/insight_weather/?api_key=${nasa}&feedtype=json&ver=1.0`,
                // params: {
                //     api_key: nasa,
                //     feedtype: JSON,
                //     version: 1.0,
                // }
            }).then(response => {
                console.log(response.data)
                let JSO = response.data
                let sol = JSO.sol_keys[0]
                console.log(JSO[sol].First_UTC)
            })
        }
    },
    created: function(){
        this.insightWeather()
    }





})