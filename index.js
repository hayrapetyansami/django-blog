fetch("http://localhost:8000/api/v1/posts/")
  .then(data => data.json())
  .then(({objects}) => {
    objects.forEach(post => {
      console.log(post.title_hy)
    })
  })