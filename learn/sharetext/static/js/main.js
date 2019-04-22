function fetch_result()
  {
    $.ajax(
      {
        url: "city",
        data : {'state' : $('#state').val()},
        success: function(xhr){
          $("#city").empty();
          $("#city").append(xhr);

  },
         error: function(xhr){
     alert("An error occured: " + xhr.status + " " + xhr.statusText);
   }
 }
 );
  }
