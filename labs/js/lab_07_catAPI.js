let app = new Vue({
    el: '#app',
    data: {
        message: 'Hello world',
        cat_photo: '',
        categories: 'test',
        category: '',
        rowID: '',
    },
    methods: {
        cat_picture: function () {
            axios({
                method: 'get',
                url: 'https://api.thecatapi.com/v1/images/search'
            }).then((response) => {
                this.cat_photo = response.data[0].url
                // console.log(this.cat_photo)
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
                console.log(this.cat_categories)
            })
        },
        category_function: function category_function(rowID,$event){
            alert('test')
            console.log(rowID)
            console.log($event)
        }
    },
    created: function () {
        this.cat_picture()
        this.cat_categories()
    }
})
