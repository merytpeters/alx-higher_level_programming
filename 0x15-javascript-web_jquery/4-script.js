$(document).ready(function () {
  // Add a click event listener to div
  $('#toggle_header').click(function () {
    // Select the header element using Jquery
    $('header').toggleClass('red green');
  });
});
