$(document).ready(function() {
    // Adjust the table width upon loading the webpage
    adjustMainTableWidth();

    // Adjust the resizeables width upon loading the content iframe
    $("#content").on("load", function() {
        adjustResizeableElements();
    });

    // Adjust the table width and resizeables whenever the browser is resized
    $(window).resize(function() {
        adjustMainTableWidth();
        adjustResizeableElements();
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
    // Hard-coded as a reference
    var maxWidth = 1920;
    var maxTableWidth = maxWidth / 2;
    var maxContentFrameWidth = maxTableWidth * 0.75;

    // Calculate how much to increase the percentage width by
    var content = $("#content");
    var contentFrameWidth = $(content).width();
    var percentIncrease = 100 - ((contentFrameWidth / maxContentFrameWidth) * 100);

    // Do the following for each element that can be resized
    var resizeables = $(content).contents().find(".resizeable");
    resizeables.each(function(index) {
        // Calculate the new percentage width of the element
        var resizeable = resizeables[index];
        var percentageWidth = parseFloat($(resizeable).attr("data-initialWidthPercentage"));
        percentageWidth += percentIncrease;
        if (percentageWidth > 100) {
            percentageWidth = 100;
        }

        // Calculate the percentage top padding so as to maintain the aspect ratio of the image
        var image = $(resizeable).children("img")[0];
        var naturalWidth = image.naturalWidth;
        var naturalHeight = image.naturalHeight;
        var paddingTop = (naturalHeight / naturalWidth) * percentageWidth;

        // Resize the element
        $(resizeable)
        .css({
            "width": percentageWidth.toString(10) + "%",
            "padding-top": paddingTop.toString(10) + "%"
        })
    })
}