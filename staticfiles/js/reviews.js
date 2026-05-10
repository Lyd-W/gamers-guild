document.addEventListener("DOMContentLoaded", () => {

  console.log("reviews.js loaded");

  const editButtons = document.getElementsByClassName("btn-edit");
  const deleteButtons = document.getElementsByClassName("btn-delete");

  const reviewForm = document.getElementById("reviewForm");
  const commentText = document.getElementById("id_comment");
  const ratingInput = document.getElementById("id_rating");

  if (!reviewForm) {
    console.error("reviewForm not found");
    return;
  }

  const submitButton = reviewForm.querySelector("button[type='submit']");

  // EDIT
  for (let button of editButtons) {
    button.addEventListener("click", (e) => {

      let reviewId = e.currentTarget.dataset.reviewId;

      let commentContent = document.getElementById(
        `review-comment${reviewId}`
      ).innerText;

      let hiddenInput = reviewForm.querySelector("input[name='review_id']");

      if (!hiddenInput) {
        hiddenInput = document.createElement("input");
        hiddenInput.type = "hidden";
        hiddenInput.name = "review_id";
        reviewForm.appendChild(hiddenInput);
      }

      hiddenInput.value = reviewId;

      commentText.value = commentContent;

      submitButton.textContent = "Update Review";
    });
  }

  // DELETE
  const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
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