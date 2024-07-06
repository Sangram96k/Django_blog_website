document.addEventListener("DOMContentLoaded", function () {
  let loadMoreButton = document.getElementById("load-more");
  let postContainer = document.querySelector("#post-container .has-scrollbar");
  let currentPage = 1;

  loadMoreButton.addEventListener("click", function () {
    currentPage++;
    fetch(`/load-more-posts/?page=${currentPage}`)
      .then((response) => response.json())
      .then((data) => {
        if (data.posts.length > 0) {
          data.posts.forEach((post) => {
            let postItem = document.createElement("li");
            postItem.classList.add("scrollbar-item");
            postItem.innerHTML = `
              <div class="blog-card">
                <figure class="card-banner img-holder" style="--width: 500; --height: 600;">
                  <img src="${post.post_img}" width="500" height="600" loading="lazy" alt="Perfection has to do with the end product" class="img-cover">
                  <ul class="avatar-list absolute">
                    <li class="avatar-item">
                      <a href="#" class="avatar img-holder" style="--width: 100; --height: 100;">
                        <img src="${post.author_img}" width="100" height="100" loading="lazy" alt="Author" class="img-cover">
                      </a>
                    </li>
                  </ul>
                </figure>
                <div class="card-content">
                  <ul class="card-meta-list">
                    <li><a href="#" class="card-tag">${post.cat}</a></li>
                  </ul>
                  <h3 class="h4"><a href="/post/${post.slug}/" class="card-title hover:underline">${post.title}</a></h3>
                  <p class="card-text">${post.excerpt}</p>
                </div>
              </div>`;
            postContainer.appendChild(postItem);
          });
        } else {
          loadMoreButton.style.display = "none";
        }
      });
  });
});
