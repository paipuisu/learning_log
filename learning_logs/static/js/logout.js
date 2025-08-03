document.addEventListener("DOMContentLoaded", function () {
  const logoutLink = document.getElementById("logout-link");
  if (logoutLink) {
    logoutLink.addEventListener("click", function (event) {
      event.preventDefault(); // aタグの通常動作（リンク遷移）を防ぐ
      const form = document.getElementById("logout-form");
      if (form) {
        form.submit();
      }
    });
  }
});
