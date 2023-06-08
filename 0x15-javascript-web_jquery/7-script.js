$(document).ready( function () {
    $.ajax( {
        url: "https://swapi-api.alx-tools.com/api/people/5/?format=json",
        success : function(res) {
            for( item in res){
                if( item === "name"){
                    $("#character").text(res[item])
                    break;
                }
            } 
        }
})
})