window.onload =
function () {

 $('.baskets_lst').on('click', 'input[type="number"]',  function(){
    var t_href = event.target;
    $.ajax({
        url:'/baskets/edit/'+ t_href.name + '/' + t_href.value + '/',
        success: function(data){
            $('.baskets_lst').html(data.result)
        }
    })
    event.preventDefault();
 });
};

