function myFunction(){
    // accessing new data points
    var x1 = document.getElementsByName("numbers")[0].value;
    var x2 = document.getElementsByName("numbers")[1].value;
    var x3= document.getElementsByName("numbers")[2].value;
    var x4= document.getElementsByName("numbers")[3].value;
    var x5= document.getElementsByName("numbers")[4].value;
    
    // storing the variables in a 2d array
    var X_array = [[Number(x1), Number(x2), Number(x3), Number(x4), Number(x5)]]
    
    // writing message to console
    console.log(X_array,  JSON.stringify(X_array))

    // run a jQuery: AJAX using the POST method
    $.ajax({
        url: '/predict',
        type:'POST',
        // headers:{
        //     ["Content-Type"]: 'application/json'
        // },
        data:{
            X: JSON.stringify(X_array)
        },

        // receive response from FLask app
        success:function(response){
            console.log(response)
            
            // Writing response in demo id
            $('#demo').text(`Probability:${response.results.results} %`)
        },
        error: function(errorResponse){
            alert('Some Error occured')
            console.log('Errors')
            console.log(errorResponse)
        }
    })
}