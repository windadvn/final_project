select bc.country_customer as country,sum(bt.amount_transaction) as amount
from bigdata_customer bc 
left join bigdata_transaction bt 
on bc.id_customer = bt.id_customer
group by country 
order by amount desc