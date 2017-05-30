from content.models import Category
from content.serializers import CategoryDetailedSerializer 


def test(): 

	cat = Category.objects.get(id=1)
	serializer = CategoryDetailedSerializer(cat)
	return serializer
