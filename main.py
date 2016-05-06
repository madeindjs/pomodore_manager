#!/usr/bin/env python
# -*- coding: utf-8 -*-
from classes.category import Category


category = Category()
# category.add('WEB')
category.add(input('Write a name for your category: '))



# category.find_by_name('YT')
# category.find_by_name('PYT')


category.list()