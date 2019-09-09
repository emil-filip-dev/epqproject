$(document).ready(function() {
    // Adjust the table width upon loading the webpage
    adjustMainTableWidth();

    // Adjust the table width whenever the browser is resized
    $(window).resize(function() {
        adjustMainTableWidth();
    });

    // Add functionality for tab menu buttons once they get clicked
    // and also change the colour of the button representing the current tab
    var currentTab = $("#tabMenuCell").attr("data-currentTab");
    var tabMenuButtons = $("#tabMenuButtons").children("button");
    tabMenuButtons.each(function(index) {
        var button = tabMenuButtons[index];
        var buttonTab = $(button).attr("data-tab");
        $(button).click(function() {
            window.location.replace("/" + buttonTab);
        });
        if (buttonTab === currentTab) {
            $(button)
            .css({
                "background-image":
                    "linear-gradient(rgba(6, 26, 95, 1), rgba(106, 90, 205, 1) 40%, rgba(125, 255, 255, 1))"
            })
        }
    });

    // Remove the table row containing the navigation buttons if they are both hidden
    if ($("#backButton").css("visibility") === "hidden" && $("#nextButton").css("visibility") === "hidden") {
        $("#navRow").remove();
    }
});

// Make the percentage of the browser window that the main table takes up to increase as the browser window width
// decreases
function adjustMainTableWidth() {
    var maxWidth = 1920;
    var width = $(window).width();
    var widthDif = maxWidth - width;

    var percentage = 0.5 + (widthDif / maxWidth);
    if (percentage > 1.0) {
        percentage = 1.0;
    }

    $("#mainTable")
    .css({
        "width": (100 * percentage).toString(10) + "%",
        "left": ((100 - (100 * percentage)) / 2).toString(10) + "%"
    })
    .css({
        "width": "-=32px",
        "left": "+=16px"
    });
}

function adjustResizeableElements() {
    var maxWidth = 1920;
    var maxTableWidth = maxWidth / 2;
    var maxContentFrameWidth = maxTableWidth * 0.75;
}