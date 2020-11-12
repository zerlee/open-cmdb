# -*- coding: utf-8 -*-
from django.conf.urls import include
from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from .views import GroupViewSet,UserViewSet,UnitaryAuthView

# register的可选参数 base_name: 用来生成urls名字，如果viewset中没有包含queryset, base_name一定要有

router = DefaultRouter()
router.register(r'groups', GroupViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^unitaryauth/$', UnitaryAuthView.as_view())
]
