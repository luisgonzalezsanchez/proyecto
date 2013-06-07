$(function(){
  $("a").on("click", function(){
    return confirm("are you sure you want to remove this?");
  });
});
