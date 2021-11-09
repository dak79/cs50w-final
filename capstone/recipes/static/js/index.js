document.addEventListener('DOMContentLoaded', function() {
    const btnCardFollow = document.querySelectorAll('.btn-card-follow');
    const btnCardRecipe = document.querySelectorAll('.btn-card-recipe');
    const btnCardComment = document.querySelectorAll('.btn-card-comment');

    btnCardFollow.forEach(btn =>
        btn.addEventListener('click', event =>
            btn_follow(event.target.dataset.id)
        )
    );

    btnCardRecipe.forEach(btn =>
        btn.addEventListener('click', event =>
            btn_recipe(event.target.dataset.id)
        )
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

function btn_recipe(id) {
    console.log(`Click recipe button with id ${id}`)

}

function btn_comment(id) {
    console.log(`Click comment button wit id ${id}`)

}
