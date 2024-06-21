from typing import Any
from django.views.generic import DetailView, ListView
from .models import Post


class StartingPageView(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data


class PostListView(ListView):
    model = Post
    template_name = "blog/all-posts.html"
    context_object_name = "all_posts"
    ordering = ["-date"]


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post-detail.html"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["post_tags"] = self.object.tags.all()
        return context
