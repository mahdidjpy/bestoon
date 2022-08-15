




# class FieldsMixin():
# 	def dispatch(self, request, *args, **kwargs):
# 		if request.user.is_superuser :
# 			self.fields = ['title', 'amount', 'user']
# 		elif request.user.is_staff :
# 			self.fields = ['title', 'amount']

# 		return super().dispatch(request, *args, **kwargs)	


