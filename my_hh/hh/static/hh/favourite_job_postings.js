

document.addEventListener('DOMContentLoaded', function() {

    // Add post to favourites
    const likeButtons = document.querySelectorAll('[id^="add-to-fav-"]');
    likeButtons.forEach(likeButton => likeButton.addEventListener('click', () => addToFavourite(likeButton)));
});


function addToFavourite(likeButton) {
    var job_posting_uuid = likeButton.id.split('add-to-fav-')[1];
    var icon = likeButton.querySelector('#like-icon');
    console.log(icon);
    fetch(`/favourite/${job_posting_uuid}`, {
        method: "PUT",
        headers: {"Content-type": "application/json", "X-CSRFToken": getTokenFromCookie('csrftoken')},
        body: JSON.stringify({
            favourite: true,
        })
    })
    .then(response => response.json())
    .then(result => {
        if (result['currently_favourite'] == false) {
            icon.className = 'fa-regular fa-heart fa-lg';
        } else {
        icon.className = 'fa-solid fa-heart fa-lg';
        }
    });
}


// Gets token from cookie
function getTokenFromCookie(token) {
    const cookie = `; ${document.cookie}`;
    const components = cookie.split(`; ${token}=`);
    if (components.length == 2) return components.pop().split(';').shift();
}