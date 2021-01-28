let app = new Vue({
    el: '#app',
    data: {
        cat_photo: '',
        // categories: 'test',
        category: '',
        breed: '',
        
    },
    methods: {
        cat_picture: function () {
            axios({
                method: 'get',
                url: 'https://api.thecatapi.com/v1/images/search',
                params: {
                    category_ids: this.category,
                    breed_ids: this.breed,
                }
            }).then((response) => {
                console.log(response.data)
                if ( response.data.length === 0) {
                    this.cat_photo = 'https://http.cat/404'
                    this.page_reload()
                } else {
                    this.cat_photo = response.data[0].url
                }
                
                
                
            })
        },
        moreCats: function () {
            this.cat_picture()
        },     
        // https://api.thecatapi.com/v1/images/search?category_ids=1
        cat_categories: function(){
            axios({
                method: 'get',
                url: 'https://api.thecatapi.com/v1/categories'
            }).then((response) => {
                this.cat_categories = response.data
                // console.log(this.cat_categories)
            })
        },
       cat_breeds: function(){
        axios({
            method: 'get',
            url: 'https://api.thecatapi.com/v1/breeds'
        }).then((response) => {
            this.cat_breeds = response.data
            // console.log(this.cat_breeds)
        })
       }
    },
    created: function () {
        this.moreCats()
        this.cat_picture()
        this.cat_categories()
        this.cat_breeds()
    },
    page_reload: function(){
        setTimeout(location.reload(), 3000)
    }
})
