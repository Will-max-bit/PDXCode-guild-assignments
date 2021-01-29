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
        sunset: '',
        sunrise: '',
        hours: '',
        weekly: '',

        
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
                // console.log(response.data),
                console.log(response.data.daily)
                this.currentTemp = parseInt((response.data.current.feels_like - 273.15)* (9/5) + 32)
                let unix_date = (response.data.current.dt)
                let date_Time = new Date(unix_date * 1000)
                this.dateTime= date_Time
                // console.log(response.data.daily)
                // console.log(response.data.current.weather[0].id)
                this.iconDescription = response.data.current.weather[0].description
                this.icon = "http://openweathermap.org/img/wn/" + response.data.current.weather[0].icon +'@4x.png'
                
                let sunriseUnix = response.data.current.sunrise
                non_unixDate_rise = new Date(sunriseUnix * 1000)
                let sunrise_hours = (non_unixDate_rise.getHours()- 12)
                let sunrise_min = (non_unixDate_rise.getMinutes())
                this.sunrise = (sunrise_hours) +':' + sunrise_min +'a.m'

                let sunsetUnix = response.data.current.sunset
                let non_unixDate = new Date(sunsetUnix  * 1000)
                let sunset_hours = (non_unixDate.getHours()- 12)
                let sunset_min = (non_unixDate.getMinutes())
                this.sunset = sunset_hours +':' + sunset_min +'p.m'
                this.weekly = response.data.daily
                
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
            

        },
        // weeklyForecast: function(){

        // }
        
        
    },
    created: function(){
            // this.weather_call()
            this.location_call()
        },
    
})


