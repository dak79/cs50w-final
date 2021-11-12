document.addEventListener('DOMContentLoaded', function() {
    const btnCardFollow = document.querySelectorAll('.btn-card-follow');
    const btnCardRecipe = document.querySelectorAll('.btn-card-recipe');
    const btnCardComment = document.querySelectorAll('.btn-card-comment');
    const btnCardAddComment = document.querySelectorAll('.btn-card-add-comment')

    // Follow / Unfollow button
    render_btn_follow(btnCardFollow);

    btnCardFollow.forEach(btn =>
        btn.addEventListener('click', event => {
            if (btn.innerHTML === 'Follow') {
                btn_follow(event.target.dataset.id);
                btn.innerHTML = 'Unfollow';
            } else {
                btn_unfollow(event.target.dataset.id);
                btn.innerHTML = 'Follow';
            }
        })
    );

    // Recipe button
    btnCardRecipe.forEach(btn =>
        btn.addEventListener('click', event =>  {
            if (event.target.innerHTML === 'Recipe') {
                btn_recipe(event.target.dataset.id);
                event.target.innerHTML = 'Close';
            } else {
                btn_recipe_close(event.target.dataset.id);
                event.target.innerHTML = 'Recipe';
            }
        })
    );

    // Comment button
    btnCardComment.forEach(btn =>
        btn.addEventListener('click', event => {
            if (event.target.innerHTML === 'Comment') {
                btn_comment(event.target.dataset.id);
                event.target.innerHTML = 'Hide';
            } else {
                btn_comment_close(event.target.dataset.id);
                event.target.innerHTML = 'Comment';
            }
        })
    );

    btnCardAddComment.forEach(btn =>
        btn.addEventListener('click', event => {
            event.preventDefault();
            btn_add_comment(event.target.dataset.id);
        })
    )

})

/**
* Toggle follow / unfollow
* @param {element} button - DOM element follow/unfollow button
*/
function render_btn_follow(button) {

    // Fetch followed recipes
    fetch('api/v1/recipe/follow')
    .then(response => response.json())
    .then(data => {

        // For each recipe render follow/unfollow
        button.forEach(btn => {
            data.forEach(favorite => {
                if (parseInt(favorite['recipe']) === parseInt(btn.dataset.id)) {

                    // Set button to unfollow
                    btn.innerHTML = 'Unfollow';
                }
            })
        })
    })
    .catch(error => console.log('Error: ', error))
}

/**
* Add a recipe to favorite page
* @param {integer} id - Recipe id
*/
function btn_follow(id) {

    // Get user id from template
    const user_id = JSON.parse(document.querySelector('#user_id').textContent);

    // Get token
    const csrfToken = getToken();

    // Add request for ${id} recipe
    fetch('api/v1/recipe/follow', {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json; charset=UTF-8',
            'X-CSRFToken': csrfToken
        },
        mode: 'same-origin',
        body: JSON.stringify({
            user: user_id,
            recipe: id
        })
    })
    .then(response => response.json())
    .then(data => console.log('Success: ', data))
    .catch(error => console.log('Error: ', error))
}

/**
* Delete recipe from favorites
* @param {integer} id - Recipe id
*/
function btn_unfollow(id){

    // Get token
    const csrfToken = getToken();

    // Delete request for ${id} recipe
    fetch('api/v1/recipe/follow', {
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

        // Remove recipe from page
        const card = document.querySelector(`#card-${id}`);
        card.remove();

        // If last recipe remove title and pagination
        const cards = document.querySelectorAll('.card-structure');
        if (cards.length === 1) {
            const pagination = document.querySelector('#pagination-container')
            pagination.remove()

            const title = document.querySelector('#title-container');
            title.remove()
        }
        console.log('Success: ', data)
    })
    .catch(error => console.log('Error: ', error))

}

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

