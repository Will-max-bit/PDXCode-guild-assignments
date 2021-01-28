let app = new Vue({
    el: '#app',
    data: {
        message: 'hello there',
        lat: '',
        lon: '',
        currentTemp: '',
        dateTime: '',
        icon: '',
        iconDescription: '',

        
    },
    methods: {
        weather_call: function () {
            axios({
                method: 'get',
                url: 'https://api.openweathermap.org/data/2.5/onecall',
                params: {
                    lat: this.lat,
                    lon: this.lon,
                    exclude: 'minutely,hourly,alerts',
                    appid: openweathermap_api_key
                }
            }).then(response => {
                console.log(response.data),
                this.currentTemp = parseInt((response.data.current.feels_like - 273.15)* (9/5) + 32)
                let unix_date = (response.data.current.dt)
                let date_Time = new Date(unix_date * 1000)
                this.dateTime= date_Time
                // console.log(response.data.daily)
                console.log(response.data.current.weather[0].id)
                this.iconDescription = response.data.current.weather[0].description
            })
        },
        // lets make a function with a for loop for populating the icons
        // maybe do display the weekly weather to in a bar below?
        location_call: function(){
            axios({
                method: 'get',
                url: "https://geo.ipify.org/api/v1",
                params: {
                    apiKey: geo_Key
                }
            }).then(response => {
                // console.log(response.data)
                this.lat = response.data.location.lat
                this.lon = response.data.location.lng
                this.weather_call()
            })
            

        }
        
        
    },
    created: function(){
            // this.weather_call()
            this.location_call()
        },
    
})


