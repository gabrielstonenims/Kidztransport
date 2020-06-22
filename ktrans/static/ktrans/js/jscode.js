$(function(){
    $(document).on("submit","#contactform",(event)=>{
        event.preventDefault()
        var form_data = $("#contactform").serialize()
        $.ajax({
            type:"POST",
            url:$(this).attr('action'),
            data:form_data,
            success:(response)=>{
                $("input").val('')
                $("textarea").val('')
                alert("Message sent")
            },
            error:(rs,e)=>{
                console.log(rs.responseText)
            }
        })
    })

    // const logo = document.querySelectorAll('#somelogo path')
    // for(let i=0;i < logo.length;i++){
    //     console.log(`Letter ${i} is ${logo[i].getTotalLength()}`)
    // }


    // //for swiper js
  var swiper = new Swiper('.swiper-container', {
    effect: 'coverflow',
    grabCursor: true,
    centeredSlides: true,
    slidesPerView: 'auto',
    coverflowEffect: {
      rotate: 50,
      stretch: 0,
      depth: 100,
      modifier: 1,
      slideShadows : true,
    },
    pagination: {
      el: '.swiper-pagination',
    },
  });

  // for navbar
  $(window).scroll(()=>{
    if($(document).scrollTop() > 50){
        $('nav').addClass('shrink')
    }
    else{
        $('nav').removeClass('shrink')
    }
})


})