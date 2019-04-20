$(document).ready(function() {
    $('.sidenav').sidenav();
    $('.parallax').parallax();
    $('.tooltipped').tooltip();
    $('.dropdown-trigger').dropdown();
    $('select').formSelect();
    $('select').material_select();

    // for HTML5 "required" attribute
    $("select[required]").css({
      display: "inline",
      height: 0,
      padding: 0,
      width: 0
    });
});
