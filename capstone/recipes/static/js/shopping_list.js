/* INDEX

1. Main
2. Button delete
3. CSFR Token

*/

// 1. Main
document.addEventListener('DOMContentLoaded', function() {
    const btn_delete = document.querySelectorAll('.btn-list-delete');

    // Button delete on shopping list
    if (btn_delete) {
        btn_delete.forEach(btn => {
            btn.addEventListener('click', event => {
                delete_recipe(event.target.dataset.id);
            })
        })
    }
})

// 2. Button delete on shopping list
/**
* Delete ingredient list
* @param {integer} id - Shopping list id
*/
function delete_recipe(id) {

    // Get token
    const csrfToken = getToken();

    // Delete request for ${id} shopping list
    fetch('', {
        method: 'DELETE',
        headers: {
                'X-CSRFToken': csrfToken
        },
        body: JSON.stringify({
            id: id
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log(data)

        // Remove element from DOM
        const div = document.querySelector(`#shopping-list-structure-${id}`);
        div.remove();
    })
    .catch(error => console.log('Error: ', error))
}

// 3. CRSF Token
/**
* Get CRSF Token from cookies
*/
function getToken() {
    if (document.cookie) {

        const xsrfCookies = document.cookie.split('=');

        if (xsrfCookies.length === 0) {
            return null;
        } else {
            return xsrfCookies[1];
        }
    } else {
        return null;
    }
}
