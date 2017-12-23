#coding:utf-8


ForeignKey.related_query_name
	外表关联过滤查询
	class Tag(models.Model):
	    article = models.ForeignKey( Article,
	        related_query_name="tag",
	    )
	Article.objects.filter(tag__name="important")
