$(document).ready(function () {
    $(".sign-in-tab-label").click(function () {
        $(".sign-up-form").hide();
        $(".sign-in-form").show();
    });

    $(".sign-up-tab-label").click(function () {
        $(".sign-in-form").hide();
        $(".sign-up-form").show();
    });
});