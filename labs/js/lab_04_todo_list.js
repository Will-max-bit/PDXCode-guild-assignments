let input_field = document.querySelector('#input_field')
let enter_Button = document.querySelector('#enter_Button')
let table_contents = document.querySelector('#table_contents')
let complete_button = document.querySelector('#complete_button')
let table_completed = document.querySelector('#table_completed')



enter_Button.addEventListener('click', function (evt) {
    let item = input_field.value
    console.log(item)

    if (item === '') {
        alert('Enter a valid selection')
        return
    }


    let tr = document.createElement('tr')
    let td_item = document.createElement('td')
    td_item.innerText = item
    tr.appendChild(td_item)

    table_contents.appendChild(tr)

    let td_btn_complete = document.createElement('td')
    let span_complete = document.createElement('span')
    span_complete.innerText = '✓'
    span_complete.classList.add('btn', 'btn-outline-success')
    td_btn_complete.appendChild(span_complete)
    tr.appendChild(td_btn_complete)

    let span_delete = document.createElement('span')
    span_delete.innerText = '❌'
    span_delete.classList.add('btn', 'btn-danger')

    span_complete.addEventListener('click', function () {
        table_contents.removeChild(tr)

        let tr_completed = document.createElement('tr')
        let td_item_completed = document.createElement('td')
        td_item_completed = td_item
        tr_completed.appendChild(td_item_completed)
        tr_completed.appendChild(span_delete)
        table_completed.appendChild(tr_completed)
        // table_completed.appendChild(span_delete)
        
        span_delete.addEventListener('click', function () {
            table_completed.removeChild(tr_completed)
            // table_completed.removeChild(span_delete)


        })


    })











})




