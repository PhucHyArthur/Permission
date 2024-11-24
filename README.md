## Pre-Requisites

pip install django
pip install djangorestframework
pip install psycopg2

## DB connections

## dùng DBeaver kết nối vào .env

## link https://www.youtube.com/watch?v=jVr-E9qefOg&t=340s

## tutorial

## cách chạy project, cd backend_erp trước

<!-- 1: chỉ chạy lần lượt 2 câu lệnh này nếu có thay đổi về file models
python manage.py makemigrations
python manage.py migrate

2 chạy câu lệnh này để chạy server cho cả dự án
python manage.py runserver

3 cau lệnh để tạo ra folder mới thay db_diy thành tên folder khác, code class thì code trong file models
python manage.py startapp db_diy -->

## route authentication

<!-- post register : https://backend-erp-drf.vercel.app/api/client/register/
                                         api/employee/register/
post login : https://backend-erp-drf.vercel.app/api/login
get users: https://backend-erp-drf.vercel.app/api/employees-list/
                                /api/clients-list/
                                api/clients/<int:pk>/
                               api/employees/<int:pk>/
 -->

## route inventory zones

<!--
get : https://backend-erp-drf.vercel.app/inventory/zones/
post: https://backend-erp-drf.vercel.app/inventory/zones/add/
delete: https://backend-erp-drf.vercel.app/inventory/zones/add/{id}/
put : https://backend-erp-drf.vercel.app/inventory/zones/add/{id}/
-->

## route inventory racks

<!--
get : https://backend-erp-drf.vercel.app/inventory/racks/
post: https://backend-erp-drf.vercel.app/inventory/racks/add/
delete: https://backend-erp-drf.vercel.app/inventory/racks/add/{id}/
put : https://backend-erp-drf.vercel.app/inventory/racks/add/{id}/
-->

## route inventory raw-materials

<!--
get : https://backend-erp-drf.vercel.app/inventory/raw-materials/
post: https://backend-erp-drf.vercel.app/inventory/raw-materials/add/
delete: https://backend-erp-drf.vercel.app/inventory/raw-materials/add/{id}/
put : https://backend-erp-drf.vercel.app/inventory/raw-materials/add/{id}/
-->

## route inventory locations

<!--
get : https://backend-erp-drf.vercel.app/inventory/locations/
post: https://backend-erp-drf.vercel.app/inventory/locations/add/
delete: https://backend-erp-drf.vercel.app/inventory/locations/add/{id}/
put : https://backend-erp-drf.vercel.app/inventory/locations/add/{id}/
-->

## route inventory locations

<!--
get : https://backend-erp-drf.vercel.app/inventory/finished-products/
post: https://backend-erp-drf.vercel.app/inventory/finished-products/add/
delete: https://backend-erp-drf.vercel.app/inventory/finished-products/add/{id}/
put : https://backend-erp-drf.vercel.app/inventory/finished-products/add/{id}/
-->

## route supplier

<!--
get: https://backend-erp-drf.vercel.app/supplier/supplier/
post: https://backend-erp-drf.vercel.app/supplier/supplier/add
put, delete: https://backend-erp-drf.vercel.app/supplier/supplier/add/{id}/
-->

## route supplier representative

<!--
get: https://backend-erp-drf.vercel.app/supplier/representative/
post: https://backend-erp-drf.vercel.app/supplier/representative/add/
put, delete: https://backend-erp-drf.vercel.app/supplier/representative/add/{id}/
-->

## route supplier bank

 <!--
 get , post : https://backend-erp-drf.vercel.app/supplier/bankingdetail/
post : https://backend-erp-drf.vercel.app/supplier/bankingdetail/add/
 put, delete: https://backend-erp-drf.vercel.app/supplier/bankingdetail/add/{id}/
-->

## route order sales-orders

<!--
get : https://backend-erp-drf.vercel.app/order/sales-orders/
post : https://backend-erp-drf.vercel.app/order/sales-orders/add/
put, delete: https://backend-erp-drf.vercel.app/order/sales-orders/add/{id}/
-->

## route order sales-orders-lines

<!--
get : https://backend-erp-drf.vercel.app/order/sales-orders-lines/
post : https://backend-erp-drf.vercel.app/order/sales-orders-lines/add/
put, delete: https://backend-erp-drf.vercel.app/order/sales-orders-lines/add/{id}/
-->

## route order purchases-orders

<!--
get : https://backend-erp-drf.vercel.app/order/purchases-orders/
post : https://backend-erp-drf.vercel.app/order/purchases-orders/add/
put, delete: https://backend-erp-drf.vercel.app/order/purchases-orders/add/{id}/
-->

## route order purchases-orders-lines

<!--
get : https://backend-erp-drf.vercel.app/order/purchases-orders-lines/
post : https://backend-erp-drf.vercel.app/order/purchases-orders-lines/add/
put, delete: https://backend-erp-drf.vercel.app/order/purchases-orders-lines/add/{id}/
-->

## route cart carts

<!--
get : https://backend-erp-drf.vercel.app/cart/carts/
post : https://backend-erp-drf.vercel.app/cart/carts/add/
put, delete: https://backend-erp-drf.vercel.app/cart/carts/add/{id}/
-->

## route cart carts

<!--
get : https://backend-erp-drf.vercel.app/cart/carts-lines/
post : https://backend-erp-drf.vercel.app/cart/carts-lines/add/
put, delete: https://backend-erp-drf.vercel.app/cart/carts-lines/add/{id}/
-->

## route bill purchases-bills

<!--
get : https://backend-erp-drf.vercel.app/bill/purchases-bills/
post : https://backend-erp-drf.vercel.app/bill/purchases-bills/add/
put, delete: https://backend-erp-drf.vercel.app/bill/purchases-bills/add/{id}/
-->

## route bill sales-bills

<!--
get : https://backend-erp-drf.vercel.app/bill/sales-bills/
post : https://backend-erp-drf.vercel.app/bill/sales-bills/add/
put, delete: https://backend-erp-drf.vercel.app/bill/sales-bills/add/{id}/
-->

## route favorite favorites

<!--
get : https://backend-erp-drf.vercel.app/favorite/favorites/
post : https://backend-erp-drf.vercel.app/favorite/favorites/add/
put, delete: https://backend-erp-drf.vercel.app/favorite/favorites/add/{id}/
-->

## route favorite favorites-lines

<!--
get : https://backend-erp-drf.vercel.app/favorite/favorites-lines/
post : https://backend-erp-drf.vercel.app/favorite/favorites-lines/add/
put, delete: https://backend-erp-drf.vercel.app/favorite/favorites-lines/add/{id}/
-->

## route role

<!--
get  https://backend-erp-drf.vercel.app/api/settings/roles/
post: https://backend-erp-drf.vercel.app/api/settings/roles/add/
put , delete: https://backend-erp-drf.vercel.app/api/settings/roles/add/{id}/ -->
