let reloadInterval
$('#hacker').ready(function () {  
    setInterval(() => window.location.reload(), 5000);
    reloadInterval = true
})
$(document).on('click', ".open_instagram", function () {
    window.open("https://www.instagram.com/?hl=ha-ng", "_blank");
});

$(document).on('click', ".reload", function () {
    window.location.reload();
});

$(document).on('click', ".toggle-reload", function () {
    
    if (reloadInterval == true) {
        clearInterval(() => window.location.reload(), 5000);
        reloadInterval = null
    } else {
        setInterval(() => window.location.reload(), 5000);
        reloadInterval = true
    }
});
