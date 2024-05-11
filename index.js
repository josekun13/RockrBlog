$(document).ready(function(){
    
    $.ajax({url: "/paginaPrincipal", success: function(data){

      

        $.each( data, function( key, val ) { 
            $("#im"+(key+1)).attr("src",val[4]);
            $("#art"+(key+1)).html(val[2]);
            $("#tit"+(key+1)).html(val[1]);
            $("#con"+(key+1)).html(val[3]);
            
            
          });

        
      }});

      $("#btn1").click(function (){
        $.ajax({
            type: 'POST',
            url: '/articulo',
            data: {titulo : $("#tit1").html()},
            success: function(data){
                console.log(data);
                $("#contenedorPrincipal").html(data);
            }
        });

      });
      $("#btn2").click(function (){
        $.ajax({
            type: 'POST',
            url: '/articulo',
            data: {titulo : $("#tit2").html()},
            success: function(data){
                console.log(data);
                $("#contenedorPrincipal").html(data);
            }
        });

      });

      $("#btn3").click(function (){
        $.ajax({
            type: 'POST',
            url: '/articulo',
            data: {titulo : $("#tit3").html()},
            success: function(data){
                console.log(data);
                $("#contenedorPrincipal").html(data);
            }
        });

      });

      $("#btn4").click(function (){
        $.ajax({
            type: 'POST',
            url: '/articulo',
            data: {titulo : $("#tit4").html()},
            success: function(data){
                console.log(data);
                $("#contenedorPrincipal").html(data);
            }
        });

      });

      $("#btn5").click(function (){
        $.ajax({
            type: 'POST',
            url: '/articulo',
            data: {titulo : $("#tit5").html()},
            success: function(data){
                console.log(data);
                $("#contenedorPrincipal").html(data);
            }
        });

      });

      $("#btn6").click(function (){
        $.ajax({
            type: 'POST',
            url: '/articulo',
            data: {titulo : $("#tit6").html()},
            success: function(data){
                console.log(data);
                $("#contenedorPrincipal").html(data);
            }
        });

      });

      $("#btn7").click(function (){
        $.ajax({
            type: 'POST',
            url: '/articulo',
            data: {titulo : $("#tit7").html()},
            success: function(data){
                console.log(data);
                $("#contenedorPrincipal").html(data);
            }
        });

      });

      $("#btn8").click(function (){
        $.ajax({
            type: 'POST',
            url: '/articulo',
            data: {titulo : $("#tit8").html()},
            success: function(data){
                console.log(data);
                $("#contenedorPrincipal").html(data);
            }
        });

      });

      $("#btn9").click(function (){
        $.ajax({
            type: 'POST',
            url: '/articulo',
            data: {titulo : $("#tit9").html()},
            success: function(data){
                console.log(data);
                $("#contenedorPrincipal").html(data);
            }
        });

      });

      $("#btn10").click(function (){
        $.ajax({
            type: 'POST',
            url: '/articulo',
            data: {titulo : $("#tit10").html()},
            success: function(data){
                console.log(data);
                $("#contenedorPrincipal").html(data);
            }
        });

      });

      $("#btn11").click(function (){
        $.ajax({
            type: 'POST',
            url: '/articulo',
            data: {titulo : $("#tit11").html()},
            success: function(data){
                console.log(data);
                $("#contenedorPrincipal").html(data);
            }
        });

      });

     

     

     

  
  }); 

 