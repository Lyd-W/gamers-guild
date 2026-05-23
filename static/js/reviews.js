document.addEventListener("DOMContentLoaded", () => {

  const editButtons = document.getElementsByClassName("btn-edit");
  const deleteButtons = document.getElementsByClassName("btn-delete");

  const reviewForm = document.getElementById("reviewForm");
  const commentText = document.getElementById("id_comment");
  const ratingInput = document.getElementById("id_rating");

  const submitButton = reviewForm.querySelector("button[type='submit']");

  for (let button of editButtons) {
    button.addEventListener("click", (e) => {
      let reviewId = e.currentTarget.dataset.reviewId;

      let commentContent = document.getElementById(
        `review-comment${reviewId}`,
      ).innerText;

      let ratingValue = document.getElementById(`review${reviewId}`).dataset
        .rating;

      let hiddenInput = reviewForm.querySelector("input[name='review_id']");

      if (!hiddenInput) {
        hiddenInput = document.createElement("input");
        hiddenInput.type = "hidden";
        hiddenInput.name = "review_id";
        reviewForm.appendChild(hiddenInput);
      }

      hiddenInput.value = reviewId;

      commentText.value = commentContent;
      ratingInput.value = ratingValue;

      submitButton.textContent = "Update Review";

      reviewForm.action = window.location.pathname + `#review${reviewId}`;
    });
  }

  const deleteModal = new bootstrap.Modal(
    document.getElementById("deleteModal"),
  );

  const deleteConfirm = document.getElementById("deleteConfirm");

  for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
      let reviewId = e.currentTarget.dataset.reviewId;

      deleteConfirm.href = `${window.location.pathname}delete_review/${reviewId}/`;

      deleteModal.show();
    });
  }

  reviewForm.addEventListener("submit", () => {
    submitButton.textContent = "Submit Review";
  });
});
