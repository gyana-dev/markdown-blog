function loadPost(filename) {
  fetch(`posts/${filename}`)
    .then(res => res.text())
    .then(markdown => {
      const html = marked.parse(markdown);
      document.getElementById('post-content').innerHTML = html;
    })
    .catch(err => {
      document.getElementById('post-content').innerHTML = '<p>Failed to load post.</p>';
      console.error('Error loading post:', err);
    });
}
