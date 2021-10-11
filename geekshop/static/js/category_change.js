$('document').ready(
function () {
console.log('load')
 $('.category').on('click', 'a', function(){
//    var t_href = event.target;
    console.log(event);
    console.log('click');

   event.preventDefault();
 });
 })