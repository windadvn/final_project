select bc.id_customer as id_customer, bc.name_customer as name_customer , sum(bt.amount_transaction) as amount
from bigdata_customer bc 
left join bigdata_transaction bt 
on bc.id_customer = bt.id_customer 
group by bc.id_customer, bc.name_customer