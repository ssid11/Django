window.onload =
function () {

 $('.category').on('click', 'a',  function(){
    var t_href = event.target;
    console.log(t_href.id)
    console.log($(this).serialize())
    $.ajax({
        url:'/products/cat_change/'+ t_href.id + '/',
        success: function(data){
            $('.product_box').html(data.result)
        }
    })
//    event.preventDefault();
return false
 });

 $('.baskets_lst').on('click', 'input[type="number"]',  function(){
    var t_href = event.target;
    console.log(t_href.value)
    $.ajax({
        url:'/baskets/edit/'+ t_href.name + '/' + t_href.value + '/',
        success: function(data){
            $('.baskets_lst').html(data.result)
        }
    })
//    event.preventDefault();
return false
 });

 $('.sale').on('click', 'a',  function(){
    var t_href = event.target;
    console.log(t_href.id)
    $.ajax({
        url:'/baskets/add_ajax/'+ t_href.id + '/',
        success: function(data){
        alert(data.result)
        }
    })
//    event.preventDefault();
return false
 });
};