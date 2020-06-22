$(function(){
    $(".forshow").on('click',()=>{
        // alert('hehehehehe')
        $(".mynavbar").css('display','block')
        $(".forshow").css('display','none')
    })
    $(".forclose").on('click',()=>{
        $(".mynavbar").css('display','none')
        $(".forshow").css('display','block')
    })
})