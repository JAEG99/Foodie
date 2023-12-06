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

// recipes.js

$(document).ready(function () {
  // Fetch and display all recipes initially
  fetchRecipes("");

  // Handle search bar input
  $("#recipeSearch").on("input", function () {
      const searchTerm = $(this).val();
      fetchRecipes(searchTerm);
  });

  function fetchRecipes(searchTerm) {
      // Make an AJAX request to your Flask endpoint to fetch recipes
      $.ajax({
          type: "GET",
          url: "{{ url_for('api_get_recipes') }}",  // Replace with your actual Flask endpoint
          data: { search: searchTerm },
          success: function (data) {
              displayRecipes(data);
          },
          error: function (error) {
              console.error("Error fetching recipes:", error);
          }
      });
  }

  function displayRecipes(recipes) {
      // Clear existing recipe cards
      $("#recipeList").empty();

      // Loop through recipes and create HTML cards
      recipes.forEach(function (recipe) {
          const cardHtml = `
              <div class="col-md-4 mb-4">
                  <div class="card">
                      <div class="card-body">
                          <h5 class="card-title">${recipe.recipe_name}</h5>
                          <p class="card-text">${recipe.instructions}</p>
                      </div>
                  </div>
              </div>
          `;
          $("#recipeList").append(cardHtml);
      });
  }
});
