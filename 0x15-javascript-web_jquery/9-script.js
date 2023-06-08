$(document).ready( function () {
    $.ajax( {
        url: "https://fourtonfish.com/hellosalut/?lang=fr",
        success : function(res) {
            console.log(res.name)
            $("#hello").prepend(`<p>${res.name}</p>`)
        }}
)})
