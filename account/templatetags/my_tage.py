from django import template


register = template.Library()


@register.inclusion_tag('registration/partial/active_css.html')
def act_css(request, link_name, content):
	context = {
		'link' : 'account:{}'.format(link_name),
		'request' : request ,
		'link_name' : link_name,
		'content' : content
	}
	return context

