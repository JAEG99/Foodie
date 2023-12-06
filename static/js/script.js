/* eslint-disable linebreak-style */
// script.js

// Ensure the document is ready before executing JavaScript
$(document).ready(function() {
  // Initialize the Bootstrap Carousel
  $('#food-carousel').carousel({
    interval: 18000, // Set the interval to 8 seconds
  });
});

$(document).ready(function () {
  // Intercept form submission
  $('#recipeForm').submit(function (e) {
      e.preventDefault(); // Prevent the default form submission


      // Redirect to a success page after submission
      window.location.href = 'success.html';

      // Set a timeout to redirect back to index.html after a certain amount of time (e.g., 5 seconds)
      setTimeout(function () {
          window.location.href = 'index.html';
      }, 5000); // 5000 milliseconds (5 seconds)
  });
});