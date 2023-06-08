$(document).ready(function() {
    $("#add_item").click( function() {
      $('ul.my_list').prepend("<li>Item</li>");
    });
  });
  