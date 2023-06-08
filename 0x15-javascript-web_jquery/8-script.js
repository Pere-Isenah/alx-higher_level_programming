$(document).ready( function () {
    $.ajax( {
        url: "https://swapi-api.alx-tools.com/api/films/?format=json",
        success : function(res) {
            for( item in res){
                if( item === "results"){
                    for (value of res[item]) {
                        for (values in value) {
                            if( values === "title"){
                                // console.log(value[values])
                                $("#list_movies").prepend("<li>1<li>")
                        }}
                    }
                }
            } 
        }
})
})