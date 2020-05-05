var updateBtns=document.getElementsByClassName('update-carte')

for(var i=0;i<updateBtns.length;i++){
    updateBtns[i].addEventListener('click',function(){
        var productId=this.dataset.product
        var action=this.dataset.action
        console.log('productId',productId,'action',action)

        console.log('User:', user)
        if (user=='AnonymouseUser') {
            console.log('Not Logged in')
        }else{
            updateUserOrder(productId,action)
        }

    })
}

function updateUserOrder(productId,action){
    console.log('User is logged in,sending data')
    var url='/updateitem/'

    fetch(url,{
        method:'POST',
        headers: {
            'Content-Type':'application.json',
            'X-CSRFTOKEN':csrftoken,
        },
        body:JSON.stringify({'productId':productId,'action':action})
    })
    .then((Response)=>{
        return Response.json()
    })
    .then((data)=>{
        console.log('data',data)
        location.reload()
    })
}