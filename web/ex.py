# -*- coding:utf-8 -*-
from collections.abc import Iterable
from collections.abc import Iterator

g = (x*x for x in range(10))

a = g.send(None)
a = g.send(1)
print(a)

a = g.send(1)
print(a)

a = g.send(2)
print(a)


a = g.send(2)
print(a)




SELECT
	*　 
FROM
	student s
	RIGHT JOIN classes c ON s.class_id = c.id
	
	
SELECT
	* 
FROM
	student s
	RIGHT JOIN classes c ON s.class_id = c.id
