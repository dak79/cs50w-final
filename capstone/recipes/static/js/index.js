document.addEventListener('DOMContentLoaded', function() {
    const btnCardFollow = document.querySelectorAll('.btn-card-follow');
    const btnCardRecipe = document.querySelectorAll('.btn-card-recipe');
    const btnCardComment = document.querySelectorAll('.btn-card-comment');



    btnCardFollow.forEach(btn =>
        btn.addEventListener('click', event => {

            btn_follow(event.target.dataset.id)
        })
    );

    btnCardRecipe.forEach(btn =>
        btn.addEventListener('click', event =>  {
            if (event.target.innerHTML === "Recipe") {
                btn_recipe(event.target.dataset.id);
                event.target.innerHTML = "Close";
            } else {
                btn_recipe_close(event.target.dataset.id);
                event.target.innerHTML = "Recipe";
            }
        })
    );

    btnCardComment.forEach(btn =>
        btn.addEventListener('click', event =>
            btn_comment(event.target.dataset.id)
        )
    );

})

function btn_follow(id) {
    console.log(`Click follow button with id ${id}`)
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

function btn_comment(id) {
    console.log(`Click comment button wit id ${id}`)

}

function btn_shopping(id) {
    console.log(`Click shop button, ingredient belong to recipe id ${id}`)
}
