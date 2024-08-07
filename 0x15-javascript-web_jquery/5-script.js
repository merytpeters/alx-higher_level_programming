$(document).ready(function () {
  // Add a click event listener to div
  $('#add_item').click(function () {
    // Append Item
    $('.my_list').append('<li>Item</li>');
  });
});
