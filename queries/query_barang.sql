select bp."Product" as produk , bp."Type" as tipe , sum(bt.amount_transaction) as amount 
from bigdata_transaction bt 
left join bigdata_product bp 
on bt.product_transaction = bp."Type" 
group by bp."Product" ,bp."Type" 