$(document).ready(function () {
  $("#search-input").keyup(function () {
    var query = $(this).val();
    if (query.length >= 3) {
      $.ajax({
        url: "{% url 'autocomplete_search' %}",
        data: {
          term: query,
        },
        dataType: "json",
        success: function (data) {
          $("#suggestions").empty();
          if (data.length > 0) {
            var suggestions = "<ul>";
            $.each(data, function (index, item) {
              suggestions += "<li>" + item.title + "</li>";
            });
            suggestions += "</ul>";
            $("#suggestions").html(suggestions);
          }
        },
      });
    } else {
      $("#suggestions").empty();
    }
  });

  $(document).on("click", "#suggestions li", function () {
    $("#search-input").val($(this).text());
    $("#suggestions").empty();
  });
});
