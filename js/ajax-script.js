$(document).ready(function() {
  $.ajax({
    url: '../js/mobile-data.js',
    dataType: 'json',
    success: function() {
      // The 'mobiles' variable is now available here
      var data = mobiles;
      // Generate HTML for each mobile in the data array and append it to the container
      for (var i = 0; i < data.length; i++) {
        var mobile = data[i];
        var html = '<div class="mobile">';
        html += '<h5 class="name">' + mobile.name + '</h5>';
        html += '<p class="phone">Phone: ' + mobile.phoneNumber + '</p>';
        html += '<p class="email">Email: ' + mobile.email + '</p>';
        html += '</div>';
        $('#dataContainer').append(html);
      }
    },
    error: function() {
      // Handle error case
      $('#dataContainer').html('<p>Error loading data.</p>');
    }
  });
});