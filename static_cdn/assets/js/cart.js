var updateBtns = document.getElementsByClassName('update-car')

for(var i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('productId: ',productId, 'action: ', action)

        console.log('User: ', user)
        if(user === 'AnonymousUser'){
            alert('You are not logged in')
        }else{
            updateUserOrder(productId, action)
        }
    })
}

function updateUserOrder(productId, action){
    alert('User logged in, sending data..')

    var url='/update_item/'

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Tye': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body:JSON.stringify({'productId': productId, 'action':action })
    })
    .then((response) => {
        return response.json()
    })

    .then((data) => {
        console.log('data:', data)
    })
}