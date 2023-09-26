


// Main function starts after the DOM was loaded
document.addEventListener('DOMContentLoaded', function() {
    console.log('DOM loaded');
    const likeButton = document.getElementById('add-to-favourites');
    likeButton.addEventListener('click', () => likeButtonPressed(likeButton));
})


function likeButtonPressed(likeButton) {
    var icon = likeButton.querySelector('#like-icon');
    var job_posting_uuid = window.location.href.split('/').slice(-2)[0];
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