/**
* Show ingredient and preparation steps
* @param {integer} id - Recipe id
*/
function btn_recipe(id) {

    // Fetch ingredient
    fetch(`api/v1/recipe/ingredients/${id}`)
    .then(response => response.json())
    .then(data => {

        // Create container
        const div = document.createElement('div');
        div.setAttribute('id', `ingredients-recipe-${id}`);
        document.querySelector(`#recipe-${id}`).after(div);

        // Create title
        const title = document.createElement('h3');
        title.innerHTML = 'Ingredients:'
        title.classList.add('title-recipe')
        div.append(title);

        // Create button for shopping list
        const btn_shop = document.createElement('button');
        btn_shop.innerHTML = 'Add Ingredient to Shop List';
        btn_shop.classList.add('btn-shop')
        btn_shop.setAttribute(`data-id`, `${id}`);
        div.append(btn_shop);
        btn_shop.addEventListener('click', event => {
            btn_shopping(event.target.dataset.id);

        })

        // Create list of ingredients
        const ul = document.createElement('ul');
        ul.setAttribute('id', `list-ingredients-recipe-${id}`);
        ul.classList.add('list-ingredients');
        document.querySelector(`#ingredients-recipe-${id}`).append(ul);

        // Populate list with ingredient and quantity
        data.forEach(ingredient => {
            const li = document.createElement('li');

            li.innerHTML = `${ingredient['ingredient']} - ${ingredient['quantity']}`
            document.querySelector(`#list-ingredients-recipe-${id}`).append(li);
        })
    })
    .catch(err => console.log('Error: ', err));

    // Fetch preparation steps
    fetch(`api/v1/recipe/preparation/${id}`)
    .then(response => response.json())
    .then(data => {

        // Create container
        const div = document.createElement('div');
        div.setAttribute('id', `preparation-recipe-${id}`);
        document.querySelector(`#recipe-${id}`).after(div);

        // Create title
        const title = document.createElement('h3');
        title.innerHTML = "Preparation:"
        title.classList.add('title-recipe')
        div.append(title);

        // Create list of steps
        const ul = document.createElement('ul');
        ul.setAttribute('id', `list-steps-recipe-${id}`);
        ul.classList.add('list-preparation')
        document.querySelector(`#preparation-recipe-${id}`).append(ul);

        // Populate list of steps
        data.forEach(step => {
            const li = document.createElement('li');

            li.innerHTML = `
                            <img class="preparation-images" src="${step.imageURL}" alt="preparation images" />
                            <p class="preparation-text">${step.step}</p>
                            `

            document.querySelector(`#list-steps-recipe-${id}`).append(li);
        })
    })
    .catch(err => console.log('Error: ', err));
}

/**
* Remove ingredient and preparation steps
* @param {integer} id - Recipe id
*/
function btn_recipe_close(id) {
    const ingredients = document.querySelector(`#ingredients-recipe-${id}`);
    const steps = document.querySelector(`#preparation-recipe-${id}`);

    // Remove ingredients
    ingredients.remove();

    // Remove steps;
    steps.remove();
}

/**
* Show comment form
* @param {integer} id - Recipe id
*/
function btn_comment(id) {

    // Show comment form
    const add_comment = document.querySelector(`#comment-recipe-${id}`);
    add_comment.classList.remove('initial-status');

    // Render comment
    render_comments(id);
}

/**
* Render comments
* @param {integer} id - Recipe id
*/
function render_comments(id) {
    fetch('api/v1/recipe/comment')
    .then(response => response.json())
    .then(data => {
        console.log(data)
        console.log(id)

        // Create a comment container
        const read_comment = document.createElement('div');
        read_comment.setAttribute('id', `read-comment-${id}`);
        document.querySelector(`#add-comment-${id}`).append(read_comment);

        // Create all comment belongs to {id} recipe
        data.forEach(comment => {
            if (id == comment['recipe_id']) {
                const div = document.createElement('div');
                div.setAttribute('id', `comment-${comment['id']}`)
                document.querySelector(`#read-comment-${id}`).append(div);
                div.innerHTML = `
                    <h4>${comment['title']}</h4>
                    <p><small>user: ${comment['user']}</small></p>
                    <p>${comment['body']}</p>
                    <p><small>${comment['date']}</small></p>

                `
            }

        })

    })
    .catch(error => console.log('Error: ', error))
}

/**
* Hide comment form
* @param {integer} id - Recipe id
*/
function btn_comment_close(id) {

    // Hide comment form
    const add_comment = document.querySelector(`#comment-recipe-${id}`);
    add_comment.classList.add('initial-status');

    // Remove comment from DOM
    const clean_comment= document.querySelector(`#read-comment-${id}`);
    clean_comment.remove();
}

/**
* Add a comment to a recipe
* @param {integer} id - Recipe id
*/
function btn_add_comment(id){

    // Get user id from template
    const user_id = JSON.parse(document.querySelector('#user_id').textContent);

    // Get token
    const csrfToken = getToken();

    // Get input fields
    const title = document.querySelector(`#add-comment-title-${id}`);
    const body = document.querySelector(`#add-comment-body-${id}`);

    // Send new comment to back end
    fetch('api/v1/recipe/comment', {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json; charset=UTF-8',
            'X-CSRFToken': csrfToken
        },
        mode: 'same-origin',
        body: JSON.stringify({
            user: user_id,
            recipe: id,
            title: title.value,
            body: body.value
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success: ', data)

        // Clean input field
        title.value = '';
        body.value = '';

        // Clean comment field
        document.querySelector(`#read-comment-${id}`).innerHTML = '';

        // Update comment field
        render_comments(id);
    })
    .catch(error => console.log('Error: ', error))
}












function btn_shopping(id) {
    console.log(`Click shop button, ingredient belong to recipe id ${id}`)
}
