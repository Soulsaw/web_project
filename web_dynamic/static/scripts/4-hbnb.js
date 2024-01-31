$(document).ready(function () {
  $.get('http://0.0.0.0:5001/api/v1/status/', function (data) {
    if (data.status === 'OK') {
      $('div#api_status').addClass('available');
    } else {
      $('div#api_status').removeClass('available');
    }
  });
  $.ajax({
    url: 'http://0.0.0.0:5001/api/v1/places_search',
    type: 'POST',
    contentType: 'application/json',
    data: JSON.stringify({}),
    success: function (responses) {
      $.each(responses, function (i, response) {
        /* Definition of the article content */
        const article = `
        <article>
        <div class="title_box">
        <h2>${response.name}</h2>
        <div class="price_by_night">${response.price_by_night}</div>
        </div>
        <div class="information">
            <div class="max_guest">${response.max_guest} Guests</div>
              <div class="number_rooms">${response.number_rooms} Bedrooms</div>
            <div class="number_bathrooms">${response.number_bathrooms} Bathrooms</div>
        </div>
        <div class="user">
        </div>
        <div class="description">
        ${response.description}
        </div>
        </article>`;
        /* Put the HTML content in the section tag */
        $('SECTION.places').append(article);
      });
    },
    error: function (err) {
      console.log(err);
    }
  });
  const selectedAmenities = {};
  const selectedAmenitiesId = {};
  const amenitiesIds = [];
  $('input[type="checkbox"]').change(function () {
    const amenityId = $(this).attr('data-id');
    const amenityName = $(this).attr('data-name');

    if ($(this).is(':checked')) {
      selectedAmenities[amenityId] = amenityName;
      amenitiesIds.push(amenityId);
    } else {
      delete selectedAmenities[amenityId];
      const idx = amenitiesIds.indexOf(amenityId);
      if (idx !== -1) {
        amenitiesIds.splice(idx, 1);
      }
    }
    selectedAmenitiesId.amenities = amenitiesIds;

    updateAmenitiesList();
  });
  $('button[type="button"]').on('click', filtersPlaces);

  function updateAmenitiesList () {
    const amenitiesList = Object.values(selectedAmenities).join(', ');
    $('DIV.amenities h4').text(amenitiesList);
  }

  function filtersPlaces () {
    $.ajax({
      url: 'http://0.0.0.0:5001/api/v1/places_search',
      type: 'POST',
      contentType: 'application/json',
      data: JSON.stringify(selectedAmenitiesId),
      success: function (responses) {
        $('SECTION.places').empty();
        $.each(responses, function (i, response) {
          /* Definition of the article content */
          const article = `
          <article>
          <div class="title_box">
          <h2>${response.name}</h2>
          <div class="price_by_night">${response.price_by_night}</div>
          </div>
          <div class="information">
              <div class="max_guest">${response.max_guest} Guests</div>
                <div class="number_rooms">${response.number_rooms} Bedrooms</div>
              <div class="number_bathrooms">${response.number_bathrooms} Bathrooms</div>
          </div>
          <div class="user">
          </div>
          <div class="description">
          ${response.description}
          </div>
          </article>`;
          /* Put the HTML content in the section tag */
          $('SECTION.places').append(article);
        });
      },
      error: function (err) {
        console.log(err);
      }
    });
  }
});
