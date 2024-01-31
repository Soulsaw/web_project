$(document).ready(function () {
  const selectedAmenities = {};

  $('input[type="checkbox"]').change(function () {
    const amenityId = $(this).attr('data-id');
    const amenityName = $(this).attr('data-name');

    if ($(this).is(':checked')) {
      selectedAmenities[amenityId] = amenityName;
    } else {
      delete selectedAmenities[amenityId];
    }

    updateAmenitiesList();
  });

  function updateAmenitiesList () {
    const amenitiesList = Object.values(selectedAmenities).join(', ');
    $('DIV.amenities h4').text(amenitiesList);
  }
});
