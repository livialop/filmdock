document.addEventListener("DOMContentLoaded", () => {
    const stars = document.querySelectorAll(".rating-stars i");
    const ratingInput = document.getElementById("rating");

    stars.forEach(star => {
        star.addEventListener("mouseover", () => {
            resetStars();
            highlightStars(star.dataset.value);
        });

        star.addEventListener("mouseout", () => {
            resetStars();
            if (ratingInput.value) highlightStars(ratingInput.value);
        });

        star.addEventListener("click", () => {
            ratingInput.value = star.dataset.value;
            highlightStars(ratingInput.value);
        });
    });

    function highlightStars(count) {
        stars.forEach(s => {
            if (parseInt(s.dataset.value) <= count) {
                s.classList.add("selected");
            }
        });
    }

    function resetStars() {
        stars.forEach(s => s.classList.remove("selected"));
    }
});
