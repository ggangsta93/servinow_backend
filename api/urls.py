from django.urls import path, include
from .api import CreateCategoryAPI, ConsultCategory_idAPI
from .api import CategoryAPI, SkillAPI
from rest_framework import routers
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register('category',CategoryAPI)
router.register('skill',SkillAPI)


urlpatterns = [ path('', include(router.urls)),
path('create_category/', CreateCategoryAPI.as_view()),
path('consult_category_id/<int:id>', ConsultCategory_idAPI.as_view())]

#consultar_ofertas/<id_prestador>
#crear_ofertas
#consultar_postulaciones/<id_oferta>

#status para las postulaciones 
