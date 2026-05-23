---
layout: home
title: 首页
---

## ![](/assets/img/home-banner.png)

---

### 📚 最新文章

<ul class="post-list">
{% for post in site.posts limit:5 %}
  <li>
    <span class="post-meta">{{ post.date | date: "%Y-%m-%d" }}</span>
    <a class="post-link" href="{{ post.url }}">{{ post.title }}</a>
  </li>
{% endfor %}
</ul>

<p><a href="/posts/">查看全部文章 →</a></p>
