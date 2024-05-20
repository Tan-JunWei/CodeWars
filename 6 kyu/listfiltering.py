# In this kata you will create a function that takes a list of non-negative integers and strings and 
# returns a new list with the strings filtered out.
#examples:
# filter_list([1,2,'a','b']) == [1,2]
# filter_list([1,'a','b',0,15]) == [1,0,15]
# filter_list([1,2,'aasf','1','123',123]) == [1,2,123]

def filter_list(l):
    new = []
    for element in l:
        if isinstance(element,int):  #or if type(element) == int
          new.append(element)
    print(new)
    return new
filter_list([1,2,'a','b'])

#correction: string.isdigit() only works for strings. 

'''
isinstance syntax

isinstance(object, classinfo)
usually use for classes 

e.g
class Polygon:
    def sides_no(self):
        pass

class Triangle(Polygon):  #the child class Triangle is inherited from base class Polygon
    def area(self):
        pass

obj_polygon = Polygon()
obj_triangle = Triangle()

print(type(obj_triangle) == Triangle)   	# true
print(type(obj_triangle) == Polygon)    	# false

print(isinstance(obj_polygon, Polygon)) 	# true
print(isinstance(obj_triangle, Polygon))	# true

In the above example, we see that type() cannot distinguish whether an instance of a class is 
somehow related to the base class. In our case, although obj_triangle is an instance of child class
Triangle, it is inherited from the base class Polygon. If you want to relate the object of a child 
class with the base class, you can achieve this with isinstance().
'''