$(document).ready(function () {
    $(".username-button").click(function () {
        $(".dropdown-menu").toggle();
    });

    $(document).click(function (e) {
        const dropdown = $(".username-dropdown");

        if (!dropdown.is(e.target) && dropdown.has(e.target).length === 0) {
            $(".dropdown-menu").hide();
        }
    });
});